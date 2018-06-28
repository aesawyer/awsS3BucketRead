# Adam Sawyer. 2018. Python-Lambda function

import boto3
import os
import json

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    bucketBack = s3.Bucket(os.environ['MOVIE_BUCKET_NAME'])
    bucketTar = s3.Bucket(os.environ['TARGET_BUCKET_NAME'])
    name = 'movieList.txt'
    data = []

    for obj in bucketBack.objects.all():
        data.append(obj.key)
    formatString = ' || '.join(data)

    bucketTar.put_object(
        ACL='public-read',
        Key=name,
        Body=formatString
    )

    print(formatString)
    return "Uploaded to " + str(bucketTar)
