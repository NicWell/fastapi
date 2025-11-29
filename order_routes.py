from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/") #roteador definindo o caminho e o tipo de request
async def pedidos():
    #explicar os parametros da nossa rota
    """_summary_

    Returns:
        essa é a rota padrão de pedidos do nosso sistema
    """
    return {"mensagem":"voce acessou a rota de pedidos"}