from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import sqlite3

app = Flask(__name__)
bcrypt = Bcrypt(app)

def crear_tabla():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contraseña TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

crear_tabla()

# Creo un endpoint /registro

@app.route('/registro', methods=['POST'])
def registrar():
    data = request.get_json()
    usuario = data['usuario']
    contraseña = bcrypt.generate_password_hash(data['contraseña']).decode('utf-8')

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)', (usuario, contraseña))
        conn.commit()
        return jsonify({'mensaje': 'Usuario registrado exitosamente'})
    except sqlite3.IntegrityError:
        return jsonify({'error': 'El usuario ya existe'}), 400
    finally:
        conn.close()

# Creo un endpoint /login

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data['usuario']
    contraseña = data['contraseña']

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT contraseña FROM usuarios WHERE usuario = ?', (usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and bcrypt.check_password_hash(resultado[0], contraseña):
        return jsonify({'mensaje': f'Bienvenido {usuario}'})
    else:
        return jsonify({'error': 'Credenciales inválidas'}), 401

# Creo un endpoint /tareas

@app.route('/tareas', methods=['GET'])
def tareas():
    return '''
    <html>
        <head><title>Bienvenido</title></head>
        <body>
            <h1>¡Has iniciado sesión exitosamente!</h1>
        </body>
    </html>
    '''

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
