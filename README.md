# Text To Receive Temperature

## Description

> This program connects to an existing MongoDB database to obtain the latest temperature reading from a temperature sensor (to set up the sensor and upload the readings to MongoDB, see https://github.com/cvizer/temperature_sensor_program).

To see the current temperature, all you need to do is send a text message to your Twilio phone number. You'll receive a response with the latest temperature reading.

---

## You Will Need

* Twilio account

* MongoDB database

* ngrok installed on your computer

---

## How To Use

First, we will need to make a few changes to sms.py. Replace "Your MongoDB URL" in line 10 with your actual MongoDB URL:

```python
    cluster = MongoClient("<<Your MongoDB URL>>")
```

We will also need to replace "Your cluster name" in line 11 with your actual cluster name:

```python
    db = cluster["<<Your cluster name>>"]
```

Next, replace "Your collection name" in line 12 with your actual cluster name:

```python
    collection = db["<<Your collection name>>"]
```

Now we need to start ngrok to forward requests to your local server. Run this from the command line:

`./ngrok http 5000`

Now copy the first ngrok forwarding URL from the command line window and paste it into Twilio > Active Number > Messaging > A message comes in > Webhook.

Open another command line window and cd into your directory where you saved sms.py. 

Then, run:

`python sms.py`

You're all set up to receive text messages with the latest temperature reading stored in your MongoDB database. Simply send a text message to your Twilio phone number and you'll receive a response within seconds.

---

## Author Info

- Github - [github.com/cvizer](https://github.com/cvizer)
- Email - <chelseavizer@yahoo.com>

[Back To Top](#text-to-receive-temperature)
