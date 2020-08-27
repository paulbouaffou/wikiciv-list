// Author: Paul Bouaffou
// License: MIT
// Description: Text Javascript


/* -------------- Vérifier les valeurs saisies dans le champ avant sa validation ---------------*/


        function check(){
             var nbr=document.frm.limit.value;
             if (isNaN(nbr)){
                 document.getElementById("msg").innerHTML="Entrez uniquement une valeur numérique !";
                 return false;
             }else if (nbr == "" || nbr == null) {
             	document.getElementById("msg").innerHTML="Veuillez saisir une valeur numérique !";
             	return false;
             }else if (nbr < 0) {
                document.getElementById("msg").innerHTML="Entrez uniquement un nombre positif !";
                return false;
            }else if (nbr != parseInt(nbr)) {
                document.getElementById("msg").innerHTML="Entrez uniquement un nombre entier !";
                return false;
            }else if (nbr == 0){
                document.getElementById("msg").innerHTML="Entrez uniquement une valeur numérique non nul !";
                return false;               
            }else{
                 return true;
             }
         }
