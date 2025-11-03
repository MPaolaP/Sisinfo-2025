# Estructura de datos: Cola (Queue)
# Versión para ejecución local y compatible con AWS Lambda

def make_queue():
    queue = []

    return {
        "enqueue": lambda x: queue.append(x),
        "dequeue": lambda: queue.pop(0) if queue else None,
        "peek": lambda: queue[0] if queue else None,
        "is_empty": lambda: len(queue) == 0,
        "size": lambda: len(queue),
        "show": lambda: queue.copy()
    }

def lambda_handler(event, context=None):
    """Simula la función principal de AWS Lambda."""
    q = make_queue()

    valores = event.get("valores", ["A", "B", "C"])
    for v in valores:
        q["enqueue"](v)

    eliminado = q["dequeue"]()

    return {
        "cola_actual": q["show"](),
        "elemento_eliminado": eliminado,
        "tamaño": q["size"]()
    }

# Bloque principal para pruebas locales
if __name__ == "__main__":
    evento_prueba = {"valores": ["X", "Y", "Z"]}
    resultado = lambda_handler(evento_prueba)
    print("Resultado:", resultado)
