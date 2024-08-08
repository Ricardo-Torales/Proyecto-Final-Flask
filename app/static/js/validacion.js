function validarFormulario() {
    var nombre = document.getElementById('nombre');
    var telefono = document.getElementById('telefono');
    var email = document.getElementById('email');

    // Reiniciar estilos
    nombre.classList.remove('campo-invalido');
    telefono.classList.remove('campo-invalido');
    email.classList.remove('campo-invalido');

    // Validar que los campos no estén vacíos
    if (nombre.value.trim() === '') {
        alert('Por favor, ingrese su nombre completo.');
        nombre.classList.add('campo-invalido');
        return false;
    }

    if (telefono.value.trim() === '') {
        alert('Por favor, ingrese su número de teléfono.');
        telefono.classList.add('campo-invalido');
        return false;
    }

    if (email.value.trim() === '') {
        alert('Por favor, ingrese su dirección de correo electrónico.');
        email.classList.add('campo-invalido');
        return false;
    }

    // Si todas las validaciones pasan, el formulario se envía
    return true;
}