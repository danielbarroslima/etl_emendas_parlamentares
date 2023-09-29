<h1>
    <a>
     <img align="center" width="40px" src="images/aperto-de-mao.png"></a>
    <span> Aplicação para analisar valores das emendas parlamentares e verificar possíveis pontos de atenção.</span>
</h1>

Repositório desenvolvido para o desafio da Digital Inonovation One, onde aprendemos sobre [ETL](https://aws.amazon.com/pt/what-is/etl/) e colocamos em prática o mesmo extraindo os dados de alguma origem transformando estes dados com o auxílio do chatGpt e depois fazendo o carregamento dos dados em alguma fonte.

## Objetivo
Praticar as etapas do ETL para que possamos agregar conhecimento sobre o mesmo e adicionar conhecimento nos dados fornecidos.

## Sobre os dados abertos

Dados abertos
Aqui é possível baixar os dados apresentados no Portal da Transparência do Governo Federal, em formato aberto, possibilitando que os usuários façam cruzamentos e análises específicas, de acordo com suas necessidades.

Os arquivos são disponibilizados em formato CSV (clique para mais informações) nas abas abaixo, de acordo com o tema e a periodicidade de atualização das respectivas consultas.

A disponibilização de informações em dados abertos visa aumentar a transparência e a participação por parte do cidadão, além de gerar, potencialmente, diversas aplicações desenvolvidas colaborativamente pela sociedade.

## Ferramentas
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
[![GitHub](https://img.shields.io/badge/GitHub-222?style=for-the-badge&logo=github&logoColor=30A3DC)](https://docs.github.com/)
[![Git](https://img.shields.io/badge/Git-222?style=for-the-badge&logo=git&logoColor=E94D5F)](https://git-scm.com/doc)
[![Python](https://img.shields.io/badge/Python-222?style=for-the-badge&logo=python&logoColor=306998)](https://www.python.org/doc)


##  Desafio: Conta bancária con funções
 Neste projeto teremos as etapas de: extração, transformação e carregamento, referente ao ETL.

 Primeiro criamos um arquivo novo em formato utf-8 pegando como base o arquivo disponibilizado no site [Portal da Transparência](https://portaldatransparencia.gov.br/download-de-dados) para que possamos trabalhar como o mesmo sem erros referente ao encode do arquivo.

 Em seguiuda fazemos a verificação se todas as dependências necessárias estão disponíveis, caso não estejam serão instaladas.

 Depois disso começamos o processo em si, extraímos os dados e fazemos as somas dos valores informados das [emendas parlamentares](https://portaldatransparencia.gov.br/pagina-interna/605525-emendas-parlamentares) download no [link](https://portaldatransparencia.gov.br/download-de-dados/emendas-parlamentares) e com essa soma iremos analisar se há algum ponto de atenção para com os valores.

 Usaremos os seguites valores contidos no arquivo:
 `"Valor Empenhado", "Valor Liquidado", "Valor Pago", "Valor Restos A Pagar Inscritos", "Valor Restos A Pagar Cancelados" e "Valor Restos A Pagar Pagos"`

 Por fim iremos adicionar no arquivo criado em utf-8 esta análise com a data e um nome para que possa ser disponibilizado o mesmo.

### Instruções (PT/BR)
1. Precisará gerar a sua API_KEY do ChatGpt pode seguir estes [passos](https://platform.openai.com/account/api-keys).

2. Depois disso precisará apenas ir no arquivo transform.py e mudar o `YOUR_API_KEY` para a sua api_key gerada no passo anterior.

3. E por fim precisará apenas rodar o arquivo principal via terminal `python3 desafio.py` e será gerado um arquivo com o nome `emendas_utf8.csv` com os dados em utf-8 e a analise feita.
