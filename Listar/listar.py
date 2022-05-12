import logging
from xml.dom.minidom import Document
from itsdangerous import exc
from mongoengine import *
from mongoengine.connection import connect
import mongoengine
from mongoengine.document import Document
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    nome = req.params.get('nome')
    try:
        lista = listar(nome)
        return func.HttpResponse(
            json.dumps(lista),
            status_code=200
    )
    except Exception as e:
        print(e)
        return func.HttpResponse(
            "Erro!",
           
            status_code=500
    )
    
    

   
def listar(escolha):
    
    dic = {} 
    contador = 0 
    #SELECIONA UM PRODUTO EM ESPECIFICO DE ACORDO COM O FILTRO (QUE NO CASO É O NOME)
    if len(escolha) >= 2:
        for  registro in Colecao.objects():
            if registro['NOME'] == escolha:
                dic[contador] = { "NOME": registro['NOME'], "DESCRICAO" : registro['DESCRICAO'], "VALOR" :registro['VALOR'] }
                contador +=1
        print("passo 1 ok")
    #PUXA A LISTA INTEIRA CASO NÃO TENHA NOME 
        
    else:
        for  registro in Colecao.objects():
            dic[contador] = { "NOME": registro['NOME'], "DESCRICAO" : registro['DESCRICAO'], "VALOR" :registro['VALOR'] }
            contador +=1
        print("passo 2 ok")
    return dic
    
def tamanho():
    print("pega tamanho ok")
    return len(Colecao.objects())   
mongoengine.connect(host = "mongodb+srv://username:password@servername.ssha1.mongodb.net/databasename?retryWrites=true&w=majority")

class Colecao(Document):

    NOME = mongoengine.StringField()
    DESCRICAO = mongoengine.StringField()
    VALOR = mongoengine.FloatField()
