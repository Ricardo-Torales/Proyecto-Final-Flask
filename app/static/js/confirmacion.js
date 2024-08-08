// confirmacion.js
document.addEventListener("DOMContentLoaded", function() {
    var formularioSection = document.getElementById("contenedor_form");
    var mensajeExito = document.getElementById("mensajeExito");

    document.querySelector('submit').addEventListener('submit', function(event) {
        event.preventDefault();
        formularioSection.style.display = 'none';
        mensajeExito.style.display = 'block';
    });
});