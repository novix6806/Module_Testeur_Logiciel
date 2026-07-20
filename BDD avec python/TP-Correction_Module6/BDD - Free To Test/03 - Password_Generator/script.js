window.onload = init;

var password = "";

var nbCar = 1;
var min = false;
var maj = false;
var num = false;
var car = false;

var valid = true;
var securityLevel = 0;

/**
 * Fonction d'initialisation. Mise en place du canvas et abonnement aux events click pour les deux boutons.
 */
function init() {
    step0();
    document.getElementById('generation').addEventListener('click', function() {
        main();
    });
    document.getElementById('copy').addEventListener('click', function() {
        copyCode();
    })
}

/**
 * Fonction principale du programme
 * Appels de plusieurs fonctions :
 * - checkElements
 * - generation
 * - display
 */
function main() {
    password = "";
    checkElements();
    generation();
    display(valid);
}

/**
 * Fonction en charge de la vérification des critères retenus pour la génération du mot de passe
 * Appel de plusieurs fonctions :
 * - readNb
 * - readCheckBox
 * Détermine la validité. Si aucun critère n'est retenu alors la demande est invalide. 
 */
function checkElements() {
    readNb();
    readCheckBox("min");
    readCheckBox("maj");
    readCheckBox("num");
    readCheckBox("car");
    if (!min && !maj && !num && !car) {
        valid = false;
    } else {
        valid = true;
        checkSecurityLevel();
    }
}

/**
 * Fonction récupérant la valeur pour la longueur du mot de passe souhaité
 */
function readNb() {
    nbCar = document.getElementById('nb').value;
}

/**
 * Fonction de lecture des checkbox
 * @param {*} id Correspond à l'id de la checkbox concernée
 */
function readCheckBox(id) {
    let state = document.getElementById(id).checked;
    switch (id) {
        case 'min': min = state;
        break;
        case 'maj': maj = state;
        break;
        case 'num': num = state;
        break;
        case 'car': car = state;
        break;
    }
}

/**
 * Fonction de génération du mot de passe
 */
function generation() {
    let possibility = "";

    if (min) {
        for (let i = 97; i < 123; i++) {
            possibility += String.fromCharCode(i);
        }
    }

    if (maj) {
        for (let i = 65; i < 91; i++) {
            possibility += String.fromCharCode(i);
        }
    }

    if (num) {
        for (let i = 48; i < 58; i++) {
            possibility += String.fromCharCode(i);
        }
    }

    if (car) {
        for (let i = 33; i < 48; i++) {
            possibility += String.fromCharCode(i);
        }
    }

    for (let i = 0; i < nbCar; i++) {
        let index = Math.floor(Math.random() * possibility.length);
        password += possibility.charAt(index); 
    }
}

/**
 * Fonction qui étudie le niveau de sécurité du mot de passe.
 * Un score est calculé sur la base du nombre de combinaisons possibles en fonction des critères retenus.
 * Plus le nombre est élevé et moins le risque d'une attaque par force brute est possible.
 * 4 paliers ont été retenus (plus ou moins arbitrairement) :
 * - 8503056 combinaisons qui correspond à un mot de passe de 4 caractères et 2 critères
 * - 62523502209 combinaisons qui correspond à un mot de passe de 6 caractères et 3 critères
 * - 1235736291547681 combinaisons qui correspond à un mot de passe de 8 caractères et 4 critères
 * - 7326680472586201000  combinaisons qui correspond à un mot de passe de 10 caractères et 4 critères
 */
function checkSecurityLevel() {
    let nb = parseInt(document.getElementById('nb').value);
    let coefMin = 1;
    let coefMaj = 1;
    let coefNum = 1;
    let coefCar = 1;

    let score = 1;

    if (min) {
        coefMin = 26;
    }
    if (maj) {
        coefMaj = 26;
    }
    if (num) {
        coefNum = 10;
    }
    if (car) {
        coefCar = 15;
    }
    
    score = Math.pow(coefMin + coefMaj + coefNum + coefCar, nb);
   
    if (score <= 8503056) { // 4 car + 2 critères
        securityLevel = 1;
    } else if (score <= 62523502209) { // 6 car + 3 critères
        securityLevel = 2;
    } else if (score <= 1235736291547681) { // 8 car + 4 critères
        securityLevel = 3;
    } else if (score <= 7326680472586201000) { // 10 car + 4 critères
        securityLevel = 4;
    } else {
        securityLevel = 5;
    }

}

/**
 * Fonction d'affichage
 * Gère l'affichage du mot de passe et du niveau de sécurité
 * @param {*} val Validité des critères retenus. Déterminé dans la fonction checkElements
 * @returns 
 */
function display(val) {
    if (!val) {
        document.getElementById('mdp').innerText = "Impossible de générer le mot de passe sans critères";
        console.log('test');
        return 0;
    } else {
        document.getElementById('mdp').innerText = password;
    }    

    switch(securityLevel) {
        case 0: step0();
        break;
        case 1: step1();
        break;
        case 2: step2();
        break;
        case 3: step3();
        break;
        case 4: step4();
        break;
        case 5: step5();
        break;
    }
}

/**
 * Fonction gérant la copie du code et l'affiche après lecture du presse-papier
 */
function copyCode() {
    if (password.length != 0) {
        navigator.clipboard.writeText(password);
        navigator.clipboard.readText()
        .then(text => {
            alert("Mot de passe copié :\n" + text);
        })
        .catch(err => {
            console.error('Problème de lecture du presse-papier : ', err);
        });
    } else {
        alert("Aucun mot de passe généré !!!");
    }
    
}

/**
 * Fonction gérant la copie du code et l'affiche directement
 */
function copyCode2() {
    if (password.length != 0) {
        navigator.clipboard.writeText(password);
        alert("Mot de passe copié :\n" + password);
    } else {
        alert("Aucun mot de passe généré !!!");
    }
    
}

