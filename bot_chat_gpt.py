from os import getenv
import chatGPT
import telebot
import json

chave_bot = getenv(key="CHAVE_BOT")
bot = telebot.TeleBot(chave_bot)
chatId = ''
credit_dict = {}
gpt_users_id = {}

def verificar_arquivo_credito():
    """Vai retornar o dict"""
    try:
        with open('gpt_creditos.txt', 'r') as file:
            credit_dict = file.read()
            a = json.loads(credit_dict)

    except Exception as e:
        with open('gpt_creditos.txt', 'w') as file:
            dict = file.read() #estudar essa subrescrição

def verificar_arquivo_usuario():
    """Vai retornar o dict"""
    try:
        with open('gpt_users_id.txt', 'r') as file:
            gpt_users_id = file.read()
            a = json.loads(gpt_users_id)

    except Exception as e:
        with open('gpt_users_id.txt', 'w') as file:
            dict = file.read() #estudar essa subrescrição

def adicionar_usuario(id, usuario):
    try:
        with open('gpt_creditos.txt', 'r') as file:
            credit_dict = file.read()
            dict = json.loads(credit_dict)
            dict['id'] = 50
            return
    except:
        with open('gpt_creditos.txt', 'w') as file:
            credit_dict = file.read()
            dict = json.loads(credit_dict)
            dict['id'] = 50
            return

def verificar_creditos(id):
    """retorna o credito do usuario"""
    with open('gpt_users_id.txt', 'r') as file:
        gpt_users_id = file.read()
        dict_user = json.loads(gpt_users_id)
        return dict_user[f'{id}']


def rodar():
    while True:
        try:
            @bot.message_handler(commands=['start'])
            def start(mensagem):
                bot.send_message(mensagem.chat.id, 'Escreva sua pergunta usando uma / no começo\n'
                                                   '/ Por que a terra gira ?')

            @bot.message_handler()
            def iniciar(mensagem):
                global chatId
                if not mensagem:
                    bot.send_message(chatId, 'Tente algo como\n'
                                                       'EX: / Por que a terra gira ?')
                    return
                chatId = mensagem.chat.id
                id_usuario = mensagem.from_user.id
                nome_usuario = mensagem.from_user.first_name
                try:
                    creditos_user = verificar_creditos(id_usuario)
                    creditos_user = creditos_user - 1
                except:
                    adicionar_usuario(id_usuario, nome_usuario)
                verificar_creditos(id_usuario)
                mensagem = str(mensagem.text)
                mensagem = mensagem.split('/')[1]
                letras = len(mensagem)
                if letras <= 10:
                    bot.send_message(chatId, 'Não foi considerado uma pergunta, tente algo como\n'
                                             'EX: / Por que a terra gira ?')
                    return
                resposta = chatGPT.chat(mensagem)
                bot.send_message(chatId, resposta)
            bot.polling()
        except Exception as e:
            global chatId
            print(f'Deu problema, reeiniciando ...\nERRO: {e}')
            bot.send_message(chatId, 'Escreva sua pergunta usando uma / no começo\n'
                                                   'EX: / Por que a terra gira ?')
        continue



