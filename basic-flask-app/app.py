from flask import Flask, render_template, request, abort
import Jetson.GPIO as GPIO
import time
import os

# Pin Definitions
r1_pin = 12  #relay 1
r2_pin = 11  #relay 2
r3_pin = 13  #relay 3

# Pin Setup:
GPIO.setmode(GPIO.BOARD)

# set pin as an output pin with optional initial state of HIGH
GPIO.setup(r1_pin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(r2_pin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(r3_pin, GPIO.OUT, initial=GPIO.HIGH)

# Flask
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/relayhook',methods =['POST'])
def relay():
	GPIO.setwarnings(False)
	if request.method == 'POST':
		status = request.headers.get("status")
		numb = request.headers.get("numb")
		# Relay 1
		if status == "on" and numb == "1":
			GPIO.output(r1_pin, GPIO.LOW)
			return 'success',200
		elif status == "off" and numb == "1":
			GPIO.output(r1_pin, GPIO.HIGH)
			return 'success',200
		# Relay 2
		elif status == "on" and numb == "2":
			GPIO.output(r2_pin, GPIO.LOW)
			return 'success',200
		elif status == "off" and numb == "2":
			GPIO.output(r2_pin, GPIO.HIGH)
			return 'success',200
		# Relay 3
		if status == "on" and numb == "3":
			GPIO.output(r3_pin, GPIO.LOW)
			return 'success',200
		elif status == "off" and numb == "3":
			GPIO.output(r3_pin, GPIO.HIGH)
			return 'success',200
		# All Relays
		elif status == "on" and numb == "0":
			GPIO.output(r1_pin, GPIO.LOW)
			GPIO.output(r2_pin, GPIO.LOW)
			GPIO.output(r3_pin, GPIO.LOW)
			return 'success',200
		elif status == "off" and numb == "0":
			GPIO.output(r1_pin, GPIO.HIGH)
			GPIO.output(r2_pin, GPIO.HIGH)
			GPIO.output(r3_pin, GPIO.HIGH)
			return 'success',200
	else:
		abort(400)

if __name__ == "__main__":
	app.run()

