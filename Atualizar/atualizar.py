import logging
from xml.dom.minidom import Document
from mongoengine import *
from mongoengine.connection import connect
import mongoengine
from mongoengine.document import Document
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    
    atualizar(req_body['NOME'], req_body['DESCRICAO'],req_body['VALOR'])
 
    return func.HttpResponse(
            "Alterado com sucesso!",
            status_code=200
    )

   
def atualizar(name, desc,valor):
    Colecao.objects(NOME = name).update_one(DESCRICAO = desc)
    Colecao.objects(NOME = name).update_one(VALOR = valor)


mongoengine.connect(host = "mongodb+srv://username:password@servername.ssha1.mongodb.net/databasename?retryWrites=true&w=majority")

class Colecao(Document):

    NOME = mongoengine.StringField()
    DESCRICAO = mongoengine.StringField()
    VALOR = mongoengine.FloatField()
