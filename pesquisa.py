import requests

def pesquisar_artigo(titulo):
    url = f"https://api.crossref.org/works?query.title={titulo}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["message"]["total-results"] > 0:
            artigo = data["message"]["items"][0]
            return artigo
        else:
            return None
    else:
        return None

def main():
    titulo = input("Digite o título do artigo que deseja pesquisar: ")
    artigo = pesquisar_artigo(titulo)
    if artigo:
        print("Artigo encontrado:")
        print("Título:", artigo["title"][0])
        print("Autores:", ", ".join(artigo["author"]))
        print("DOI:", artigo["DOI"])
    else:
        print("Nenhum artigo encontrado com o título fornecido.")

if __name__ == "__main__":
    main()
