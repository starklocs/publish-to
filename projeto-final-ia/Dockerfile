# Use uma imagem base Python 3.10
FROM python:3.10-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o arquivo de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código para o diretório de trabalho
COPY . .

# Expõe a porta que o Streamlit usa
EXPOSE 8501

# Comando para rodar o aplicativo Streamlit
# O -s. significa que a chave da API será lida do ambiente do sistema
CMD ["streamlit", "run", "src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]