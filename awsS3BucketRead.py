# Adam Sawyer. 2018. Python-Lambda function

import boto3
import os
import json

def lambda_handler(event, context):
    files = []
    s3 = boto3.resource('s3')
    bucketBack = s3.Bucket(os.environ['MOVIE_BUCKET_NAME'])
    bucketTar = s3.Bucket(os.environ['TARGET_BUCKET_NAME'])

    for obj in bucketBack.objects.all():
        files.append(obj.key)
    formatString = ' | '.join(files)

    print(formatString)
    return formatString
