import logging
from xml.dom.minidom import Document
from mongoengine import *
from mongoengine.connection import connect
import mongoengine
from mongoengine.document import Document
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    nome = req.params.get('nome')
    
    deletar(nome)
 
    return func.HttpResponse(
            "Deletado com sucesso!",
            status_code=200
    )

   
def deletar(identificacao): 
    item = Colecao.objects(NOME = identificacao)
    item.delete()


mongoengine.connect(host = "mongodb+srv://username:password@servername.ssha1.mongodb.net/databasename?retryWrites=true&w=majority")

class Colecao(Document):

    NOME = mongoengine.StringField()
    DESCRICAO = mongoengine.StringField()
    VALOR = mongoengine.FloatField()
