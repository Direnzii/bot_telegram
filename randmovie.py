from os import getenv
import requests
import random
from googletrans import Translator

class assistir_filme():
    token = getenv(key="CHAVE_API_FILMES")
    dict_genero = {"terror":27, "acao":28, "comedia":35, "drama":18, "ficcao_cientifica":878,
               "fantasia":14, "familia":10751, "aventura":12, "misterio":9648, "suspense":53,
               "crime":80, "cinemaTv":10770, "romance":10749}

    def numero_aleatorio(self, limite_range=501):
        numero_aleatorio = random.randrange(1, limite_range)
        return numero_aleatorio

    def chunks(self, lista):
        for i in range(0, len(lista), 4):
            yield lista[i:i + 4]

    def lista_aleatoria(self, lista):
        lista = list(self.chunks(lista))
        count_list = len(lista)
        numero = random.randrange(0, count_list +1)
        try:
            list_aleatoria = lista[numero]
        except:
            numero = numero - 1
            list_aleatoria = lista[numero]
        return list_aleatoria

    def requisicao(self, url):
        requisicao = requests.get(url)
        json = requisicao.json()
        return json

    def listar_filmes_rate_genero(self, rate, genero):
        while True:
            lista_filmes = []
            genero_id = self.dict_genero[f"{genero}"]
            url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                        f"api_key={self.token}&" \
                        "include_adult=false&" \
                        "include_video=false&" \
                        f"page={self.numero_aleatorio()}&" \
                        f"vote_average.gte={rate}&" \
                        f"with_genres={genero_id}"
            filmes = self.requisicao(url_geral)
            filmes = filmes['results']
            if not filmes:
                continue
            else:
                for movie in filmes:
                    id = movie['id']
                    lista_filmes.append(id)
                return lista_filmes

    def listar_filmes_genero(self, genero):
        while True:
            lista_filmes = []
            genero_id = self.dict_genero[f"{genero}"]
            url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                        f"api_key={self.token}&" \
                        "include_adult=false&" \
                        "include_video=false&" \
                        f"page={self.numero_aleatorio()}&" \
                        f"with_genres={genero_id}"
            filmes = self.requisicao(url_geral)
            filmes = filmes['results']
            if not filmes:
                continue
            else:
                for movie in filmes:
                    id = movie['id']
                    lista_filmes.append(id)
                return lista_filmes

    def listar_filmes_rate(self, rate, max_rate=10):
        contador_de_tentativas = 0
        while True:
            if rate >=0 and rate <=4:
                max_rate = 4
            if rate >= 5 and rate <= 7:
                max_rate = 7
            if rate >= 8 and rate <= 10:
                max_rate = 10

            lista_filmes = []
            url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                        f"api_key={self.token}&" \
                        "include_adult=false&" \
                        "include_video=false&" \
                        f"page={self.numero_aleatorio()}&" \
                        f"vote_average.gte={rate}&" \
                        f"vote_average.lte={max_rate}"
            filmes = self.requisicao(url_geral)
            filmes = filmes['results']
            if not filmes:
                contador_de_tentativas += 1
                if contador_de_tentativas == 20:
                    url_geral = f'https://api.themoviedb.org/3/discover/movie?' \
                                f'api_key={self.token}&' \
                                f'include_adult=false&' \
                                f'include_video=false&page={self.numero_aleatorio(limite_range=max_rate)}&' \
                                f'vote_average.gte={rate}&' \
                                f'vote_average.lte={max_rate}'
                    filmes = self.requisicao(url_geral)
                    filmes = filmes['results']
                    if not filmes:
                        continue
                    for movie in filmes:
                        id = movie['id']
                        lista_filmes.append(id)
                    return lista_filmes
                continue
            else:
                for movie in filmes:
                    id = movie['id']
                    lista_filmes.append(id)
                return lista_filmes

    def listar_filmes(self):
        while True:
            lista_filmes = []
            url_geral = "https://api.themoviedb.org/3/discover/movie?" \
                        f"api_key={self.token}&" \
                        "include_adult=false&" \
                        "include_video=false&" \
                        f"page={self.numero_aleatorio()}"
            filmes = self.requisicao(url_geral)
            filmes = filmes['results']
            if not filmes:
                continue
            else:
                for movie in filmes:
                    id = movie['id']
                    lista_filmes.append(id)
                return lista_filmes

    def rodar(self, lista_filmes):
        i = True
        while i:
            try:
                count_movies = len(lista_filmes)
                random_id = random.randrange(0, count_movies + 1)
                id_filme = lista_filmes[random_id]

                url_filme = f"https://api.themoviedb.org/3/movie/{id_filme}?" \
                            f"api_key={self.token}"
                filme = self.requisicao(url_filme)
                imagem = filme['poster_path']
                id = filme['id']
                url_id = 'https://www.themoviedb.org/movie/'+str(id)
                nome = filme['original_title']
                sinopse = filme['overview']
                translator = Translator()
                sinopse = translator.translate(text=sinopse, dest='pt')
                nome_pt = translator.translate(text=nome, dest='pt')
                if not sinopse:
                    sinopse = "Não encontrado"
                votos = filme['vote_average']
                saida = f'****** SEU FILME É ******\nNome: {nome_pt.text} ({nome})\nSinopse: {sinopse.text}\nMédia de votos: {votos}'
                i = False
                return [saida, url_id, imagem]
            except Exception as e:
                print("Algo deu errado, finalizando !")