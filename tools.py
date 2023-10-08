import os
from dotenv import load_dotenv
import openai


# Cargar variables de entorno
load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY', '')

# Asignar la API Key
openai.api_key = OPENAI_KEY

def mychatbot(messages):
    # Chatbot que hace consultas "query" a una base de conocimiento "contract_knowledge"

    # Enviar solicitud a la api OpenAI con el modelo "GPT-3.5-turbo"
    res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = messages
    )

    # Del diccionario extraer la informacion correspondiente al id "content"
    conclusion = res['choices'][0]['message']['content']
    
    return conclusion


def ask_chatbot(question):

    prompt = f"""
    Dada la siguiente pregunta realizada por el usuario: {question}.
    Reponde de manera cálida la conversación.
    Agrega datos curiososos sobre el espacio y el turismo espacial. 
    """


    # Dialogo con ChatGPT
    messages = [
        {"role": "system", "content": "Eres un asistente útil experto en psicología y turismo espacial. Acompañarás al usuario durante todo su viaje espacial."},
        {"role": "user", "content": prompt}
    ]

    # Output
    respuesta = mychatbot(messages)

    return respuesta
