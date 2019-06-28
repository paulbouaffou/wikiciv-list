#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
#                                                                            #
# Description: Application pour lister les articles de CIV
# à problèmes pour
# Licence: MIT                                                               #
#                                                                            #
##############################################################################

from flask import Flask
from flask import render_template
from flask import request
import utils

app = Flask(__name__)


@app.route("/")
@app.route("/", methods = ["GET", "POST"])
def accueil():

	# If form was submitted 
	if request.methods == "POST":
		limit = 10
		if request.form['limit'] != "":
    		limit = request.form['limit']
		
		articles = utils.getArticles(limit)
		return render_template('index.html', articles=articles)
    
    # If request is GET
    else:
    	return render_template('index.html')
