import boto3

# Definir el nombre del rol IAM y el ID de la instancia EC2
iam_instance_profile_name = "WriteS3ObjectRole"
instance_id = "i-0848976b2fa28e596"  # Reemplaza con el ID de tu instancia EC2

# Crear un cliente de EC2
ec2 = boto3.client("ec2")

# Asociar el rol IAM a la instancia EC2
response = ec2.associate_iam_instance_profile(
    IamInstanceProfile={
        "Name": iam_instance_profile_name
    },
    InstanceId=instance_id
)

print("Rol IAM asociado a la instancia EC2:", response)