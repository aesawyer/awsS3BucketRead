# Adam Sawyer. 2018. Python-Lambda function
# Alt-Shift-T : Show Todo Sidebar

import boto3
import os

def lambda_handler(event, context):
    client = boto3.client('s3')
    s3 = boto3.resource('s3')
    bucketBack = s3.Bucket('MOVIE_BUCKET_NAME')
    bucketTar = s3.Bucket('TARGET_BUCKET_NAME')
    obj = client.get_object(Bucket=bucketBack,Key='*') # TODO: resolve client.get_object return issues
    return obj
