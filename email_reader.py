from googleapiclient.discovery import build
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
from apiclient import errors

import threading
import time

SCOPES = ['https://mail.google.com/']

class GmailListener:
    def __init__(self):
        self.creds = None
        self.service = None
        self.recentHistoryId = -1

    def set_creds_service(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        if not self.creds or not self.creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials2.json', SCOPES)
            self.creds = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)
        self.service = build('gmail', 'v1', credentials=self.creds)

    def set_recent_id(self):
        results = self.service.users().messages().list(userId='me',labelIds = ['INBOX']).execute()
        messages = results.get('messages', [])
        print(messages)
        if not messages:
            print("No messages found.")
        else:
            recentMsg = self.service.users().messages().get(userId='me', id = messages[0]['id']).execute()
            self.recentHistoryId = recentMsg['historyId']

    def get_new_emails(self):
        try:
            while _ in range (10):
                results = self.service.users().history().list(userId='me', startHistoryId=self.recentHistoryId).execute()
                message = results.get('history', [])
                if not message:
                    print("{0}: No new messages.".format(self.recentHistoryId))
                else:
                    latestMessage = message[-1]
                    id = latestMessage.get('messages')[0].get('id')
                    print(id)
                    recentMsg = self.service.users().messages().get(userId='me', id = id).execute()
                    print(recentMsg['snippet'])
                    self.recentHistoryId = recentMsg['historyId']
                time.sleep(3)
        except errors.HttpError as error:
            print(error)


if __name__ == '__main__':

    listener = GmailListener()
    listener.set_creds_service()
    listener.set_recent_id()
    #listener.test_history_list(3936)
    listener.get_new_emails()
