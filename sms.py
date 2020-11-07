import os
from flask import Flask, request, redirect
from flask import render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import time
import pymongo
from pymongo import MongoClient

cluster = MongoClient("<<Your MongoDB URL>>")
db = cluster["<<Your cluster name>>"]
collection = db["<<Your collection name>>"]

app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    postCount = collection.count()
    latestTemp = postCount - 1

    results = collection.find({"_id":latestTemp})

    for result in results:
        currentTemp = result["temperature"]

    resp = MessagingResponse()
    resp.message("Incoming temperature: {}".format(currentTemp))
    return str(resp)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)
