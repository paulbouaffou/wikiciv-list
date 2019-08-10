#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# Author: Samuel Guebo & Paul Bouaffou
# Description: Utility file
# License: MIT

# Functions Python in connection with Database TinyDB

import os
from tinydb import TinyDB, Query


def getDb():
	""" Return a Database (TinyDB) object """
	dbFolder = "database"
	if not os.path.exists(dbFolder):
		os.makedirs(dbFolder)

	db = TinyDB(dbFolder + '/db.json')
	return db


def getArticles(limit=10):
	""" Return all articles in the database """
	db = getDb()
	results = db.all()
	results_limit = results[0:limit]

	return results_limit


def createArticle(article):
	""" Insert new article database """
	db = getDb()
	return db.insert(article)

def getNumberArticle():
	""" Get number of article in the database """
	db = getDb()
	article_count = len(db)

	return article_count

'''def function():
	"""Get category number of article in the database"""
	Article = Query()
	article_source = db.search(Article.wikitext == )

	return'''
