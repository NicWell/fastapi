from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv #importa as variaveis de ambiente
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY") #localiza a secret key

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #descriptografar as senhas

from order_routes import order_router #importando a rota de pedidos 
from auth_routes import auth_router #importando a rota de autorizacao

#incluindo as rotas no app
app.include_router(auth_router)
app.include_router(order_router)



# instanciando o app
#para rodar nosso sitema, uvicorn main:app --reload
#endpoints == rotas
#requisições
# get > leitura
# post > enviar
# patch > editar
# delete > deletar
# Temos uma rest Api