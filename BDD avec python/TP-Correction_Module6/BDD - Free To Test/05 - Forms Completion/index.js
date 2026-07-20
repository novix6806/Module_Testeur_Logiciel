window.onload = init;

function init() {
    var staticModaleCookie = new bootstrap.Modal(document.getElementById("staticModaleCookie"));
    staticModaleCookie.show()
}



var toastTrigger = document.getElementById('connexionToastBtn')
var toastLiveExample = document.getElementById('connexionToast')
if (toastTrigger) {
    toastTrigger.addEventListener('click', function() {
        var toast = new bootstrap.Toast(toastLiveExample)
        toast.show()
    })
}