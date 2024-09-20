from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
import pandas as pd
import json
import dotenv
from dotenv import load_dotenv

env_path = ".env"
load_dotenv(env_path)

STORAGE_ACCOUNT_KEY = os.environ['STORAGE_ACCOUNT_KEY']
CONTAINER_JSON = os.environ['CONTAINER_JSON']
PATH = './json_files'

blob_service_client = BlobServiceClient.from_connection_string(STORAGE_ACCOUNT_KEY)
container_client = blob_service_client.get_container_client(CONTAINER_JSON)

def upload_files_to_blob(container_client):
    for filename in os.listdir(PATH):
        print("Verificando o arquivo ", filename)
        file_path = f'{PATH}/{filename}'
    
        if filename.endswith('.json'):
            with open(file_path, 'r') as f:
                data = json.load(f)
    
            blob_client = container_client.get_blob_client(os.path.basename(file_path))
            
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)
            
            print(f"Upload do {filename} concluído!")

upload_files_to_blob(container_client)