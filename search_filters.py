import pymongo
import datetime
import pandas as pd
from textblob import TextBlob


client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["bigdata"]

collections = ["cloud_developer", "data_scientist", "researcher", "software_engineer", "technical_manager"]

country = {"us": "US", "usa": "US", "united states": "US"}

states = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 
          'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 
          'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy', 'dc', 'as', 'gu', 'mp', 'pr', 'um', 'vi']

states_abbreviation = {
    "alabama": "AL",
    "alaska": "AK",
    "arizona": "AZ",
    "arkansas": "AR",
    "california": "CA",
    "colorado": "CO",
    "connecticut": "CT",
    "delaware": "DE",
    "florida": "FL",
    "georgia": "GA",
    "hawaii": "HI",
    "idaho": "ID",
    "illinois": "IL",
    "indiana": "IN",
    "iowa": "IA",
    "kansas": "KS",
    "kentucky": "KY",
    "louisiana": "LA",
    "maine": "ME",
    "maryland": "MD",
    "massachusetts": "MA",
    "michigan": "MI",
    "minnesota": "MN",
    "mississippi": "MS",
    "missouri": "MO",
    "montana": "MT",
    "nebraska": "NE",
    "nevada": "NV",
    "new hampshire": "NH",
    "new jersey": "NJ",
    "new mexico": "NM",
    "new york": "NY",
    "north carolina": "NC",
    "north dakota": "ND",
    "ohio": "OH",
    "oklahoma": "OK",
    "oregon": "OR",
    "pennsylvania": "PA",
    "rhode island": "RI",
    "south carolina": "SC",
    "south dakota": "SD",
    "tennessee": "TN",
    "texas": "TX",
    "utah": "UT",
    "vermont": "VT",
    "virginia": "VA",
    "washington": "WA",
    "west virginia": "WV",
    "wisconsin": "WI",
    "wyoming": "WY",
    "district of columbia": "DC",
    "american samoa": "AS",
    "guam": "GU",
    "northern mariana islands": "MP",
    "puerto rico": "PR",
    "united states minor outlying islands": "UM",
    "u.s. virgin islands": "VI",
}

def correct_spelling(text):
    return str(TextBlob(text).correct())

def search_jobs(job_title=None, location=None, date_posted=None, remote_jobs_only=None, employment_type=None):
    query = {}
    if job_title:
        # Correct typo in the job title and the location with TextBlob
        job_title = correct_spelling(job_title.lower()) 
        print(job_title)
        # Use a case-insensitive regex for partial matching
        query["job_title"] = {"$regex": job_title, "$options": "i"} 

    if location:
        location = correct_spelling(location.lower())
        print(location)
        if location in country:
            print(country[location])
            query["job_country"] = {"$regex": country[location], "$options": "i"}
        elif location in states:
            print(location)
            query["job_state"] = {"$regex": location, "$options": "i"}
        elif location in states_abbreviation:
            print(states_abbreviation[location])
            query["job_state"] = {"$regex": states_abbreviation[location], "$options": "i"}
        else: # City
            query["job_city"] = {"$regex": location, "$options": "i"}

    if date_posted:
        current_time = datetime.datetime.now()
        if date_posted == "past 24 hours":
            time_threshold = current_time - datetime.timedelta(days=1)
        elif date_posted == "past week":
            time_threshold = current_time - datetime.timedelta(weeks=1)
        elif date_posted == "past month":
            time_threshold = current_time - datetime.timedelta(weeks=4)
        else:  # Default to any time
            time_threshold = None
        if time_threshold:
            query["job_posted_at_datetime_utc"] = {"$gte": time_threshold.isoformat()}

    if remote_jobs_only:
        query["job_is_remote"] = True

    if employment_type:
        query["job_employment_type"] = {"$regex": employment_type, "$options": "i"}

    matching_jobs = []
    
    for collection_name in collections:
        collection = db[collection_name]
        for job in collection.find(query):
            matching_jobs.append(job)

    """
    if sort_by == "most recent":
        matching_jobs.sort(key=lambda x: x['job_posted_at_datetime_utc'], reverse=True)
    elif sort_by == "most relevant":
        matching_jobs.sort(key=lambda x: len(set(job_title.lower().split()) & set(x['job_title'].lower().split())) / len(x['job_title'].lower().split()), reverse=True)
    """

    matching_jobs.sort(key=lambda x: len(set(job_title.lower().split()) & set(x['job_title'].lower().split())) / len(x['job_title'].lower().split()), reverse=True)

    return matching_jobs

##### comment out for running server #######
# if __name__ == "__main__":
#     job_title_filter = input("Enter job title (e.g., Data Scientist): ")
#     location_filter = input("Enter location (city, state, or country): ")
#     date_posted_filter = input("Enter date posted (any time, past 24 hours, past week, past month): ")
#     remote_jobs_only_filter = input("Remote jobs only? (y/n): ").lower() == "y"
#     employment_type_filter = input("Enter employment type (FULLTIME, CONTRACTOR, PARTTIME, INTERN): ")
# #    sort_by_filter = input("Enter sorting type (most recent, most relevant): ")


# result = search_jobs(job_title=job_title_filter, location=location_filter, date_posted=date_posted_filter,
#                      remote_jobs_only=remote_jobs_only_filter, employment_type=employment_type_filter)

# # Create a pandas DataFrame from the job data
# df = pd.DataFrame(result)

# # Save the DataFrame to an Excel file
# df.to_excel('result.xlsx', index=False)
