import requests
from bs4 import BeautifulSoup

def buscar_noticias_g1(paginas=1):
    base_url = 'https://g1.globo.com/economia/'
    noticias = []
    horarios = []
    links = []

    for pagina in range(1, paginas + 1):
        url = f'{base_url}?page={pagina}'
        try:
            req = requests.get(url)
            req.raise_for_status()
            soup = BeautifulSoup(req.content, 'html.parser')

            noticia_lista = soup.find_all('a', class_='feed-post-link gui-color-primary gui-color-hover', href=True)
            horario_lista = soup.find_all('span', class_='feed-post-datetime')

            noticias.extend([noticia.text.strip() for noticia in noticia_lista])
            horarios.extend([horario.text.strip() for horario in horario_lista])
            links.extend([noticia['href'] for noticia in noticia_lista])

        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a página {pagina}: {e}")
    
    return noticias, horarios, links


def exibir_noticias(titulo, noticias, horarios, links, max_titulo_len=50, max_link_len=40, max_horario_len=20):
    print(f'{titulo:^80}')
    print('-' * 80)
    print(f'{"TÍTULO".ljust(max_titulo_len)} {"HORÁRIO".ljust(max_horario_len)} {"LINK".ljust(max_link_len)}')
    
    for i in range(len(noticias)):
        noticia = noticias[i][:max_titulo_len].ljust(max_titulo_len)
        horario = horarios[i][:max_horario_len].ljust(max_horario_len)
        link = links[i][:max_link_len].ljust(max_link_len)
        print(f'{noticia} {horario} {link}')


def obter_cotacao_moeda():
    url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL'
    try:
        response = requests.get(url)
        response.raise_for_status()
        cotacoes = response.json()

        cotacao_dolar = float(cotacoes['USDBRL']['bid'])
        cotacao_euro = float(cotacoes['EURBRL']['bid'])

        return cotacao_dolar, cotacao_euro
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter cotação: {e}")
        return None, None


def exibir_cotacoes(cotacao_dolar, cotacao_euro):
    print('-' * 80)
    if cotacao_dolar and cotacao_euro:
        print(f'COTAÇÃO DO DÓLAR: R$ {cotacao_dolar:.2f}')
        print(f'COTAÇÃO DO EURO: R$ {cotacao_euro:.2f}')
    else:
        print("Não foi possível obter as cotações.")


def main():
    print("Buscando notícias...")
    noticias, horarios, links = buscar_noticias_g1(paginas=3)
    exibir_noticias("G1 - ECONOMIA", noticias, horarios, links)
    
    print("\nBuscando cotações...")
    cotacao_dolar, cotacao_euro = obter_cotacao_moeda()
    exibir_cotacoes(cotacao_dolar, cotacao_euro)


if __name__ == "__main__":
    main()
