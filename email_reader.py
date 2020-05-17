from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import os.path
import base64
from apiclient import errors
import time

SCOPES = ['https://mail.google.com/']

class GmailListener:
    def __init__(self):
        self.creds = None
        self.service = None
        self.recentHistoryId = -1
        self.authorizedAccounts = []

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
        if not messages:
            print("No messages found.")
        else:
            recentMsg = self.service.users().messages().get(userId='me', id = messages[0]['id']).execute()
            self.recentHistoryId = recentMsg['historyId']

    def set_authorized_accounts(self):
        with open('authorized_accounts.txt', 'rt') as accounts:
            self.authorizedAccounts = [account.strip() for account in accounts]
        print(self.authorizedAccounts[0])

    def get_new_emails(self):
        try:
            for _ in range (10):
                results = self.service.users().history().list(userId='me', startHistoryId=self.recentHistoryId).execute()
                messages = results.get('history', [])
                if not messages:
                    print("ID {0}: No new messages.".format(self.recentHistoryId))
                else:
                    latestNewMessage = messages[-1]
                    id = latestNewMessage.get('messages')[0].get('id')
                    recentMsg = self.service.users().messages().get(userId='me', id = id).execute()
                    recentMsgBody = recentMsg['snippet'].strip()
                    self.recentHistoryId = recentMsg['historyId']

                    print(recentMsgBody)
                time.sleep(3)
        except errors.HttpError as error:
            print(error)

    def test(self):
        try:
            for _ in range (10):
                results = self.service.users().history().list(userId='me', startHistoryId=self.recentHistoryId).execute()
                messages = results.get('history', [])
                if not messages:
                    print("ID {0}: No new messages.".format(self.recentHistoryId))
                else:
                    latestNewMessage = messages[-1]
                    id = latestNewMessage.get('messages')[0].get('id')
                    recentMsg = self.service.users().messages().get(userId='me', id = id).execute()
                    recentMsgEmail = self.service.users().messages().get(userId='me', id = id, format='metadata',
                                            metadataHeaders=['From'], fields='payload/headers').execute()
                    recentMsgEmail = recentMsgEmail.get('payload').get('headers')[0].get('value')
                    recentMsgBody = recentMsg.get('snippet').strip()
                    self.recentHistoryId = recentMsg.get('historyId')

                    print(recentMsgEmail)
                    print(recentMsgBody)
                time.sleep(3)
        except errors.HttpError as error:
            print(error)

if __name__ == '__main__':
    listener = GmailListener()
    listener.set_creds_service()
    listener.set_recent_id()
    #listener.set_authorized_accounts()
    #listener.get_new_emails()
    listener.test()
