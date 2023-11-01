import boto3
from botocore.exceptions import NoCredentialsError

# Configuraciones
BUCKET_NAME = 'mi-nuevo-bucket-unico-2023-11-01'  # Cambia esto a un nombre único para tu bucket
REGION = 'eu-south-2'  # Cambia esto a tu región preferida

def create_bucket(bucket_name, region):
    s3_client = boto3.client('s3', region_name=region)
    
    try:
        response = s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region},
        )
        
        # Establecer la política para asegurarnos de que el bucket no sea público
        s3_client.put_bucket_acl(
            Bucket=bucket_name,
            ACL='private'  # Asegura que el bucket sea privado
        )
        
        print(f'Bucket {bucket_name} creado exitosamente en la región {region}.')
        return response
    except NoCredentialsError:
        print('No se encontraron credenciales. Asegúrate de configurar boto3 correctamente.')
        return None
if __name__ == '__main__':
    create_bucket(BUCKET_NAME, REGION)