# DataSecurity
###How to run:
     pip install -r requirements.txt
#####In src directory:
     export FLASK_APP app.py
     flask run
 ##App Description
 Simple app that allows user to login and upload posts. 
 User is registered to SQLlite database. 
 ##Generating SSL certificate
 #####in src folder:
    openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
 ##DataBase
 #####Run this script
    dbSetup.py