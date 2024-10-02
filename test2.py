import boto3

s3 = boto3.client('s3')

# Define your variables
LOCAL_FILE = "C:\Users\men_l\PycharmProjects\pythonProject10\test.py"
BUCKET_NAME = 'my-bucket'
S3_FILE_NAME = "C:\Users\men_l\PycharmProjects\pythonProject10\test.py"

# Upload the file
s3.upload_file(local_file, bucket_name, s3_file_name)
