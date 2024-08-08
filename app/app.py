from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/proyecto'
db = SQLAlchemy(app)

class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False)



@app.route('/')
def evento():
    return render_template('evento.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/aniadir_contacto', methods=['POST'])
def aniadir_contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']

        nuevo_contacto = Contacto(nombre=nombre, telefono=telefono, email=email)
        db.session.add(nuevo_contacto)
        db.session.commit()
        return render_template('confirmacion.html')
   

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/contactos', methods=['GET', 'POST'])
def contactos():
    contactos = Contacto.query.all()
    return render_template('contactos.html', contactos=contactos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST' and 'usuario' in request.form and 'contra' in request.form:
        usuario = request.form['usuario']
        contra = request.form['contra']
        
        if usuario == 'Fullstack' and contra == 'Oeste':
            # Si las credenciales son correctas, redirigir a la página de contactos
            return redirect(url_for('contactos'))
        else:
            if usuario == '' and contra == '':
                # Si las credenciales son correctas, redirigir a la página de contactos
                #return redirect(url_for('admin'))
                error = 'Ingrese Usuario y contraseña'
            else:
                # Si las credenciales son incorrectas, mostrar un mensaje de error
                error = 'Usuario o contraseña incorrectos.'
                #return render_template('admin.html', error=error)

    # Si el método es GET o las credenciales son incorrectas, renderear el formulario de inicio de sesión
    return render_template('admin.html', error=error)

    
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST' and 'usuario' in request.form and 'contra' in request.form:
#         usuario = request.form['usuario']
#         contra = request.form['contra']
        
#         if usuario == 'Fullstack' and contra == 'Oeste':
#             # Si las credenciales son correctas, redirigir a la página de contactos
#             return render_template('contactos.html')
#         else:
#             # Si las credenciales son incorrectas, mostrar un mensaje de error
#             mensaje_error = 'Usuario o contraseña incorrectos.'

#      # Si el método es GET o las credenciales son incorrectas, renderear el formulario de inicio de sesión
#     return render_template('admin.html', mensaje_error=mensaje_error)



@app.route('/editar_contacto/<int:id>', methods=['GET', 'POST'])
def editar_contacto(id):
    contacto = Contacto.query.get(id)

    if request.method == 'POST':
        # Aquí manejas la actualización del contacto según los datos del formulario
        nombre_actualizado = request.form['nombre']
        telefono_actualizado = request.form['telefono']
        email_actualizado = request.form['email']

        # Actualizar los atributos del contacto
        contacto.nombre = nombre_actualizado
        contacto.telefono = telefono_actualizado
        contacto.email = email_actualizado

        db.session.commit()
        #return f'Contacto con ID {id} actualizado correctamente.'
        return render_template('exito_editar.html')

    # Si la solicitud es GET, renderizar el formulario con los datos del contacto
    return render_template('editar_contacto.html', contacto=contacto)

@app.route('/seleccionar_contacto/<int:id>', methods=['GET', 'POST'])
def seleccionar_contacto(id):
    contacto = Contacto.query.get(id)

    if request.method == 'POST':
        # Aquí manejas la actualización del contacto según los datos del formulario
        nombre_actualizado = request.form['nombre']
        telefono_actualizado = request.form['telefono']
        email_actualizado = request.form['email']
        
    return render_template('seleccionar_contacto.html', contacto=contacto)

@app.route('/borrar_contacto/<int:id>')
def borrar_contacto(id):
    contacto = Contacto.query.get(id)

    if contacto:
        db.session.delete(contacto)
        db.session.commit()
        return render_template('exito_borrar.html')
    else:
        return render_template('no_existe_contacto.html')
    

# @app.route('/borrar_contacto/<int:id>')
# def borrar_contacto(id):
#     contacto = Contacto.query.get(id)
#     db.session.delete(contacto)
#     db.session.commit()
#     return f'Contacto con ID {id} borrado correctamente.'


if __name__ == "__main__":
    # Crear las tablas antes de ejecutar la aplicación
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5000)
