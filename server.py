from flask import Flask, request, render_template, redirect, session, jsonify
import json
from search_filters import search_jobs
from recommend import recommend
import pymongo
import pandas as pd
from bson.json_util import dumps
import secrets
from flask_login import LoginManager
from user import User, users_collection, check_password_hash
from bson.objectid import ObjectId



app = Flask(__name__, static_url_path='/static', static_folder='templates/static')
app.secret_key = secrets.token_hex(16)


@app.route("/users")
def users():
    return {"users": ["pc3082", "user2", "user3"]}

@app.route("/search/<role>/<location>/<date>/<remote>/<type>")
def search(role, location, date, remote, type):
    # f = open('data/cloud_developer.json')#test.json')
    # data = json.load(f)
    if remote=="false":
        remote = 'n'
    else:
        remote = 'y'
    list = search_jobs(role, location, date, remote, type)
    # print(len(list))
    if(len(list) == 0):
        f = open('data/cloud_developer.json')#test.json')
        data = json.load(f)
    else:
        tmp = dumps(list)
        json_data = json.loads(tmp)
        data = {}
        data['data'] = json_data
        data = json.dumps(data)

    return data

@app.route("/recommend/<username>/<userinfo>")
def recommend_job(username, userinfo):
    # f = open('data/cloud_developer.json')#test.json')
    # data = json.load(f)
    # print(username, userinfo)
    ##
    print("recommending......")
    document = db['users'].find_one(sort=[("_id", pymongo.DESCENDING)])
    tech_stack = document.get('tech_stack', '')
    location = document.get('location', '')
    jobs_for_looking = document.get('jobs_for_looking', '')
    userinfo=jobs_for_looking+location+tech_stack
    print(userinfo)

    '''["User Experience Researcher", "Greenhouse", "1Vq_lpiZB_wAAAAAAAAAAA==",
    "Intrinsic", 1676937600, "FULLTIME",
    "Researcher", "Mountain View", "CA"], '''

    recommendlist = json.loads(recommend(userinfo))
    keys = ['job_title','job_publisher','job_id',
            'employer_name','job_posted_at_timestamp','job_employment_type',
            'job_job_title', 'job_city','job_state']
    data_map =  [{keys[i]: row[i] for i in range(len(keys))} for row in recommendlist]
    data = json.dumps(data_map)
    # print(data)
    return data


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


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["bigdata"]
    collections = ["cloud_developer", "data_scientist", "researcher", "software_engineer", "technical_manager"]
    usercollect=['users']
    app.run(debug=True)
