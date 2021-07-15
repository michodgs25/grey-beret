<h2 align="center">Weather App</h2>
<div align="center">
<img src="https://cdn.givingcompass.org/wp-content/uploads/2019/12/02081412/Climate-Change-and-the-New-Language-of-Weather-800x450.jpg" 
     target="_blank" rel="noopener" alt="Products">
</div>

# Project Overview
Knowing what the weather is like at your location, is key to deciding your wardrobe, which time to arrive and whether to go in the first place.

## Purpose
The purpose of the application is to allow users to find out the weather at their location or a destination by entering the postcode, town/city.

## Contents
* [purpose](#Purpose)
* [wireframes](#Wireframes)
   * [Homepage-wireframe](#Homepage-wireframes)
   * [Add-or-Edit-wireframe](#Add-or-Edit-wireframes)
* [Database](#Database)
* [Heroku](#Heroku)
* [Technologies](#Technologies)
     * [Languages](#Languages)
     * [Libraries](#Libraries)
* [Deployment](#Deployment)
     * [Heroku](#Heroku)
* [Acknowledgements](#Acknowledgements)
     * [External-Media](#External-Media)

----------------

## Wireframes

<h2 align="center">Homepage</h2>

<div align="center">
<img src="" 
     target="_blank" rel="noopener" alt="Homepage wireframe">
</div>

<h2 align="center">Search</h2>

<div align="center">
<img src="" 
     target="_blank" rel="noopener" alt="Add or Edit wireframe">
</div>

<h2 align="center">Results</h2>

<div align="center">
<img src="" 
     target="_blank" rel="noopener" alt="Add or Edit wireframe">
</div>


## Database
I chose MongoDB as my chosen database, because MongoDB provides high performance data persistence. In particular,

Support for embedded data models reduces I/O activity on database system.
Indexes support faster queries and can include keys from embedded documents and arrays.
Rich Query Language
MongoDB supports a rich query language to support read and write operations (CRUD) see more at: https://docs.mongodb.com/manual/introduction/


## Heroku 

I hosted the product table on Heroku as it is simple to set up for small scale projects such as this. See more at - https://devcenter.heroku.com/


## Technologies 

* W3S html& css validator - https://validator.w3.org/: Tested both my HTML& CSS code and provided feedback to improve quality.

* Google dev tools: found top right corner of the chrome browser, more tool then bottom option. Provided a virtual testing environment.

### Languages

In this project I used *HTML5*, *CSS*, *PYTHON* and *JINJA* programming languages.

### Libraries

- Flask 
* https://flask.palletsprojects.com/en/2.0.x/

- MongoDb
* https://www.mongodb.com/

- Materialize CSS and JS Libraries: 
* https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css 

* https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js

- Python 3.7: https://www.python.org/

- Font Awesome: https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css

- JQuery library: https://jquery.com/ 

## Deployment

#### Requirements 
You will need the following tools installed on your system:

Python 3 - https://www.python.org/downloads/
An IDE such as Visual Studio, gitpod, Code, or like this project gitpod
An account at MongoDB Atlas - https://account.mongodb.com/account/login
Git - https://gist.github.com/derhuerst/1b15ff4652a867391f03


I personally used github on my local machine to develop the site using Python 3.7.3 and deployed to Heroku via Github.

1. To download or clone the site to your local machine you will need to go to my repo [here.](https://github.com/michodgs25/jeffs-store) and see deployment steps in https://help.github.com/en/articles/cloning-a-repository

2. Before you download or clone the site you will need to ensure you have Python 3.7 or above installed.

3. Once you have Python installed, created a virtual environment as appropriate to your chosen IDE and os.

4. Run the requirements.txt file as appropriate to your IDE to install the relevant required packages dependencies for the project into your virtual environment.

5. Create a MONGODB account, Create a cluster and follow the mongodb steps to connecting with your application.

6. I created an env.py file(make sure its added to '.gitignore' file. As to ensure no secret keys are exposed) and add the following:
  - **IP**: `0.0.0.0`
  - **PORT**: `8000`
  - **MONGO_URI**: `string to connect with MongoDB`
  - **SECRET_KEY**: `your chosen secret key`

7. Add these to the top of your app.py file:
```
import os
from flask import (
    Flask, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env
 ```

8. Run the app.py file as appropriate to your chosen environment and os.

9. You should now be able to view the site on your localhost on port 8000.


## Heroku

#### Instructions
To deploy this app to Heroku you need to follow the steps below:

- Create a **requirements.txt** file so that Heroku can install all the dependencies required to run the app.
  `pip freeze > requirements.txt`

- Create a **Procfile** with the command:
  `echo web: python app.py > Procfile`

- In this step, you have to create a free account on the [Heroku website](https://signup.heroku.com/).
-  Login to the account, click on new and then create a new app. In the following screen, you need to give a name and choose the Europe region.
-  In the menu access the **Deploy** option, after that click on Connect to Github. Just below provide the information from the app's repository on GitHub and select the option Enable Automatic Deploy.
- On the Dashboard of the APP, click on Settings and then click on the option **Reveal config Vars**.
- Now you need to add the following variables to **Reveal config Vars**:
  - **IP**: `0.0.0.0`
  - **PORT**: `8000`
  - **MONGO_URI**: `string to connect with MongoDB`
  - **SECRET_KEY**: `your chosen secret key`
- You are now ready to access the deployed app on Heroku.


## Acknowledgements

Thank you to Clere group for providing me the opportunity to display my skills.

### External-Media
All images were take from Google images advanced search with filter - __"free to use or share"__

Wireframe images were taken from __https://github.com/deltabrot/clere-coding-challenge-api__
