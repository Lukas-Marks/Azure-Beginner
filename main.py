from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de entrada
class InputData(BaseModel):
    valor: float

# Endpoint para previsão
@app.post("/prever/")
def prever(dados: InputData):
    # Simulação de um modelo de previsão (multiplicando por 2)
    resultado = dados.valor * 2
    return {"valor_original": dados.valor, "previsao": resultado}

# Endpoint para teste
@app.get("/")
def home():
    return {"mensagem": "API de previsão funcionando!"}
