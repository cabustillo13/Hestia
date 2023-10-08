import gradio as gr
from tools import ask_chatbot

def check_inputs(question):
    if(question !="" ):
        respuesta = ask_chatbot(question)
        return respuesta
    else:
        return "!Ups, hubo un Error! - Nos hacen falta información para poder ayudarte", None


# Descripción del Header
description = """
<center><h1><b>Hest.ia 👑 </b></h1>
<center><h2><b>Acompañante durante vuelos espaciales 🗣️💡 </b></h2>
Simplemente carga respuestas a ciertas preguntas clave y obtén conclusiones detalladas sobre tu viaje.
</center>
"""

# Descripción del Footer
article = """
<br>
<b>¿Por qué elegirnos?</b>
<br><b>Hest.ia  👑</b>, tu aliado inteligente para mejorar tus habilidades comunicativas 💯. <br>Hacemos análisis de tus respuestas ante preguntas 🔍 y te damos feedback para mejorar tu viaje espacial 🙌.
<br>Descubre el poder de la inteligencia artificial aplicada a potenciar los viajes espaciales.🤖💡
"""


# Inputs
question = gr.Textbox(label="Contame, en qué te puedo ayudar ❓")

# Outputs
resultado = gr.Textbox(label="Respuesta 💡")

gui = gr.Interface(
    fn=check_inputs, 
    inputs=[question], 
    outputs=[resultado],
    description = description,
    article = article,
    theme=gr.themes.Soft()
)

gui.launch()