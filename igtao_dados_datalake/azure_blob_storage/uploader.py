from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()

class AzureBlobUploader:
    def __init__(self, container_name):
        self.storage_account_key = os.environ['STORAGE_ACCOUNT_KEY']
        self.container_name = container_name
        self.blob_service_client = BlobServiceClient.from_connection_string(self.storage_account_key)
        self.container_client = self.blob_service_client.get_container_client(self.container_name)

    def upload_file(self, file_path):
        filename = os.path.basename(file_path)
        blob_client = self.container_client.get_blob_client(filename)

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        
        print(f"Upload do {filename} concluído!")

    def upload_files_from_directory(self, directory_path):
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            if os.path.isfile(file_path):
                self.upload_file(file_path)