import boto3

ACCESS_KEY = ""
SECRET_KEY = ""
LOCAL_FILE = "local_file_name"
BUCKET_NAME = "bucket_name"
S3_FILE_NAME = "file_name_on_s3"

def upload_to_s3(local_file, bucket, s3_file):
    # This function is responsible for uploading the file into the S3 bucket using the specified credentials
    s3 = boto3.client(
        "s3", aws
    )