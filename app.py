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

app = Flask(__name__)


@app.route("/")
def accueil():
    return render_template('index.html')
