# Azure-Beginner
Começando a trabalhar com azure

# Previsão de Aluguéis de Bicicletas

Este projeto utiliza um modelo de regressão desenvolvido na Azure Machine Learning para prever o número de bicicletas que podem ser alugadas em um determinado período no futuro. A aplicação foi criada como uma API para facilitar o acesso às previsões.

---

## 🛠 Tecnologias Utilizadas

- **Microsoft Azure Machine Learning** (para treinamento e hospedagem do modelo)
- **FastAPI** (para criar uma API acessível e interativa)
- **Uvicorn** (servidor ASGI para rodar a aplicação localmente)
- **Python 3.10+** (linguagem de programação)

---

## 📋 Objetivo

O objetivo do projeto é ajudar locadoras de bicicletas a planejar melhor suas operações, oferecendo previsões baseadas em fatores como:
---

## 🚀 Como Configurar o Projeto

1. **Clone o repositório**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd nome-do-repositorio

2. Instale as dependências :  pip install fastapi uvicorn requests
3.  Inicie o servidor : uvicorn main:app --reload

4.  Testar API: uvicorn main:app --reload
5.  Estrutura do Repositório
main.py: Código principal da aplicação FastAPI.
endpoints.json: Arquivo contendo a descrição e exemplos dos endpoints disponíveis.
README.md: Este arquivo, explicando o projeto.
💻 Sobre o Modelo
O modelo de regressão foi treinado usando o Microsoft Azure Machine Learning e é baseado em dados históricos de aluguéis de bicicletas. Ele considera variáveis como condições climáticas, horário e padrões sazonais.

Principais Métricas de Avaliação:
R² Score: 0.85
Mean Absolute Error (MAE): 12 aluguéis
Root Mean Squared Error (RMSE): 15 aluguéis

📌 Observações
Certifique-se de configurar suas chaves de acesso da Azure no código caso o modelo esteja sendo chamado por meio da nuvem.
Este é um projeto em evolução, e futuras melhorias podem incluir:
Integração com bancos de dados
Dashboard de visualização
Mais variáveis preditoras para maior precisão


