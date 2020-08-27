
		 
	 												      												  
#auteur: Paul Bouaffou ;						              
	 												      												  
#description: Programme donnant le nombre de contributions d'un utilisateur		              
	                sur les Projets WIKI en langue française (Exemples: Wikipédia, Wikimedia Commons,    
	                Wikiquote, Wikidata, Wikitionnaire, ...). [NB]: Il s'exécute en ligne de commande ;  
	 												      											  
	* @licence: MIT ;									
	*/

	// Presentation succincte de l'application
	echo "\nBienvenu(e) sur l'application dénommée 'media-wiki-contribution' !!!\n";

	// Précision de la langue utlisé pour une meilleure affichage des contributions
	echo "NB: Cette application concerne uniquement les contributeurs des projets WIKI en langue française. \n\n";

	// Renseignement du nom d'utilisateur sur les projets WIKI
	echo "Veuillez renseignez votre username : ";
	$username = readline();

	// Tableau de lien des projets WIKI
	$project_wiki_link = array('fr.wikipedia.org', 'commons.wikimedia.org', 'fr.wikiquote.org', 'wikidata.org', 'fr.wiktionary.org');

	// Tableau de nom des projets WIKI
	$project_wiki_name = array('Wikipedia', 'Wikimedia Commons', 'Wikiquote', 'Wikidata', 'Wikitionnaire');

	// Découpage de l'URL

	$link_1 = "https://";   // Hôte

	$link_2 = "/w/api.php?action=query&format=json&list=users&ususers=";   //  Paramètre de l'URL

	$link_3 = "&usprop=editcount";   // Paramètre de l'URL

	// Variable qui regroupera tous les éléments de l'URL ci-dessus
	$link_all = NULL;
	
	// Boucle faisant l'alternance des éléments du tableau numéroté 1 afin de traiter chaque lien wiki.
	for ($link_wiki=0; $link_wiki < 5; $link_wiki++) {

		// Formation de l'URL
		$link_all = $link_1.$project_wiki_link[$link_wiki].$link_2.urlencode($username).$link_3;

		// Recuperation du contenu du lien pour le mettre dans une variable $link_content 
		$link_content = file_get_contents($link_all); 

		// convert json string to array
		$contributions = json_decode($link_content, true);

		// Vérification de l'existence des paramètres "query" & "users"
		if (isset($contributions["query"]["users"])) {
				
			foreach ($contributions["query"]["users"] as $content) {

				// Affichage du nombre de contributions de l'utilisateur
				echo "\n Vous avez ".$content["editcount"]." contribution(s) en  ".$project_wiki_name[$link_wiki]."\n\n";

			}	

		}

	}

?>