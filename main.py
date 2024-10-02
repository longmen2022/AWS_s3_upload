# This imports the boto3 library, which is the AWS SDK for Py. It allows us to interact with various AWS services,
# including S3
import boto3
# This imports the NoCredentialsError exception from the botocore lib, which is used to handle erros related to
# missing AWS credentials
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = ""
SECRET_KEY = ""
LOCAL_FILE = "pexels-frank-cone-140140-3250638.jpg"
BUCKET_NAME = "uploadBucket"
S3_FILE_NAME = "S3BucketUpload"


def upload_to_s3(local_file, bucket, s3_file):
    # This function is responsible for uploading the file into the S3 bucket using the specified credentials
    s3 = boto3.client(
        "s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY
    )
    try: # This block attempts to upload the file to S3
        # This method uploads the specified local file to the specified S3 bucket with the specified S3 file name.
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError: #This block catches the FileNotFoundError if the local file is not found
        print("The file was not found")
        return False
    except NoCredentialsError: # The block catches the NoCredentialsError if the AWS credentials are not available
        print("Credentials not available")
        return False


result = upload_to_s3(LOCAL_FILE, BUCKET_NAME, S3_FILE_NAME)
