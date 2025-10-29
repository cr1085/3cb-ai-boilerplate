# Proyecto: Boilerplate de Agente de IA

¡Construye tu primer agente de IA en menos de 5 minutos!

Esta es una plantilla de código lista para usar (`boilerplate`) diseñada para eliminar la fricción inicial al crear aplicaciones de IA. Está pensada para ser simple, fácil de entender y fácilmente extensible.

---

### ¿Por Qué Usar Esta Plantilla?

El 90% del tiempo al iniciar un proyecto de IA se pierde en:
* Configurar el entorno.
* Organizar los archivos (especialmente los prompts).
* Manejar correctamente las claves de API.
* Escribir el código repetitivo para conectarse al modelo.

Esta plantilla resuelve todo eso por ti.

### Características

* **Estructura Limpia:** Organización lógica de carpetas (`/app`, `/prompts`).
* **Gestión de APIs:** Carga segura de claves API usando `.env`.
* **Prompts Externos:** Separa tu lógica (`.py`) de tus instrucciones (`.txt`).
* **Mínimas Dependencias:** Usa solo `openai` y `python-dotenv` para empezar.
* **Listo para Extender:** Incluye un archivo `herramientas.py` vacío listo para que añadas tus propias funciones (búsqueda web, cálculos, etc.).

---

### Guía de Inicio Rápido (5 Minutos)

Sigue estos 4 pasos para tener tu agente funcionando.

#### Paso 1: Clona el Repositorio

```bash
git clone 
cd proyecto-agente
```

#### Paso 2: Configura tu Entorno

Te recomiendo usar un entorno virtual:

```bash
# Crea el entorno
python -m venv venv

# Actívalo (en Mac/Linux)
source venv/bin/activate
# (en Windows)
.\venv\Scripts\activate
```

Ahora, instala las dependencias:

```bash
pip install -r requirements.txt
```

#### Paso 3: Añade tu Clave de API

1.  Renombra el archivo `.env.example` a `.env`.
2.  Abre el nuevo archivo `.env` y pega tu clave de OpenAI:

    ```ini
    OPENAI_API_KEY="sk-TU_CLAVE_SECRETA_AQUI"
    ```

#### Paso 4: ¡Ejecuta el Agente!

Todo está listo. Simplemente corre el script principal:

```bash
python app/main.py
```

**¡Felicidades!** Acabas de ejecutar tu primer agente.

---

### ¿Cómo Modificarlo?

1.  **Cambia la Tarea:** Edita el archivo `prompts/tareas.txt` para darle una nueva misión a tu agente.
2.  **Mejora el Cerebro:** Edita `prompts/sistema.txt` para cambiar la personalidad, instrucciones y reglas del agente.
3.  **Añade Herramientas:** Ve a `app/herramientas.py` y define nuevas funciones. Luego, impórtalas en `app/agente.py` y enséñale al agente cómo usarlas (editando el `prompt_sistema.txt`).

### Sobre el Autor y el Siguiente Nivel

Hola, soy Cristian Camilo Cuadrado Beltran. Creé esta plantilla por una razón muy simple: estaba harto de que la configuración matara la creatividad.

Cada vez que tenía una nueva idea para un agente de IA, perdía horas configurando el mismo entorno, organizando archivos y conectando APIs. Me di cuenta de que este "trabajo pesado" inicial es el principal enemigo del momentum.

Mi promesa con esta plantilla es devolverte ese tiempo. Es la vía rápida para que puedas saltar directamente a lo divertido: diseñar el cerebro de tu agente y experimentar. Úsala para que nunca más dejes un gran proyecto a medias por culpa de un setup aburrido.

**¿Te gustó esta plantilla?** Esto es solo el 1% de lo que implica construir agentes robustos y productivos.

Si quieres aprender a:
* Crear bucles de pensamiento-acción (ReAct).
* Darle herramientas complejas (como búsqueda en Google o acceso a APIs).
* Manejar la memoria a corto y largo plazo.
* Evaluar el rendimiento de tu agente.

**Estoy preparando mi curso completo de IA: INTELIGENCIA ARTIFICIAL PARA TODOS.**

➡️ **[(https://tally.so/r/nWG1VL)]** Únete a la lista de espera para ser el primero en saberlo y obtener un descuento de lanzamiento exclusivo.