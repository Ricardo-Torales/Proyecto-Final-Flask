document.getElementById('loginForm').addEventListener('submit', function (event) {
    // Limpiar mensajes de error anteriores
    document.getElementById('usuarioError').textContent = '';
    document.getElementById('contraError').textContent = '';

    // Validar usuario
    var usuario = document.getElementById('usuario').value;
    if (usuario.trim() === '') {
        document.getElementById('usuarioError').textContent = 'El campo Usuario es obligatorio.';
        event.preventDefault(); // Evitar el envío del formulario si hay errores
    }

    // Validar contraseña
    var contra = document.getElementById('contra').value;
    if (contra.trim() === '') {
        document.getElementById('contraError').textContent = 'El campo Contraseña es obligatorio.';
        event.preventDefault(); // Evitar el envío del formulario si hay errores
    }
});