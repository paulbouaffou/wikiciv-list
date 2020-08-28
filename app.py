#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Auteurs: Samuel Guébo & Paul Bouaffou

from flask import Flask
from flask import render_template
from flask import request
import utils
import update

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
	# return home page
	
	# return year actual
	year = utils.giveYear()

	# Number of article in the database
	number_article = utils.getNumberArticle()

	# If form was submitted
	if request.method == "POST":
		limit = 10
		if request.form['limit'] != "":
			limit = int(request.form['limit'])
		# Getting the articles in database
		articles = utils.getArticles(limit)
		return render_template('index.html', title = "Résultats | Gawa Côte d'Ivoire ", articles = articles, number_article = number_article, year = year, limit = limit)
	# If request is GET
	else:
		return render_template('index.html', title = "Accueil | Gawa Côte d'Ivoire ", number_article = number_article, year = year)

@app.route("/result")
def result():

	# return year actual
	year = utils.giveYear()

	# Number of article in the database
	number_article = utils.getNumberArticle()
	
	# Number of article in the database
	all_articles = utils.getAllArticles()
	
	return render_template('result.html', title = "Résultats de tous les articles à améliorer | Gawa Côte d'Ivoire ", number_article = number_article, all_articles = all_articles, year = year)
	
@app.route("/updated")
def updated():
	# return page without information. But a bot is operating background this page

	# Turn the bot
	miseajour = update.setup()

	return render_template('api.html', title = "Résultats API | Gawa Côte d'Ivoire ", miseajour = miseajour)

@app.route("/admin")
def admin():

	# Number of article in the database
	number_article = utils.getNumberArticle()

	# Number of article in archive Ivory Cost
	all_article_archive = update.app()

	# Number of article in archive Ivory Cost which has not problem
	rest_article_archive = update.difference()
	
	return render_template('admin.html', title = "Administration | Gawa Côte d'Ivoire ", number_article = number_article, all_article_archive = all_article_archive, rest_article_archive = rest_article_archive)

# Execute the application
if __name__ == '__main__':
	app.run()