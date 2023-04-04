# Libraries
from pprint import pprint
from flask import Flask, json, request, render_template
import sys, os, getopt, json
from webexteamssdk import WebexTeamsAPI
import requests
import meraki
import time
import shutil
import datetime


token = "MWM5NWRiYTctOWJkZS00NjA1LWJiZTItMzc2Yzk2M2Y3YjQ1Yzc0ZGY2ODgtNTgw_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

ROOM_ID = "Y2lzY29zcGFyazovL3VzL1JPT00vZTYwNTc5NTAtMmMzNS0xMWVjLWE3MzgtY2ZlNmFkNzRkNjc0"

MERAKI_API_KEY="b7f21d401cfcce7311c94edc2a41cd048bea032d"


# WEBEX TEAMS CLIENT
if token != '':
    webexapi = WebexTeamsAPI(access_token=token)
    webex_flag = True
else:
    webex_flag = False




# Flask App
app = Flask(__name__)

# Webhook Receiver Code - Accepts JSON POST from Meraki and
# Posts to WebEx Teams
@app.route("/", methods=["POST"])
def get_webhook_json():
    global webhook_data

    # Webhook Receiver
    webhook_data_json = request.json
    pprint(webhook_data_json, indent=1)
    webhook_data = json.dumps(webhook_data_json)

    try:
        teams_message = "## {}\n".format("Meraki Notifier")
        teams_message += "* Data is: {}\n".format(webhook_data_json)
        # teams_message += "* Alert Type: {}\n".format(webhook_data_json['alertType'])
        # teams_message += "* Network URL: {}\n".format(webhook_data_json['networkUrl'])
    except:
        teams_message = "Please check meraki webhook"
            
    to = "swsingh3@cisco.com"
    webexapi.messages.create(roomId=ROOM_ID, markdown=teams_message)
                 
    return "WebHook POST Received"


def create():
    print("Print random message here")


if __name__ == "__main__":
    app.run(debug=False)
