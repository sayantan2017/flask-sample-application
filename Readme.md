We will require two packages to set up your environment. virtualenv for a user to create multiple Python environments side-by-side. Thereby, it can avoid compatibility issues between the different versions of the libraries and the next will be Flask itself. 

virtualenv cration
pip install virtualenv

Create Python virtual environment
virtualenv venv

Activate virtual environment
venv\Scripts\activate

If you are getting some issues then activate windows virtual enviroment policies.
Open powershell and run below command

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUse

Run Flask application Syntax

We can run the Flask application using the below command.

flask –app <app_name> run
flask run
python app_name.py

Routing


