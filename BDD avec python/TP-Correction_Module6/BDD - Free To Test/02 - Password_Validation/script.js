window.onload = init;

var visible = false;
var conformiteMdp = 0;
var pointMinuscule = 0;
var pointMajuscule = 0;
var pointChiffre = 0;
var pointNbCaracteres = 0;

/**
 * fonction d'initialisation
 * Abonnements des events
 */
function init() {
    document.getElementById("btn-visibilite-password").addEventListener("click", () => {
        visibilite();
    });
    document.getElementById('mdp').addEventListener('input', () => {
        controleMotDePasse();
    })
}


/**
 * Fonction gérant la visibilité du mot de passe
 */
function visibilite() {
    let oeil = document.getElementById("oeil");
    if (!visible) {
        visible = true;
        oeil.setAttribute('src', "images/eye-open.png");
        oeil.setAttribute('alt', "Icône oeil ouvert");
        document.getElementById("mdp").setAttribute('type', 'text');
    } else {
        visible = false;
        oeil.setAttribute('src', "images/eye-close.png");
        oeil.setAttribute('alt', "Icône oeil fermé");
        document.getElementById("mdp").setAttribute('type', 'password');
    }
}


/**
 * Fonction vérifiant que chaque consigne est respectée et gérant l'activation du bouton valider
 */
function validation() {
    conformiteMdp = pointMinuscule + pointMajuscule + pointChiffre + pointNbCaracteres;
    console.log(conformiteMdp);
    if (conformiteMdp == 4) {
        document.getElementById("valider").disabled = false;
    } else {
        document.getElementById("valider").disabled = true;
    }
}


/**
 * Fonction centrale du contrôle du mot de passe
 */
function controleMotDePasse() {
    let mdp = document.getElementById("mdp").value;
   
    verifMinuscule(mdp);

    verifMajuscule(mdp);

    verifChiffre(mdp);

    verifNbCaracteres(mdp);

    validation();

}


function verifMinuscule(mdp) {
    let presenceMinuscule = false;

    for (let i = 0; i < mdp.length; i++) {
        if (mdp.charCodeAt(i) >= 97 && mdp.charCodeAt(i) <= 122) {
            presenceMinuscule = true;
        } 
    }

    if (presenceMinuscule) {
        colorTextGreen('minuscule');
        pointMinuscule = 1;
    } else {
        colorTextRed('minuscule');
        pointMinuscule = 0;
    }

}

function verifMajuscule(mdp) {
    let presenceMajuscule = false;
    

    for (let i = 0; i < mdp.length; i++) {
        if (mdp.charCodeAt(i) >= 65 && mdp.charCodeAt(i) <= 90) {
            presenceMajuscule = true;
        } 
    }

    if (presenceMajuscule) {
        colorTextGreen('majuscule');
        pointMajuscule = 1;
    } else {
        colorTextRed('majuscule');
        pointMajuscule = 0;
    }

}

function verifChiffre(mdp) {
    let presenceChiffre = false;

    for (let i = 0; i < mdp.length; i++) {
        if (mdp.charCodeAt(i) >= 48 && mdp.charCodeAt(i) <= 57) {
            presenceChiffre = true;
        } 
    }

    if (presenceChiffre) {
        colorTextGreen('chiffre');
        pointChiffre = 1;
    } else {
        colorTextRed('chiffre');
        pointChiffre = 0;
    }
   
}

function verifNbCaracteres(mdp) {
    let nbCaract = false;

    if (mdp.length == 0) {
        colorTextRed('minuscule');
        colorTextRed('majuscule');
        colorTextRed('chiffre');
        colorTextRed('nbCaracteres');
    }

    if (mdp.length >= 8) {
        colorTextGreen('nbCaracteres');
        nbCaract = true;
    } else {
        colorTextRed('nbCaracteres');
        nbCaract = false;
    }

    if (nbCaract) {
        pointNbCaracteres = 1;
    } else {
        pointNbCaracteres = 0;
    }

}

function colorTextRed(id) {
    document.getElementById(id).style.color = "red";
}

function colorTextGreen(id) {
    document.getElementById(id).style.color = "green";
}
