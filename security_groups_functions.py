import boto3
ec2 = boto3.client("ec2")

def list_security_groups():
    response = ec2.describe_security_groups()
    for sg in response["SecurityGroups"]:
        print("SECURITY GROUPS:", sg["GroupName"])
    return response["SecurityGroups"]
