window.onload = init;

function init() {
    document.getElementById('createGradient').addEventListener('click', () => {
        createGradient();
    });

    /*Niveau 3*/
    document.getElementById('linear').addEventListener('change', () => {
        displayDegre();
    });
    document.getElementById('radial').addEventListener('change', () => {
        displayDegre();
    });
    /**********/
}


function createGradient() {
    /*Niveau 2 */
    let typeGradient = "";
    let radios = document.querySelectorAll('input[name="typeGradient"]');
    for (let i = 0; i< radios.length; i++) {
        if (radios[i].checked) {
            typeGradient = radios[i].value;
        }
    }
    /**********/

    let color1 = document.getElementById('color1').value;

    let color2 = document.getElementById('color2').value;

    let degre = document.getElementById('angle').value;

    let zoneDegrade = document.getElementById('gradient');

    /*Niveau 2 */
    /* Pour le niveau 1, nous nous arrêtons à :
    let value = "linear-gradient(" + degre + "deg, " + color1 + ", " + color2 + ")";
    */
    let value = typeGradient === 'linear' ? typeGradient + "-gradient(" + degre + "deg, " + color1 + ", " + color2 + ")" : typeGradient + "-gradient(" + color1 + ", " + color2 + ")";
    /**********/

    zoneDegrade.style.background = value;

    document.getElementById('codeCSS').innerText = value + ";";
}


function displayDegre() {
    /*Niveau 3*/
    let inputAngle = document.getElementById('inputAngle');
    if (document.querySelector('#linear').checked === true) {
        inputAngle.style.display = "block";
    } else {
        inputAngle.style.display = "none";
    }
    /**********/
}