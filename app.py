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
		
	#return home page
	return render_template('index.html', title = "Accueil | Wikiciv List ")
	
@app.route("/result", methods = ["POST", "GET"])
def result():

	# Number of article in the database
	number_article = utils.getNumberArticle()

	# If form was submitted
	if request.method == "POST":
		limit = 10
		if request.form['limit'] != "":
			limit = int(request.form['limit'])
		# Getting the articles in database
		articles = utils.getArticles(limit)
		return render_template('result.html', title = "Résultats | Wikiciv List ", articles = articles, number_article = number_article)
	# If request is GET
	else:
		return render_template('result.html', title = "Résultats | Wikiciv List ", number_article = number_article)

@app.route("/about")
def about():

	# Return "about: page
	return render_template('about.html', title = "À Propos | Wikiciv List")
	

# Execute the application
if __name__ == '__main__':
	app.run()