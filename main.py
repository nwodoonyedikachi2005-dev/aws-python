import boto3
import logging
import s3_fuctions as s3_buck
import security_groups_functions as sg
from botocore.exceptions import ClientError


s3 = boto3.client("s3")
ec2 = boto3.client("ec2")


logging.basicConfig(
    filename="results.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

s3_b = s3_buck.list_s3_buckets()
for bucket in s3_b["Buckets"]:
 logging.info("bucket name: %s", bucket["Name"])
 try:
  s3.get_bucket_encryption(
   Bucket=bucket["Name"]
  )
  logging.info("buckets encryption default")
 except ClientError as e:
  if e.s3_b["Error"]["Code"] == "ServerSideEncryptionConfigurationNotFoundError":
    logging.warning("there is no encryption")

sg_groups = sg.list_security_groups()
for group in sg_groups:
   logging.info("SECURITY GROUPS: %s", group["GroupName"])
   print("\n inbound rules")
for rule in sg_groups:
        print(rule)
for FromPort in rule:
        from_port = rule.get("FromPort")
        to_port = rule.get("ToPort")
        if from_port==22 and to_port==22:
            logging.warning("YOUR SSH PORT IS OPEN!")
for ip_range in rule.get("IpRanges", []):
    ip = ip_range["CidrIp"]
    if ip=="0.0.0.0/0":
        logging.warning("YOUR SECURITY GROUP CAN BE ACCESSED THROUGH THE INTERNET")