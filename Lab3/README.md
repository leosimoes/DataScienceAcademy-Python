# Lab 3 - Trabalhando com Expressões Regulares em Python com ChatGPT

## Regexs utilizados

Os regexs gerados pelo ChatGPT e utilizados no Lab foram:
- `r'\bfinito\b'` para contar a palavra "finito" na música.
- `r'\binfinito\b'` para contar a palavra "infinito" na música.
- `r'\w*finito\b'` para contar as palavras terminadas com "finito" na música.
- `r'\w*(H|h)á\b'` para contar as palavras "Há" ou "há" na música.
- `r'(H|h)á (\w+)\s+(\w+)'` para encontrar os pares de palavras que aparecem depois de "Há" ou "há" na música.
- `r'\b[\w]*(?:[áàâãéèêíïóôõöúü])[\w]*\b'` para encontrar apenas as palavras com algum acento da língua portuguesa na música.
- `r'\b\w+,(?=\s)'` para encontrar apenas as palavras que são sucedidas por vírgula na música.


## Referências

ChatGPT: https://chat.openai.com/ 
, Acessado em 13/05/2023.

Data Science Academy - Fundamentos de Linguagem Python Para Análise de Dados e Data Science (Com ChatGPT):
https://www.datascienceacademy.com.br/course/fundamentos-de-linguagem-python-para-analise-de-dados-e-data-science 
, Acessado em 13/05/2023.

Vagalume: https://www.vagalume.com.br/rosa-de-saron/algoritmo.html , Acessado em 13/05/2023.