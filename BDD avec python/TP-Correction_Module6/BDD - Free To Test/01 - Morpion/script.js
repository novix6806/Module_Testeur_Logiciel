var playerturn = true;
var scoreArray = new Array();


/**
 * NIVEAU 1 : Fonction d'initialisation
 */
$(function() {
    for (let i = 0; i < 9; i++) {
        scoreArray[i] = 0;
        let id = "#" + i;
        $(id).click(function(e) {
            imageReplace(e)
        });
    }
});

/**
 *  NIVEAU 2 : Méthode de remplacement de l'image
 * @param {*} e event
 */
function imageReplace(e) {
    if (playerturn) {
		//Met la croix dans la zone cliquée.
        $(e.target).attr("src", "assets/images/croix.png");
		//Affiche que c'est au tour du joueur 2
        $("joueur").text("2");
		//Met à jour le tableau de score
        scoreArray[e.currentTarget.id] = 1;
    } else {
		//On affiche l'image cercle dans la zone cliquée.
        $(e.target).attr("src", "assets/images/rond.png");
        $("joueur").text("1");
        scoreArray[e.currentTarget.id] = 10;
    }
	//Supprime l'évènement
    $(e.currentTarget).off("click");
	//Met à jour la variable pour savoir qui joue.
    playerturn = !playerturn;
	//Vérifie si quelqu'un a gagné
    verification();
}

/**
 * NIVEAU 3 : Méthode de vérification de victoire
 */
function verification() {
    let scoreL1 = scoreArray[0] + scoreArray[1] + scoreArray[2];
    let scoreL2 = scoreArray[3] + scoreArray[4] + scoreArray[5];
    let scoreL3 = scoreArray[6] + scoreArray[7] + scoreArray[8];
    let scoreC1 = scoreArray[0] + scoreArray[3] + scoreArray[6];
    let scoreC2 = scoreArray[1] + scoreArray[4] + scoreArray[7];
    let scoreC3 = scoreArray[2] + scoreArray[5] + scoreArray[8];
    let scoreD1 = scoreArray[0] + scoreArray[4] + scoreArray[8];
    let scoreD2 = scoreArray[2] + scoreArray[4] + scoreArray[6];

    // Victoire joueur 1
    if ( scoreL1 === 3 || scoreL2 === 3 || scoreL3 === 3 || scoreC1 === 3 || scoreC2 === 3 || scoreC3 === 3 || scoreD1 === 3 || scoreD2 === 3) {
        $("h3").text('Joueur 1 gagne !');
        stopGame();
    }

     // Victoire joueur 2
    if ( scoreL1 === 30 || scoreL2 === 30 || scoreL3 === 30 || scoreC1 === 30 || scoreC2 === 30 || scoreC3 === 30 || scoreD1 === 30 || scoreD2 === 30) {
        $("h3").text('Joueur 2 gagne !');
        stopGame();
    }

    // Egalité
    if (scoreArray[0] + scoreArray[1] + scoreArray[2] + scoreArray[3] + scoreArray[4] + scoreArray[5] +scoreArray[6] + scoreArray[7] + scoreArray[8] === 45) {
        $("h3").text('Egalité !');
        stopGame();
    }
    
}

// Fin de jeu
function stopGame() {
    for (let i = 0; i < 9; i++) {
        let id = "#" + i;
        $(id).off("click");
    }
}