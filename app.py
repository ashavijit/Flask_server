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
app=Flask(__name__)

@app.route('/')
def index():
    return "Hello World";
    


@app.route('/getTime')
def getTime():
    date=datetime.now()
    return  date.strftime('%A %B, %d %Y %H:%M:%S')



    



    
        

    


  
            








if __name__=='__main__':
    app.run(port=5000 ,debug=True)
    