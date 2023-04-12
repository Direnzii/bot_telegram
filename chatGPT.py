from os import getenv
import openai
import json


def chat(mensagem: str):
    openai.api_key = getenv(key='OPENAI_API_KEY')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=mensagem,
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    text_response = json.loads(str(response)).get('choices')
    text_response = text_response[0]

    return text_response['text']
