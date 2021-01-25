# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html

import boto3
import base64
from botocore.exceptions import ClientError
import requests
import json
import os

class secrets_manager:
    def __init__(self):
        self.secrets_manager_client = self.get_secrets_manager_client()
        self.region = os.environ.get('region')
        self.env = os.environ.get('env')

    def get_secrets_manager_client(self):
        # Create a Secrets Manager client
        session = boto3.session.Session()
        secrets_manager_client = session.client(
            service_name='secretsmanager',
            region_name=self.region
        )
        return secrets_manager_client

    def get_secret(self, secret_name):
        secret = self.secrets_manager_client.get_secret_value(
            SecretId=f'{self.env}/{secret_name}'
        )
        return json.loads(secret['SecretString'])


