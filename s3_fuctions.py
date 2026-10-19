import boto3
s3 = boto3.client("s3")



def list_s3_buckets():
    response = s3.list_buckets()
    for bucket in response["Buckets"]:
        print (bucket["Name"])
    return response


