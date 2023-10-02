## Job Searching&Recommending System

This is implentation of our Job Searching & Recommending System.

**Code structure**

```
|-- client
|   |-- src
|       |-- index.js
|       |-- component
|
|-- data
|   |-- cloud_developer.json, product_manager.json... software_engineer.json
|
|-- doc
|   |-- group6_final_slides.pdf
|
|-- templates
|   |-- js
|   |-- static
|       |-- css
|   |-- index.html... signup.html
|
|-- ETL\ workflow.ipynb
|-- originJobs2mongo.py
|-- recommend.py
|-- routes.py
|-- search_filters.py
|-- server.py
|-- transformer.py
|-- user.py

```

1. `client` directory contains React code for searching, recommending and rendering job cards.
2. `data` directory contains json format data we got from API.
3. `templates` directory has html code for login and signing up.
4. `ETL workflow.ipynb` grabs data from API and inserts to MongoDB.
5. `originJobs2mongo.py` inserts data under data folder into MongoDB.
6. `server.py` connects front-end with back-end.
7.  `routes.py` and `user.py` defines url redirect for login, allows user to register and login.
8. `recommend.py` and `transformer.py` outputs the recommended jobs, given jobs and user profiles.
9. `search_filters.py` outputs the filtered jobs that meets requirements of user input.

**How to run**

For prepare, run `ETL workflow.ipynb` to grab data into MongoDB, then run `transformer.py` to transform records into embedding for model. Under `client` directory, run `npm install` to install packages. 

For running this application, open two terminal:

Under root directory, run `python server.py` to start Flask engine.

Under `client` directory, run `npm run start` to start front-end

In Browser, input `127.0.0.1:5000/login` to start from login, then login in with register account or sign up a new account. After sign in, you will be redirected to React dashboard where you could search for jobs or get recommended jobs according to your profile.
