#Exibe os documentos indentados
def printIndentJson():
    import json
    from pymongo import MongoClient
    from sys import argv
    #variavel para controlar a quantidade de json printado de forma indentada
    limit=argv[0]
    #Cria uma conexão com o mongodb
    connection = MongoClient('localhost', 27017)
    #Cria um banco como nome 'json_stream_db' caso nao exista
    db = connection.json_stream_db
    #Cria uma coleção dentro do banco 'json_stream_db' com o nome 'json_collection' caso não exista
    collection = db.json_stream_db
    collection = db.json_collection
    for post in collection.find().limit(limit):
        #Elimina do dicionario o id gerado pelo mongodb para poder indentar
        post.pop('_id', None)
        #exibe de forma indentada os json's existentes na coleção
        print(json.dumps(post, indent=4))