##############################################################################################################
# script:   twilio_call_sms_handler.py
# by:       Darren Hakimi
# desc:     Lambda Function is triggered by webhooks from Twilio to AWS API Gateway endpoint.
#           Each client has a Twilio phone number. The script handles multiple clients.
#           Calls/SMS are forwarded to client. An additional text is sent to the client,
#           informing the client that the referral is from me.
#           Communication is logged by using AWS Simple Notification Service to trigger another Lambda.
# rqmts:    Twilio Library, Twilio credentials, AWS ARN associated with AWS SNS trigger.
##############################################################################################################

# pip3 install -t . --upgrade twilio
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

from urllib.parse import unquote_plus
import json
import boto3

from credentials import credentials

ACCOUNT_SID = credentials['twilio']['account_sid']
AUTH_TOKEN = credentials['twilio']['auth_token']

##############################################################################################################
# LOG - Uses AWS Simple Notification Service to trigger the Twilio Google Sheets Logger Lambda Function.
##############################################################################################################
def log(client_name, client_description, lead_number, call_or_sms, body):
    message = {
        "client_name": client_name, 
        "client_description": client_description, 
        "lead_number": lead_number, 
        "call_or_sms": call_or_sms, 
        "body": body
    }
    client = boto3.client('sns', region_name='us-east-1')
    arn = credentials['twilio']['aws_arn_google_sheets_logger']
    response = client.publish(
        TargetArn=arn,
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json'
    )

##############################################################################################################
# SMS - Send text message from verified Twilio phone number to other phone number.
##############################################################################################################
def sms(to_number, from_number, msg):
    """Using our caller's number and the number they called, send an SMS."""
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(
        body=msg,
        from_=from_number,
        to=to_number
    )
    resp = MessagingResponse()
    return str(resp)

##############################################################################################################
# CALL - Forwards call to given phone number.
##############################################################################################################
def call(forward_to_number):
    """Respond to incoming phone calls with a message."""
    # Start our TwiML response / forward call
    resp = VoiceResponse()
    resp.dial(forward_to_number)

    return str(resp)

##############################################################################################################
# LAMBDA_HANDLER - Determine whether received call or sms, for which client it is for, and handle it.
##############################################################################################################
def lambda_handler(event, context):
    # unquote_plus is used to decode characters from the webhook (e.g. '%2b' => '+')
    twilio_number = unquote_plus(event.get('To', ""))
    lead_number = unquote_plus(event.get('From', ""))
    body = unquote_plus(event.get('Body', ""))
    print("to_number: {}\nfrom_number: {}\nbody: {}".format(twilio_number, lead_number, body))

    # twilio_dict contains all phone_numbers that this lambda will handle.
    # Rather than build a Lambda for each client, I have parameterized client info.
    twilio_dict = {
        "+12223334444": (
            "Test_Name", 
            "Test_Description", 
            "+12121234567"
        )
    }

    if twilio_number in twilio_dict:
        client_name, client_description, client_phone_number = twilio_dict[twilio_number]
        message = "REFERRAL FROM: Darren Hakimi\nLEAD PHONE NUMBER-- {}\nINQUIRING ON {} Listing:\n".format(lead_number, client_description)
        if body:
            log(client_name, client_description, lead_number, "sms", body)
            message = "{}\n{}".format(message, body)
            return sms(client_phone_number, twilio_number, message)
        else:
            log(client_name, client_description, lead_number, "call", "")
            message = "{}THIS LEAD CALLED YOU!".format(message)
            sms(client_phone_number, twilio_number, message)
            return call(client_phone_number)
