from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
env_path = ".env"
load_dotenv(env_path)

# Chaves da conta de armazenamento e nome do container
STORAGE_ACCOUNT_KEY = os.environ['STORAGE_ACCOUNT_KEY']
CONTAINER_AUDIOS = os.environ['CONTAINER_AUDIOS']
PATH = './audio_samples/audio_samples'

# Conectar-se ao serviço de blob usando a connection string
blob_service_client = BlobServiceClient.from_connection_string(STORAGE_ACCOUNT_KEY)
container_client = blob_service_client.get_container_client(CONTAINER_AUDIOS)

def upload_files_to_blob(container_client):
    for filename in os.listdir(PATH):
        file_path = f'{PATH}/{filename}'
        
        # Verificar se o caminho é um arquivo e tem a extensão .wav
        if os.path.isfile(file_path) and filename.endswith('.wav'):
            print(f"Lendo o arquivo: {filename}")
            
            # Obter o cliente do Blob para esse arquivo
            blob_client = container_client.get_blob_client(os.path.basename(file_path))
            
            # Abrir o arquivo .wav no modo binário e fazer o upload
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)
            
            print(f"Upload do arquivo {filename} concluído!")
        else:
            print(f"{filename} não é um arquivo .wav ou é um diretório.")

# Executar a função de upload
upload_files_to_blob(container_client)
