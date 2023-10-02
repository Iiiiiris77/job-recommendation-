import pymongo
import json
import os

def insert_json_to_mongodb(filename, collection):
    # convert json to diction
    with open(filename, 'r', encoding='utf-8') as f:
        data_dict = json.load(f)

    # 将data插入collection
    #collection.insert_one(data_dict)
    job_dict = {}
    for i in range(len(data_dict["data"])):
        job_dict = data_dict["data"][i]
        collection.insert_one(job_dict)

# connect to mogodb

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["bigdata"]

# All colletcions in db
collections = ["cloud_developer", "data_scientist", "jobs_data", "product_manager", "researcher", "software_engineer", "technical_manager"]

# insert to MongoDB
for collection_name in collections:
    collection = db[collection_name]
    filename = f"data/{collection_name}.json"
    insert_json_to_mongodb(filename, collection)
