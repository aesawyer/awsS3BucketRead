# Adam Sawyer. 2018. Python-Lambda function
# Alt-Shift-T : Show Todo Sidebar

import boto3
import os.path
import json

def lambda_handler(event, context):
    client = boto3.client('s3')
    s3 = boto3.resource('s3')
    bucketBack = s3.Bucket('MOVIE_BUCKET_NAME')
    bucketTar = s3.Bucket('TARGET_BUCKET_NAME')

    for obj in bucketBack.objects.all():
        files.append(obj.key, obj.metadata)
    movieList = s3.Object(bucketTar, 'movieList.txt').put(Body=json.dumps(files))
    return "Success"
