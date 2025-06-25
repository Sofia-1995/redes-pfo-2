# Gestor de Tareas con Flask y SQLite

## Requisitos

- Python 3
- Flask
- Flask-Bcrypt

## Cómo ejecutar

1. Intalar dependencias:

   ```bash
   pip intall flask flask-bcrypt
   ```

2. Ejecutar el servidor:

   ```bash
   python servidor.py
   ```

3. Endpoints:
   - POST /registro
   - POST /login
   - GET /tareas

## Comandos de ejemplo

### Registro

```bash
curl -X POST http://127.0.0.1:5000/registro \
 -H "Content-Type: application/json" \
 -d '{"usuario": "sofi", "contraseña": "1234"}'
```

### Login

```bash
curl -X POST http://127.0.0.1:5000/login \
 -H "Content-Type: application/json" \
 -d '{"usuario": "sofi", "contraseña": "1234"}'
```
