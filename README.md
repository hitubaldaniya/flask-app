## Python Flask App
- Just to demonstrate CRUD operations with SQLite database using Flask framework.

### Installation and Setup Instructions:
1. Clone the repository or download the zip file.
2. Make sure you have Python installed in your system. (https://www.python.org/downloads/)
3. Open Command Prompt or Terminal, and navigate to the directory where you have downloaded or cloned the Repository.
3. Open the terminal(cmd) from the root directory of the cloned folder.
4. Now install the required packages by following steps

### Install Virtual Environment
- pip install virtualenv

### Create a virtual environment
- virtualenv env 
-> If you are reveiving an error in creating virtualenv run the following command
- Set-ExecutionPolicy unrestricted (Run in PowerShell)(Yes to all)

### Enter into(activate) the virtual environment
- .\env\Scripts\activate.ps1 (enter into the environment and install necessary package inside it)
- Once it is activated, now the things will run into this virtual environment only

### Install Flask
- pip install flask
- pip install flask-sqlalchemy (Database)

### Create DB (inside env)
- run: python
- run: from app import app, db - (initially you can just import db)
- run: app.app_context().push() - (with just import db do not run this command move to next directly)
- run: db.create_all()
- you will see instance > todo.db
- Install the "Jinja2 Snippet Kit" extension in 'VS Code' to help display dynamic stuff in the HTML

### Install Gunicorn
- pip install gunicorn
- with this, we can serve our app in multiple threads
- with this, we can make our application live on any server like Heroku etc.
- pip freeze > requirements.txt
- create a Procfile which is gonna used by Heroku.

### Create a Heroku account and install Heroku CLI
- run command: "Heroku" (to see if cli working properly)
- run command: "Heroku create app-name" (create a new app in Heroku)

### App Url (Url stopped working as Heroku requires a payment)
- https://flasksqlite-todo-b173f1a4fb85.herokuapp.com/

### APP View
![List Page](https://raw.githubusercontent.com/hitubaldaniya/flask-app/main/static/img/todo-list.png)

![Update Page](https://raw.githubusercontent.com/hitubaldaniya/flask-app/main/static/img/update-todo.png)

### Keep in mind
- There is no expra features available like form validation, proper designing etc...
