## This is the code for Listing S3

import boto3

s3 = boto3.client("s3")
result = s3.list_buckets()

for bucket in result["Buckets"]:
    name = bucket["Name"]
    size = 0
    for key in s3.list_objects(Bucket=name)["Contents"]:
        size += key["Size"]
    print(f"Bucket: {name} - Size: {size/(1024**3):.2f} GB")
