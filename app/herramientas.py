# --- app/herramientas.py ---

"""
Este archivo contendrá todas las "herramientas" que tu agente puede decidir usar.
Una herramienta es simplemente una función de Python que realiza una tarea específica.

En el curso avanzado, aprenderemos a construir herramientas de verdad:
- Búsqueda en Google (Web Search)
- Conexión a bases de datos (SQL)
- entre otras muy importantes
- etc...
"""

def obtener_clima_actual(ciudad: str) -> str:
    """
    Ejemplo de una función de herramienta simple (simulada).
    
    En un proyecto real, esta función haría una llamada a una API
    de clima como OpenWeatherMap.
    """
    print(f"[Herramienta]: Se ha llamado a obtener_clima_actual con la ciudad: {ciudad}")
    
    # Simulación de respuesta de API
    if ciudad.lower() == "bogotá":
        return "El clima en Bogotá es frío, con 15°C y lloviznas."
    elif ciudad.lower() == "madrid":
        return "El clima en Madrid es soleado, con 28°C."
    else:
        return f"No tengo información del clima para {ciudad}."

def calculadora_simple(operacion_matematica: str) -> str:
    """
    Ejemplo de una herramienta que usa eval() para operaciones simples.
    ¡CUIDADO! Usar eval() con input del usuario no es seguro en producción,
    pero sirve como un buen ejemplo de una herramienta "funcional".
    """
    print(f"[Herramienta]: Se ha llamado a calculadora_simple con la operación: {operacion_matematica}")
    try:
        # Por seguridad, solo permitimos caracteres numéricos y operadores básicos
        allowed_chars = "0123456789+-*/.() "
        if not all(char in allowed_chars for char in operacion_matematica):
            return "Error: Operación no válida. Solo se permiten números y operadores básicos."
            
        resultado = eval(operacion_matematica)
        return f"El resultado de '{operacion_matematica}' es: {resultado}"
    except Exception as e:
        return f"Error al calcular: {e}"

# --- Puedes añadir más funciones de ejemplo aquí ---