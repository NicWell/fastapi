from pydantic import BaseModel
from typing import Optional

#cria um modelo de usario e passa como parametros na requisição
class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]
    
    class Config:
        from_attributes = True