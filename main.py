import boto3

AWS_ACCESS_key = ""
AWS_SECRET_KEY = ""
AWS_S3_BUCKET_NAME = "eagleimagebucket"
AWS_REGION = "us-east-2"

LOCAL_FILE = 'test_file.txt'
NAME_FOR_S3 = 'test_file.txt'


def main():
    print('in main method')
    s3_client = boto3.client(
        service_name='s3',
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_key,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    response = s3_client.upload_file(LOCAL_FILE, AWS_S3_BUCKET_NAME, NAME_FOR_S3)
    print(f'upload file response: {response}')


if __name__ == '__main__':
    main()
