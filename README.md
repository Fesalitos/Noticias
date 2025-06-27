Relatório de Estágio - Projeto: Extração de Notícias e Cotação de Moeda
1. Introdução
O objetivo deste projeto foi desenvolver um sistema que extrai notícias de economia de uma fonte confiável e, simultaneamente, obtém as cotações de moedas (como o Dólar e o Euro) em tempo real. O código foi desenvolvido utilizando a linguagem Python e as bibliotecas BeautifulSoup e Requests para fazer scraping das notícias e acessar uma API para as cotações.

O projeto foi organizado de forma modular, onde a função principal coleta as notícias e cotações e as exibe de maneira organizada.

2. Funcionalidade do Código
O código desenvolvido realiza as seguintes tarefas:

Extração de Notícias: Utiliza a biblioteca BeautifulSoup para acessar as páginas do G1 (seção de Economia) e extrair as últimas notícias relacionadas a economia.

Obtenção de Cotação de Moeda: Através da API https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL, o sistema consulta e exibe a cotação do Dólar e do Euro em relação ao Real.

Exibição de Dados: As notícias e as cotações são exibidas no terminal de forma organizada, mostrando o título da notícia, horário de publicação e o link da matéria, juntamente com as cotações das moedas.

3. Resultados
Notícias Extraídas
O código foi configurado para buscar até 3 páginas de notícias. Como resultado, foram extraídas as últimas notícias de economia com seus respectivos horários de publicação e links para as matérias. Exemplo de uma saída de notícias extraídas:

G1 - ECONOMIA
--------------------------------------------------------------------------------
TÍTULO                                             HORÁRIO              LINK
Ações da Nike disparam 17% após planos de reduzir  Há 10 minutos        https://g1.globo.com/economia/noticia/2025
Número de filhos por mulher no Brasil é o menor da Há 2 horas           https://g1.globo.com/economia/noticia/2024
Venezuelanos superam portugueses e passam a ser a  Há 3 horas           https://g1.globo.com/economia/noticia/2023
Cotação do Dólar e do Euro
A cotação do Dólar e do Euro foi consultada em tempo real utilizando a API. O sistema retornou os seguintes valores:

mathematica
Copiar
Editar
COTAÇÃO DO DÓLAR: R$ 5.4676
COTAÇÃO DO EURO: R$ 6.40205
Esses valores são extraídos diretamente da API de câmbio e são atualizados em tempo real.

4. Resultados Esperados vs Resultados Obtidos
Notícias
O código foi capaz de extrair e exibir corretamente as últimas notícias de economia. Porém, como o G1 possui atualizações frequentes, o número de notícias e os horários podem variar dependendo do momento em que o código é executado.

Cotação das Moedas
As cotações do Dólar e do Euro foram corretamente obtidas a partir da API e exibidas de forma clara. A API fornece valores precisos e atualizados de acordo com as flutuações do mercado cambial.

5. Conclusão
O sistema desenvolvido cumpre sua função de forma eficiente, proporcionando uma interface simples e objetiva para a exibição de notícias e cotações de moedas. O código foi escrito de maneira modular, facilitando futuras manutenções e expansões, como a adição de mais moedas ou a extração de notícias de outras fontes.

O uso de APIs e técnicas de web scraping permitiu que o sistema fosse autossuficiente, extraindo dados automaticamente e atualizando-os conforme necessário. O projeto demonstra as habilidades adquiridas no estágio, como o uso de bibliotecas externas, o manejo de APIs e o tratamento de dados obtidos da web.

6. Sugestões para Melhorias Futuras
Adição de Outras Moedas: Incorporar a cotação de outras moedas além do Dólar e Euro.

Interface Gráfica: Criar uma interface gráfica simples para o usuário final, facilitando a visualização dos dados.

Melhoria no Scraping: Melhorar o tratamento de exceções e o tempo de espera entre requisições para evitar sobrecarga no servidor do site de notícias.
