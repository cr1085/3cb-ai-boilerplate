import os 
from openai import OpenAI

class Agente:
    def __init__(self, cliente_api, modelo, api_key):
        self.modelo=modelo
        self.cliente= OpenAI(api_key=api_key)
        self.prompt_sistema= self._cargar_prompt_sistema()
        self.historial=[
            {"role": "system", "content": self.prompt_sistema}
        ] 


    def _cargar_prompt_sistema(self):
        ruta_prompt='prompts/sistema.txt'
        if not os.path.exists(ruta_prompt):
            print(f'El archivo de prompt del sistema no se encontró en la ruta: {ruta_prompt}')
            return 'Eres un agente de IA útil.'
        
        with open(ruta_prompt, 'r', encoding='utf-8') as f:
            return f.read().strip()
        
    def ejecutar(self,tarea):
        print(f"[Agente]: Pensando en la tarea: {tarea}")
        self.historial.append({"role":"user","content":tarea})

        try:
            respuesta= self.cliente.chat.completions.create(
                model=self.modelo,
                messages=self.historial
            )

            respuesta_texto= respuesta.choices[0].message.content
            self.historial.append({"role":"assistant","content":respuesta_texto})

            return respuesta_texto
        except Exception as e:
            print(f"Erro al llamar a la API:{e}")
            return "Hubo un error al procesar la solicitud del sistema."

            
                
