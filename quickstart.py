from __future__ import print_function
from googleapiclient.discovery import build
from apiclient import errors
#from httplib2 import Http
from email.mime.text import MIMEText
import base64
from google.oauth2 import service_account
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.cloud import pubsub_v1

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://mail.google.com/']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials2.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    #Push
    request = {
        'labelIds': ['INBOX'],
        'topicName': 'projects/quickstart-1589434138460/topics/dev_gmail_listener'
    }
    print(service.users().watch(userId='me',body=request).execute())

    #Send
    """
    message = MIMEText("this is a test.");
    message['to'] = 'lyuah2434@gmail.com'
    message['from'] = 'jaemo.developer@gmail.com'
    message['subject'] = 'This is a test.'
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    message = service.users().messages().send(userId='me', body={'raw': raw}).execute()
    """

if __name__ == '__main__':
    main()
