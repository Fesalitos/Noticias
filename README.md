Relatório de Estágio - Projeto: Extração de Notícias e Cotação de Moeda

O objetivo deste projeto foi desenvolver um sistema que extrai notícias de economia de uma fonte confiável e, simultaneamente, obtém as cotações de moedas (como o Dólar e o Euro) em tempo real. O código foi desenvolvido utilizando a linguagem Python e as bibliotecas BeautifulSoup e Requests para fazer scraping das notícias e acessar uma API para as cotações.
O projeto foi organizado de forma modular, onde a função principal coleta as notícias e cotações e as exibe de maneira organizada.

Funcionalidade do Código
O código desenvolvido realiza as seguintes tarefas:
Extração de Notícias: Utiliza a biblioteca BeautifulSoup para acessar as páginas do G1 (seção de Economia) e extrair as últimas notícias relacionadas a economia.
Obtenção de Cotação de Moeda: Através da API https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL, o sistema consulta e exibe a cotação do Dólar e do Euro em relação ao Real.
Exibição de Dados: As notícias e as cotações são exibidas no terminal de forma organizada, mostrando o título da notícia, horário de publicação e o link da matéria, juntamente com as cotações das moedas.

O código foi configurado para buscar até 3 páginas de notícias da seção de Economia do site G1. O resultado inclui as últimas notícias, com seus respectivos títulos, horários de publicação e links para as matérias. Exemplo:


--------------------------------------------------------------------------------
TÍTULO                                             HORÁRIO              LINK
Ações da Nike disparam 17% após planos de reduzir  Há 10 minutos        https://g1.globo.com/economia/noticia/2025
Número de filhos por mulher no Brasil é o menor da Há 2 horas           https://g1.globo.com/economia/noticia/2024
Venezuelanos superam portugueses e passam a ser a  Há 3 horas           https://g1.globo.com/economia/noticia/

Cotação do Dólar e do Euro
A cotação do Dólar e do Euro foi consultada em tempo real utilizando a API. O sistema retornou os seguintes valores:

COTAÇÃO DO DÓLAR: R$ 5.4676
COTAÇÃO DO EURO: R$ 6.40205

Resultados
Notícias
O código foi capaz de extrair e exibir corretamente as últimas notícias de economia. Porém, como o G1 possui atualizações frequentes, o número de notícias e os horários podem variar dependendo do momento em que o código é executado.
Cotação das Moedas
As cotações do Dólar e do Euro foram corretamente obtidas a partir da API e exibidas de forma clara. A API fornece valores precisos e atualizados de acordo com as flutuações do mercado cambial.
