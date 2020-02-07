# Twilio-Call-SMS-Handler
## Description
This repository represents an AWS Lambda Deployment Package (LDP). The Lambda Function is triggered by webhooks from Twilio to an AWS API Gateway endpoint. Each client has a Twilio phone number. The script can handle multiple clients. Calls/SMS are forwarded to the client. An additional text is sent to the client, informing the client that the referral is from me. Communication is logged in Google Sheets by using AWS Simple Notification Service to trigger another Lambda Function.<br/>
## Setup (optional)
This repository already contains the necessary libraries. If you would like to update the libraries or add your own, use the below steps to create a Docker Container that mimics the AWS Lambda (EC2) environment. It is necessary to do this to get the proper Linux binaries:<br/>

    $ cd <working directory on local machine>
    $ # NOTE: Below '$(pwd)' is used because an absolute path is required.
    $ docker run -v $(pwd):/working -it --rm amazonlinux
    $ yum install -y python3-pip
    $ cd working
    $ pip3 install -y -r requirements.txt

Now, outside of the container, copy the installed files from working into your LDP. Zip the contents of the folder and upload to AWS Lambda.<br/>
## twilio_call_sms_handler.py
This is the only code file that I created in this repository. Everything else is part of the Twilio Library, which is needed for the LDP.