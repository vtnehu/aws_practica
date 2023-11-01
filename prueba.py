import boto3
import os

def generate_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def upload_to_s3(filename, bucket_name):
    s3 = boto3.client('s3')
    s3.upload_file(filename, bucket_name, filename)
    print(f"File {filename} uploaded to {bucket_name}")

if __name__ == '_main_':
    file_name = "sample.txt"
    content = "Este es mi texto de prueba"
    
    generate_file(file_name, content)
    upload_to_s3(file_name, "mi-nuevo-bucket-unico")  # reemplaza 'your-bucket-name' con el nombre de tu bucket

    # Limpiar: eliminar el archivo generado (opcional)
    os.remove(file_name)