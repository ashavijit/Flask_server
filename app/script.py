from ast import Return
from turtle import color
from urllib import response
from flask import Flask,request
import time
from datetime import datetime
from flask_mail import Mail, Message
import traceback
from werkzeug.exceptions import InternalServerError
import sendgrid
from dotenv import load_dotenv
import os
sg=sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
app=Flask(__name__)

@app.route('/')
def index():
    return "Hello World";
    


@app.route('/getTime')
def getTime():
    date=datetime.now()
    return  date.strftime('%A %B, %d %Y %H:%M:%S')

@app.route('/getTime')

def create_message(email_text):
    return sendgrid.helpers.mail.Mail(
        from_email=os.environ["SENDGRID_FROM_EMAIL"],
        to_emails=os.environ["SENDGRID_TO_EMAIL"],
        subject="Server is not working",
        html_content=email_text
    )

@app.errorhandler(InternalServerError)
def handle_500_error(exception):
    error_tb=traceback.format_exc()
    try:
        resp=sg.send(create_message(error_tb))
    except Exception as e:
        print(e.message)

    return app.finalize_request(e,from_error_handler=True)


    



    
        

    


  
            








if __name__=='__main__':
    app.run(debug=True)
    