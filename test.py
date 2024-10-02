import boto3
from botocore.exceptions import NoCredentialsError
import os  # Import for environment variables

# Set environment variables for security (replace with your actual credentials)
os.environ['AWS_ACCESS_KEY_ID'] = ''
os.environ['AWS_SECRET_ACCESS_KEY'] = ''

LOCAL_FILE = "pexels-frank-cone-140140-3250638.jpg"
BUCKET_NAME = 'my-bucket'
S3_FILE_NAME = "uploaded_file.txt"  # Example filename in S3

def upload_to_s3(local_file, bucket, s3_file):
    # This function is responsible for uploading the file into the S3 bucket using environment variables
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
    )
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available (check environment variables)")
        return False

result = upload_to_s3(LOCAL_FILE, BUCKET_NAME, S3_FILE_NAME)