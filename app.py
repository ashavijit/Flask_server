from ast import Return
from pydoc import plain
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
load_dotenv()
app=Flask(__name__)

sg=sendgrid.SendGridAPIClient()


# create a mail object

def create_message(email_text):
    return sendgrid.helpers.mail.Mail(
        from_email=os.environ["FROM_EMAIL"],
        to_emails=os.environ["TO_EMAIL"],
        subject="[Alert] Your website is down",
        html_content=email_text,
        plain_text_content=email_text
    )

@app.route('/')
def index():
    return "Hello World";
    


@app.route('/getTime')
def getTime():
    date=datetime.now()
    return  date.strftime('%A %B, %d %Y %H:%M:%S')

@app.errorhandler(InternalServerError)
def handle_500(e):
    error_tb=traceback.format_exc()
    return app.finalize_request(e, from_error_handler=True)

class BigBangException(Exception):
    pass

@app.route('/getTime')
def index():
    raise BigBangException("internal server error")
    return "message sent"


    



    
        

    


  
            








if __name__=='__main__':
    app.run(port=5000 ,debug=True)
    