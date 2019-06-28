#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################################################################
#                                                                                                #
# Description: Application pour lister les articles de CIV à problèmes pour un editathon         #
# Auteurs: Samuel Guebo & Paul Bouaffou                                                          #
# Licence: MIT                                                                                   #
#                                                                                                #
##################################################################################################

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template('index.html')

