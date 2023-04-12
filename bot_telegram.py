from os import getenv
import telebot
import requests
from shodan import Shodan
from randmovie import assistir_filme
import random
from collections import defaultdict

chave_bot = getenv(key="CHAVE_BOT")
shodan_key = getenv(key="CHAVE_SHODAN")
api = Shodan(shodan_key)

bot = telebot.TeleBot(chave_bot)
aleatorio = assistir_filme()
dict_genero = aleatorio.dict_genero

infos = defaultdict(list)

while True:
    try:
        @bot.message_handler(commands=['salvar'])
        def salvar(mensagem):
            try:
                f = open('infos.txt')
                f.close()
                lista_linhas_temp = []
                with open('infos.txt', 'r') as arquivo:
                    for linha in arquivo:
                        lista_linhas_temp.append(linha)
                with open('infos.txt', 'a') as file:
                    saida = ''
                    try:
                        for i in infos:
                            saida += i
                            saida += ':'
                            saida += str(infos[i])
                            saida += '\n'
                            teste = saida in lista_linhas_temp
                            if teste == False:
                                file.write(saida)
                        infos.clear()
                    except Exception as e:
                        pass
            except:
                with open('infos.txt', 'w') as file:
                    saida = ''
                    try:
                        for i in infos:
                            saida += i
                            saida += ':'
                            saida += str(infos[i])
                            saida += '\n'
                        file.write(saida)
                        infos.clear()
                    except Exception as e:
                        pass

        @bot.message_handler(commands=['por_rate_e_genero'])
        def por_rate_e_genero_bot(mensagem, genero=None, rate=None, verificar=True):
            if verificar == True:
                bot.send_message(mensagem.chat.id,
                                 'Para esta opção você precisará digitar o gênero - rate que deseja '
                                 '(sem acento e minusculo (Exceto o Tv do genero cinemaTv))\n'
                                 'Ex: comedia - 5 ou terror - 9\n'
                                 'LEMBRANDO* Essa opção é muito mais especifica, podendo demorar a ser processada'
                                 'até mesmo causando algum erro, aguarde e caso não retorne, tente novamente.\n'
                                 'TEMAS:\nterror\nacao\ncomedia\ndrama\nficcao_cientifica\nfantasia\nfamilia\n'
                                 'aventura\nmisterio\nsuspense\ncrime\ncinemaTv\nromance\n'
                                 'Outras opções serão consideradas inválidas')
                return
            lista_rate_genero = aleatorio.listar_filmes_rate_genero(rate, genero)
            lista_aleatoria = aleatorio.lista_aleatoria(lista_rate_genero)
            saida = aleatorio.rodar(lista_aleatoria)
            saida_sinopse_link = f'{saida[0]}\n{saida[1]}'
            bot.send_message(mensagem.chat.id, saida_sinopse_link)
            imagem = saida[2]
            url_imagem = f'https://image.tmdb.org/t/p/w600_and_h900_bestv2{str(imagem)}'
            url_imagem_http = f'http://image.tmdb.org/t/p/w600_and_h900_bestv2{str(imagem)}'
            try:
                bot.send_photo(mensagem.chat.id, photo=url_imagem)
            except:
                try:
                    send_photo = enviar_photo(url_imagem, mensagem.chat.id)
                    if send_photo == 2:
                        send_photo2 = enviar_photo(url_imagem_http, mensagem.chat.id)
                        if send_photo2 == 2:
                            bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                               'Link do poster do filme: ' + url_imagem)
                    if send_photo == 1:
                        send_photo3 = enviar_photo(url_imagem_http, mensagem.chat.id)
                        if send_photo3 == 1:
                            bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                               'Link do poster do filme: ' + url_imagem)
                except Exception as e:
                    try:
                        bot.send_photo(mensagem.chat.id, photo=url_imagem)
                    except:
                        bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                           'Link do poster do filme: ' + url_imagem)


        @bot.message_handler(commands=['por_genero'])
        def por_genero_bot(mensagem, genero=None, verificar=True):
            if verificar == True:
                bot.send_message(mensagem.chat.id,
                                 'Escolha o gênero que deseja buscar:\n/acao\n/comedia\n/drama\n/ficcao_cientifica'
                                 '\n/fantasia\n/familia\n/aventura\n/misterio\n/suspense\n/crime\n/cinemaTv\n/romance\n'
                                 'Outras opções serão consideradas inválidas')
                return
            lista_genero = aleatorio.listar_filmes_genero(genero=genero)
            lista_aleatoria = aleatorio.lista_aleatoria(lista_genero)
            saida = aleatorio.rodar(lista_aleatoria)
            saida_sinopse_link = f'{saida[0]}\n{saida[1]}'
            bot.send_message(mensagem.chat.id, saida_sinopse_link)
            imagem = saida[2]
            url_imagem = f'https://image.tmdb.org/t/p/w600_and_h900_bestv2{str(imagem)}'
            url_imagem_http = f'http://image.tmdb.org/t/p/w600_and_h900_bestv2{str(imagem)}'
            try:
                bot.send_photo(mensagem.chat.id, photo=url_imagem)
            except:
                try:
                    send_photo = enviar_photo(url_imagem, mensagem.chat.id)
                    if send_photo == 2:
                        send_photo2 = enviar_photo(url_imagem_http, mensagem.chat.id)
                        if send_photo2 == 2:
                            bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                               'Link do poster do filme: ' + url_imagem)
                    if send_photo == 1:
                        send_photo3 = enviar_photo(url_imagem_http, mensagem.chat.id)
                        if send_photo3 == 1:
                            bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                               'Link do poster do filme: ' + url_imagem)
                except Exception as e:
                    try:
                        bot.send_photo(mensagem.chat.id, photo=url_imagem)
                    except:
                        bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                           'Link do poster do filme: ' + url_imagem)


        def enviar_photo(imagem, chat_id):
            try:
                body = {
                    'chat_id': chat_id,
                    'photo': imagem
                }
                r = requests.post('https://api.telegram.org/bot{}/sendPhoto'.format(
                    chave_bot), data=body)
                if r.status_code >= 400:
                    return 1  # ok
                else:
                    return 0  # erro
            except Exception as e:
                return 2  # exception


        @bot.message_handler(commands=['rate_0_a_4'])
        def por_rate_bot_op1(mensagem):
            rate = random.randrange(0, 5)
            lista_filmes = aleatorio.listar_filmes_rate(rate)
            lista_aleatoria = aleatorio.lista_aleatoria(lista_filmes)
            saida = aleatorio.rodar(lista_aleatoria)
            saida_sinopse_link = f'{saida[0]}\n{saida[1]}'
            bot.send_message(mensagem.chat.id, saida_sinopse_link)
            imagem = saida[2]
            url_imagem = f'https://image.tmdb.org/t/p/w600_and_h900_bestv2{str(imagem)}'
            url_imagem_http = f'http://image.tmdb.org/t/p/w600_and_h900_bestv2{str(imagem)}'
            try:
                bot.send_photo(mensagem.chat.id, photo=url_imagem)
            except:
                try:
                    send_photo = enviar_photo(url_imagem, mensagem.chat.id)
                    if send_photo == 2:
                        send_photo2 = enviar_photo(url_imagem_http, mensagem.chat.id)
                        if send_photo2 == 2:
                            bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                               'Link do poster do filme: ' + url_imagem)
                    if send_photo == 1:
                        send_photo3 = enviar_photo(url_imagem_http, mensagem.chat.id)
                        if send_photo3 == 1:
                            bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                               'Link do poster do filme: ' + url_imagem)
                except Exception as e:
                    try:
                        bot.send_photo(mensagem.chat.id, photo=url_imagem)
                    except:
                        bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                           'Link do poster do filme: ' + url_imagem)


        @bot.message_handler(commands=['rate_5_a_7'])
        def por_rate_bot_op2(mensagem):
            rate = random.randrange(5, 8)
            lista_filmes = aleatorio.listar_filmes_rate(rate)
            lista_aleatoria = aleatorio.lista_aleatoria(lista_filmes)
            saida = aleatorio.rodar(lista_aleatoria)
            saida_sinopse_link = f'{saida[0]}\n{saida[1]}'
            bot.send_message(mensagem.chat.id, saida_sinopse_link)
            imagem = saida[2]
            url_imagem = f'https://image.tmdb.org/t/p/w600_and_h900_bestv2{str(imagem)}'
            url_imagem_http = f'http://image.tmdb.org/t/p/w600_and_h900_bestv2{str(imagem)}'
            try:
                bot.send_photo(mensagem.chat.id, photo=url_imagem)
            except:
                try:
                    send_photo = enviar_photo(url_imagem, mensagem.chat.id)
                    if send_photo == 2:
                        send_photo2 = enviar_photo(url_imagem_http, mensagem.chat.id)
                        if send_photo2 == 2:
                            bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                               'Link do poster do filme: ' + url_imagem)
                    if send_photo == 1:
                        send_photo3 = enviar_photo(url_imagem_http, mensagem.chat.id)
                        if send_photo3 == 1:
                            bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                               'Link do poster do filme: ' + url_imagem)
                except Exception as e:
                    try:
                        bot.send_photo(mensagem.chat.id, photo=url_imagem)
                    except:
                        bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                           'Link do poster do filme: ' + url_imagem)


        @bot.message_handler(commands=['rate_8_a_10'])
        def por_rate_bot_op3(mensagem):
            rate = random.randrange(8, 11)
            lista_filmes = aleatorio.listar_filmes_rate(rate)
            lista_aleatoria = aleatorio.lista_aleatoria(lista_filmes)
            saida = aleatorio.rodar(lista_aleatoria)
            saida_sinopse_link = f'{saida[0]}\n{saida[1]}'
            bot.send_message(mensagem.chat.id, saida_sinopse_link)
            imagem = saida[2]
            url_imagem = f'https://image.tmdb.org/t/p/w600_and_h900_bestv2{str(imagem)}'
            url_imagem_http = f'http://image.tmdb.org/t/p/w600_and_h900_bestv2{str(imagem)}'
            try:
                bot.send_photo(mensagem.chat.id, photo=url_imagem)
            except:
                try:
                    send_photo = enviar_photo(url_imagem, mensagem.chat.id)
                    if send_photo == 2:
                        send_photo2 = enviar_photo(url_imagem_http, mensagem.chat.id)
                        if send_photo2 == 2:
                            bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                               'Link do poster do filme: ' + url_imagem)
                    if send_photo == 1:
                        send_photo3 = enviar_photo(url_imagem_http, mensagem.chat.id)
                        if send_photo3 == 1:
                            bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                               'Link do poster do filme: ' + url_imagem)
                except Exception as e:
                    try:
                        bot.send_photo(mensagem.chat.id, photo=url_imagem)
                    except:
                        bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                           'Link do poster do filme: ' + url_imagem)
            # bot.send_message(mensagem.chat.id, 'Não disponivel')


        @bot.message_handler(commands=['por_rate'])
        def por_rate_bot(mensagem):
            bot.send_message(mensagem.chat.id,
                             'Escolha o rate que deseja buscar:\n/rate_0_a_4\n/rate_5_a_7\n/rate_8_a_10\n'
                             'Outras opções serão consideradas inválidas')
            # bot.send_message(mensagem.chat.id, 'Não disponivel')


        @bot.message_handler(commands=['aleatorio'])
        def aleatorio_bot(mensagem):
            lista_filmes = aleatorio.listar_filmes()
            lista_aleatoria = aleatorio.lista_aleatoria(lista_filmes)
            saida = aleatorio.rodar(lista_aleatoria)
            saida_sinopse_link = f'{saida[0]}\n{saida[1]}'
            bot.send_message(mensagem.chat.id, saida_sinopse_link)
            imagem = saida[2]
            url_imagem = f'https://image.tmdb.org/t/p/w600_and_h900_bestv2{str(imagem)}'
            url_imagem_http = f'http://image.tmdb.org/t/p/w600_and_h900_bestv2{str(imagem)}'
            try:
                bot.send_photo(mensagem.chat.id, photo=url_imagem)
            except:
                try:
                    send_photo = enviar_photo(url_imagem, mensagem.chat.id)
                    if send_photo == 2:
                        send_photo2 = enviar_photo(url_imagem_http, mensagem.chat.id)
                        if send_photo2 == 2:
                            bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                               'Link do poster do filme: ' + url_imagem)
                    if send_photo == 1:
                        send_photo3 = enviar_photo(url_imagem_http, mensagem.chat.id)
                        if send_photo3 == 1:
                            bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                               'Link do poster do filme: ' + url_imagem)
                except Exception as e:
                    try:
                        bot.send_photo(mensagem.chat.id, photo=url_imagem)
                    except:
                        bot.send_message(mensagem.chat.id, 'Não foi possivel baixar a imagem\n'
                                                           'Link do poster do filme: ' + url_imagem)


        @bot.message_handler(commands=['rate_0_a_4'])
        def conselho_aleatorio(mensagem):
            a = 1

        def verificar(mensagem):
            try:
                texto = mensagem.text
                texto = texto.split('/')
                genero = texto[1]
                validacao = genero in dict_genero
                if validacao:
                    return por_genero_bot(mensagem, genero=genero, verificar=False)
                return True
            except Exception as e:
                texto = mensagem.text
                texto = texto.split(' - ')
                genero = texto[0]
                validacao = genero in dict_genero
                if validacao:
                    rate = texto[1]
                    rate = int(rate)
                    return por_rate_e_genero_bot(mensagem, genero=genero, rate=rate, verificar=False)

                return True


        @bot.message_handler(func=verificar)
        def start(mensagem):
            bot.send_message(mensagem.chat.id, 'Sou o Bot de filmes aleatórios\n'
                                               'Selecione uma das opções abaixo\n'
                                               '/aleatorio\n'
                                               '/por_rate\n'
                                               '/por_genero\n'
                                               '/por_rate_e_genero\n'
                                               '/conselho_aleatorio\n'
                                               'Outras opções serão consideradas inválidas')
            nome = mensagem.from_user.first_name
            teste_info = nome in infos
            if teste_info == False:
                chat_id = mensagem.chat.id
                infos[nome] = chat_id


        bot.polling()
    except Exception as e:
        print('Deu problema, reeiniciando ...')
        continue
