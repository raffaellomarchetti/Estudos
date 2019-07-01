import json
from sseclient import SSEClient as EventSource
from pymongo import MongoClient  
#Cria uma conexão com o mongodb
connection = MongoClient('localhost', 27017)
#Fonte de dados
url = "https://stream.wikimedia.org/v2/stream/recentchange"  
#variavel booleana para filtrar o tipo de bot
bot_value = False
#variavel que irá receber o json
str_to_dict={}
#variavel para controlar a quantidade de json printado de forma indentada
limit=2
#Lista de nomes dos db existentes
dbnames = connection.list_database_names()
#Cria um banco como nome 'json_stream_db' caso nao exista
db = connection.json_stream_db
#Cria uma coleção dentro do banco 'json_stream_db' com o nome 'json_collection' caso não exista
collection = db.json_stream_db
collection = db.json_collection

#Verifica se o banco ja existe, caso exista o banco a colecão será truncada
if 'json_stream_db' in dbnames:
    collection.delete_many({})
#Para cada evento disponivel na URL irá acontecer uma iteração, assim fazendo o processo de streaming
for event in EventSource(url):
    #Cada evento que for uma mensagem, será trazido em formato json
    if event.event == 'message':
        data='{{"id":{0},"data":{1}}}'.format(event.id,event.data)
        #Tentará converter a string para dicionário, caso consiga significa que é um json 'válido', 
        #caso contrario irá para o proximo evento
        try:
            str_to_dict=json.loads(data)
            #Caso o valor da chave 'bot' seja igual ao valor filtrado, 
            #o json será armazenado na coleção de json's via pymongo
            if str_to_dict['data']['bot'] == bot_value:
                post_id = collection.insert_one(str_to_dict)
        except:
            pass
