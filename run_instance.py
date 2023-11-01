import sdk.boto3 as boto3
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Creamos sesion de AWS con perfil especifico
aws_session = boto3.Session(profile_name=os.environ.get("PROFILE"))

# Crea una instancia de cliente de EC2
ec2_client = aws_session.client('ec2')

# Variables de entorno para los parámetros
image_id = os.environ.get('AWS_IMAGE_ID')
instance_type = os.environ.get('AWS_INSTANCE_TYPE')
key_name = os.environ.get('AWS_KEY_NAME')
instance_name = os.environ.get('AWS_INSTANCE_NAME')


# Define los parámetros para la instancia
launch_params = {
    'ImageId': image_id,
    'InstanceType': instance_type,
    'KeyName': key_name,
    'TagSpecifications': [
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': instance_name
                },
            ]
        },
    ],
    'MaxCount': int(os.environ.get("AWS_MAX_COUNT_INSTANCES")),
    'MinCount': int(os.environ.get("AWS_MIN_COUNT_INSTANCES"))
}

# Crea la instancia
response = ec2_client.run_instances(**launch_params)

# Obtiene el ID de la instancia creada
instance_id = response['Instances'][0]['InstanceId']

print(f"Se ha creado la instancia con ID: {instance_id}")