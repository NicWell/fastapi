from fastapi import FastAPI


app = FastAPI()

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