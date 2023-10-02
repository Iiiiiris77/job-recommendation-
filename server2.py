from flask import Flask, request, render_template, redirect, session, jsonify
import json
from flask_login import LoginManager
from user import User, users_collection, check_password_hash
import pymongo
import secrets
##from routes import bp as routes_bp
from bson.objectid import ObjectId
#from recommend import recommend

app = Flask(__name__, static_url_path='/static', static_folder='templates/static')
##app.register_blueprint(routes_bp)
app.secret_key = secrets.token_hex(16)
##@app.route("/users")
##def users():
##    return {"users": ["pc3082", "user2", "user3"]}



@app.route('/register', methods= ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username =request.form.get('username')
        password = request.form.get('password')
        jobs_for_looking = request.form.get('jobs_for_looking')
        tech_stack = request.form.get('tech_stack')
        location = request.form.get('location')
        user = User(username=username, password=password, jobs_for_looking=jobs_for_looking, tech_stack=tech_stack, location=location)
        user.save()
        return redirect('/success')

    return render_template('index.html')

@app.route('/success', methods=['GET', 'POST'])
def success():


    return render_template('success.html')

 # Define route for user login
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Get form data from request
        #data = request.get_json()
        # Find the user in the database
        user = users_collection.find_one({'username': request.form.get('username')})
        print("1111" + user['password'])
        if user and check_password_hash(user['password'], request.form.get('password')):
        # If login credentials are valid, store user_id in session
            session['id'] = str(user['_id'])
            print(str(user['_id']))
            return redirect('http://localhost:3000/react-octo-job-search-003')
            #return jsonify({'success': True, 'username': user['username']})
        else:
            error_message = 'Invalid username or password. Please try again.'
            return render_template('login.html', error_message=error_message)
            #return jsonify({'success': False, 'message': error_message})
    else:
        return render_template('login.html')

@app.route('/recommend/<username>', methods=['GET','POST'])
def recommend(username):
    # Retrieve user ID from session
    user_id = session.get('id')
    if user_id:
        # If user is logged in, retrieve user profile from database and render dashboard
        user = users_collection.find_one({'_id': ObjectId(user_id)})
        #jobs = recommend(user['tech_stack'] + user['location'] + user['jobs_for_looking'])
        null = None
        jobs = [["Data Scientist", "LinkedIn", "XPfmHZvGz0kAAAAAAAAAAA==", "Xorbix Technologies, Inc.", 1682018436, "FULLTIME", "Data scientist", null, null], ["Google Cloud Developers", "Salary.com", "V-ICfI4Ry5oAAAAAAAAAAA==", "Cosmos IT Solutions", 1678233600, "FULLTIME", null, null, null], ["Software Engineer (Python)", "LinkedIn", "nzwzIn5vA6gAAAAAAAAAAA==", "Concept International", 1681902463, "FULLTIME", "Software engineer", null, null], ["ERP Oracle Cloud Developer - Oracle HCM", "LinkedIn", "qeFQHc7dvMAAAAAAAAAAAA==", "CyberCoders", 1681837173, "FULLTIME", null, "Farmington", "MI"], ["Software Engineer (Mid)", "Careers - Sev1Tech, LLC. - ICIMS", "4SL3vhydGPoAAAAAAAAAAA==", "Sev1Tech", 1618751508, "FULLTIME", "Software engineer", null, null], ["Senior Cloud Developer - Full Stack", "Indeed", "34CyhBk-iaQAAAAAAAAAAA==", "Avance Consulting", 1682033555, "FULLTIME", "Senior", null, null], ["Cloud Developer", "Snagajob", "GrvNB_moe6sAAAAAAAAAAA==", "Collabera", 1681860282, "FULLTIME", null, "Columbus", "OH"], ["Software/Cloud Developer", "WGN-TV Jobs", "rWz6fFMDmqoAAAAAAAAAAA==", "GENERAL DYNAMICS INFORMATION TECHNOLOGY", 1681023958, "FULLTIME", null, null, "MA"], ["Quantitative Researcher", "Salary.com", "9OSFUWJ_1HYAAAAAAAAAAA==", "Aresfi", 1681862400, "FULLTIME", "Researcher", "Incline Village", "NV"], ["Lead Cloud Developer(AWS)", "Indeed", "PmQjIr8xXCAAAAAAAAAAAA==", "FalconSmartIT", 1666122377, "FULLTIME", null, "Dover", "DE"]]

        ##
        print(user)
        ##print(jobs)
        #return jsonify({'success': True, 'user': user})
        return render_template('dashboard.html', user=user, jobs=jobs)
    else:
        # If user is not logged in, redirect to login page
        return redirect('/login')
        #return jsonify({'success': False, 'message': 'User not logged in.'})

@app.route('/findall')
def findall():
    alluser =  users_collection.find()
    for u in alluser:
        print(u)
    return render_template('findall.html',users=alluser)

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('id', None)
    print("here")
    return redirect('/login')

@app.route("/search/<role>/<location>/<date>/<remote>/<type>")
def search(role, location="United States", date='any_time', remote = False, type = "FULLTIME"):
    f = open('data/cloud_developer.json')#test.json')
    data = json.load(f)
    # list = search_jobs(role, location, date_posted, remote_jobs_only, employment_type)
    # data = json.dumps(list)
    # print(data)

    return data

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["bigdata"]
    collections = ["cloud_developer", "data_scientist", "researcher", "software_engineer", "technical_manager"]
    app.run(port=5001)
