#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
# Description: Générateur d'articles wikipedia à améliorer pour CIV
# Auteurs: Samuel Guebo & Paul Bouaffou
# Licence: MIT

import json
import requests
import utils

def runMediaWikiRequest(url):
		"""
		function to give resultat of url request
		"""
		resultatJson = requests.get(url).content
		# return the json text
		return resultatJson


def setup():
	""" Main entry point for the tool.
		It gets all articles from CIV archives
	"""

	try:
		civ_archives_url = "https://fr.wikipedia.org/w/api.php?action=parse&format=json&page=Projet:C%C3%B4te_d%27Ivoire/Articles_r%C3%A9cents/Archive&prop=links"
		archives_json = runMediaWikiRequest(civ_archives_url)

		# convert from plain text to python array, and browse to get items 'parse'
		# and its child 'links'
		archives_links = json.loads(archives_json)['parse']['links']

		# just the two first items of the array

		links_test = archives_links

		# initiate counter
		articles_count = 0

		# loop through the small set
		for link in links_test:
			page_title = link['*']# build the url
			page_templates_url = "https://fr.wikipedia.org/w/api.php?action=parse&format=json&page="
			page_templates_url += page_title + "&prop=templates"

			# run an Http request and get the template of each page
			page_templates_json = runMediaWikiRequest(page_templates_url)
			page_templates = json.loads(page_templates_json)['parse']['templates']


			# if the page has any templates
			if(len(page_templates) > 0):

				# Define which templates are considered problematic
				modele_bandeau = [
					"Modèle:Méta bandeau d'avertissement"
				]

				# search for problematic templates
				for template in page_templates:
					if template["*"] in modele_bandeau:
						
						# all the articles at problem in archive civ
						article = {
							"title" : page_title
						}

						if not utils.verifyDb(page_title):

							utils.createArticle(article)

						else:
							print('Article enregistré !')
	except KeyError:
		print('Enregistrement effectué avec succès !')

					#articles_count += 1
					
# Execute the application
if __name__ == '__main__':
	setup()