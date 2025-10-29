from agente import Agente
from config import OPENAI_API_KEY


def leer_promtp_tarea():
    try:
        with open('prompts/tareas.txt', 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        return "Tarea por defecto: ¿Quién ghano el mundial de fútbol del 2022?"

def main():
    print("Inicializando el agente...")

    cliente_api='openai'
    modelo='gpt-4o-mini'
    agente= Agente(cliente_api, modelo, OPENAI_API_KEY)
    tarea= leer_promtp_tarea() 
    resultado=agente.ejecutar(tarea)
    print(f"resultados:{resultado}")

if __name__ == "__main__":
    main()          