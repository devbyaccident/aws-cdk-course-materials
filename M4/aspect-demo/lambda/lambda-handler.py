# Forked from https://github.com/antonycc/aws-serverless-lambda-python
import os
import logging
import boto3
import uuid

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

def main(event, context):    
    if 'Records' in event:
        process_all_records(event['Records'])

def process_all_records(records):
    destination_bucket = os.environ['DestinationBucket']
    for record in records:
        source_bucket = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key'] 
        copy_between_buckets(source_bucket, destination_bucket, object_key)

def copy_between_buckets(source_bucket, destination_bucket, object_key):    
    local_filepath = '/tmp/{}{}'.format(uuid.uuid4(), object_key)
    s3_client.download_file(source_bucket, object_key, local_filepath)
    s3_client.upload_file(local_filepath, destination_bucket, object_key)
    logger.info("Created s3://{}/{}".format(destination_bucket, object_key))