## This is the code for Listing S3

import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List all the S3 buckets
response = s3.list_buckets()

# Get the list of bucket names
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print the list of bucket names
print("Bucket names:")
for bucket in buckets:
    print(bucket)


#############################################################
