from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, jsonify, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
##from server import app, db
from user import User, users_collection
from flask import render_template

bp = Blueprint('routes', __name__)

# Define route for user registration
@bp.route('/register', methods=['POST'])
def register():
    ##global user_id_counter
    # Get form data from request
    data = request.get_json()
    username =data.get('username')
    password = data.get('password')
    tech_stack = data.get('tech_stack')
    location = data.get('location')

    user_id = users_collection.count_documents({}) + 1
    
    user = User(id=user_id, username=username, password=password, tech_stack=tech_stack, location=location)
    print(user)
    user.save() 

    # e.g. user.save()
    return render_template('signup.html')

# Define route for user login
#@bp.route('/login', methods=['POST'])
#def login():
    # Get form data from request
#    data = request.get_json()
    # Find the user in the database
 #   user = users_collection.find_one({'id': data['id']})
 #   if user and check_password_hash(user['password'], data['password']):
  #      # If login credentials are valid, store user_id in session
#        session['id'] = str(user['id'])
 #       return render_template('login.html')
#    else:
 #       return jsonify({'message': 'Invalid username or password'}), 401

    

@bp.route('/logout', methods=['POST','DELETE'])
@login_required
def logout():
    session.pop('id', None)
    return redirect('/login')

@bp.route('/dashboard', methods=['GET'])
def dashboard():
    # Check if user is logged in by checking session
    if 'id' in session:
        # Query MongoDB to find User document with user_id in session
        user = users_collection.find_one({'id': ObjectId(session['id'])})
        if user:
            # Render dashboard page with user information
            return render_template('dashboard.html')

    # If user is not logged in, redirect to login page
    return redirect('/login')
