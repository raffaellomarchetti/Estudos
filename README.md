# Python Take Home Coding Test

## Objetivo
Construir uma pipeline para monitorar, armazenar e visualizar os eventos de mudança em tempo real proveniente do Wikipedia.

## Ferramentas e sua utilização
#### Python 3.6.5
Responsável pelo processo de extração, formatação e exportação dos dados.

#### MongoDB 4.0
Responsável pelo armazenamento dos Json's.

#### **HTML
Responsável pela estrutura e apresentação do site. (Não implementado)

#### **Charts.js
Responsável por construir e apresentar os gráficos. (Não implementado)

## Vantagens
A principal vantagem dessa arquitetura é o seu baixo custo, tanto de hardware quanto financeiro, pois são ferramentas leves e gratuitas. Outro ponto levado em consideração é a clareza das documentações e a facilidade de se encontrar bons materiais de estudo das mesmas.

## Desvantagens
Poderia ser utilizado em conjunto do Python, o framework Apache Spark em conjunto do Apache Kafka e Apache Hbase, para melhorar a performance paralelizando o processamento e deixando o programa mais escalável a longo prazo. Sintaxe do MongoDB não é muito amigável para usuários finais, se fosse utilizado ferramentas do Hadoop como Spark e Hive seria mais amigável pelo fato de suportarem a sintaxe SQL ou bem próxima ao SQL, tornando assim o programa mais amigável para usuários finais.

## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar as seguintes bibliotecas.

```bash
pip install pymongo
pip install sseclient
```
Para utilizar a biblioteca "pymongo" será necessário instalar o [mongodb](https://www.mongodb.com/download-center).
## Execução 
Para executar os programas, será necessário abrir 2 terminais. Em um terminal ficará em execução o programa responsável pelo streaming.
```bash
python StreamJson.py
```
No segundo terminal ficará em execução o programa responsável pela impressão do Json de forma indentada.

```bash
python printIndentJson.py
```
Como padrão apenas 1 Json será impresso, caso queira imprimir mais de 1, será necessário substituir o valor da variável 'limit' para a quantidade desejada.
