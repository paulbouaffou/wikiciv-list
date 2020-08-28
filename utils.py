#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# Author: Samuel Guebo & Paul Bouaffou
# Description: Utility file
# License: MIT

# Functions Python in connection with Database TinyDB and others functions

import os
import datetime
from tinydb import TinyDB, Query


def getDb():
	""" Return a Database (TinyDB) object """
	dbFolder = "database"

	if not os.path.exists(dbFolder):
		os.makedirs(dbFolder)

	db = TinyDB(dbFolder + '/db.json')
	return db


def getArticles(limit=10):
	""" Return the number of articles asked in the database """
	db = getDb()
	results = db.all()
	results_limit = results[0:limit]

	return results_limit

def getAllArticles():
	""" Return all the articles in the database """
	db = getDb()
	allresults = db.all()

	return allresults


def createArticle(article):
	""" Insert new article database """
	db = getDb()
	return db.insert(article)


def getNumberArticle():
	""" Get number of article in the database """
	db = getDb()
	article_count = len(db)

	return article_count


def getYear():

	""" Give the year of the moment """
	d = datetime.datetime.now()

	annee = d.year

	return annee

def getDate():

	""" Give the date of the moment """
	date_du_jour = datetime.datetime.today().strftime('%d/%m/%Y')

	return date_du_jour


def verifyDb(page_title):

	""" Verify if article is registred in the database """
	db = getDb()
	Verified = Query()

	verify = db.contains(Verified.title == page_title)

	return verify








	





