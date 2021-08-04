#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Auteurs: Samuel Guébo & Paul Bouaffou

from flask import Flask
from flask import render_template
from flask import request
import utils
import update

app = Flask(__name__)

@app.route("/")
def home():
	# return home page
	
	return render_template('index.html', title = "Accueil | Gawa Côte d'Ivoire ")

@app.route("/result")
def result():
	
	return render_template('index.html', title = "Accueil | Gawa Côte d'Ivoire ")
	
@app.route("/updated")
def updated():

	return render_template('index.html', title = "Accueil | Gawa Côte d'Ivoire ")

@app.route("/admin")
def admin():
	
	return render_template('index.html', title = "Accueil | Gawa Côte d'Ivoire ")
	
# Execute the application
if __name__ == '__main__':
	app.run()
