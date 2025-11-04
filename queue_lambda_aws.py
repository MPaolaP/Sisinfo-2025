"""
AWS Lambda Example: Simple REST API
------------------------------------

Este ejemplo muestra cómo construir una función Lambda en Python que se comporta
como una pequeña API con rutas GET y POST usando API Gateway.

✅ Funcionalidades:
- Responde a solicitudes GET con un saludo personalizado.
- Acepta solicitudes POST para registrar un usuario (simulado en memoria).
- Devuelve respuestas con formato JSON y códigos HTTP adecuados.

acceder con URLs tipo:
   - GET  → https://.../default/apiLambdaExample?name=Maria
   - POST → https://.../default/apiLambdaExample  (con cuerpo JSON)

📦 Ejemplo de cuerpo POST:
{
  "username": "maria123",
  "email": "maria@example.com"
}
"""

import json

# Simulamos una "base de datos" en memoria
USERS = []


def lambda_handler(event, context):
    """
    Manejador principal de la función Lambda.
    Interpreta el método HTTP y delega la acción correspondiente.
    """

    # Extraer el método HTTP y ruta del evento
    http_method = event.get("httpMethod", "GET")
    path = event.get("path", "/")

    # Determinar la acción según el método
    if http_method == "GET":
        return handle_get(event)
    elif http_method == "POST":
        return handle_post(event)
    else:
        return response(405, {"error": f"Method {http_method} not allowed"})


def handle_get(event):
    """Maneja solicitudes GET (por ejemplo, saludo personalizado)."""
    name = event.get("queryStringParameters", {}).get("name", "Visitor")
    message = f"Hello, {name}! Welcome to our AWS Lambda API."
    return response(200, {"message": message})


def handle_post(event):
    """Maneja solicitudes POST (registrar usuario)."""

    try:
        body = json.loads(event.get("body", "{}"))
    except json.JSONDecodeError:
        return response(400, {"error": "Invalid JSON format"})

    username = body.get("username")
    email = body.get("email")

    if not username or not email:
        return response(400, {"error": "Missing 'username' or 'email'"})

    # Simulamos guardar usuario
    USERS.append({"username": username, "email": email})

    return response(201, {
        "message": "User registered successfully",
        "user": {"username": username, "email": email},
        "total_users": len(USERS)
    })


def response(status_code, body_dict):
    """Crea una respuesta estándar con formato JSON."""
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body_dict)
    }