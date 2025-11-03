# Estructura de datos: Cola (Queue)
# Versión compatible con AWS Lambda

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

# Función principal requerida por AWS Lambda
def lambda_handler(event, context):
    q = make_queue()

    # Cargar algunos valores de ejemplo o desde el evento
    valores = event.get("valores", ["A", "B", "C"])
    for v in valores:
        q["enqueue"](v)

    # Simular operación de dequeue (eliminar primero)
    eliminado = q["dequeue"]()

    # Retornar resultado como JSON
    return {
        "cola_actual": q["show"](),
        "elemento_eliminado": eliminado,
        "tamaño": q["size"]()
    }
