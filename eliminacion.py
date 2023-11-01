import boto3

# Reemplaza 'nombre-del-bucket' con el nombre del bucket que deseas eliminar
bucket_name = 'mi-nuevo-bucket-unico-2023-11-01'

# Crear un cliente de S3
s3 = boto3.client('s3')

# Listar todos los objetos en el bucket
objects = s3.list_objects_v2(Bucket=bucket_name)

# Eliminar los objetos dentro del bucket
if 'Contents' in objects:
    for obj in objects['Contents']:
        s3.delete_object(Bucket=bucket_name, Key=obj['Key'])

# Eliminar el bucket
s3.delete_bucket(Bucket=bucket_name)

print(f'Bucket {bucket_name} eliminado exitosamente.')
