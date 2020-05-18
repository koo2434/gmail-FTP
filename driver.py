from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import os.path
from queue import *
import gmail_listener
#import file_processor
from concurrent.futures import ThreadPoolExecutor
import threading

SCOPES = ['https://mail.google.com/']
CREDENTIALS = 'credentials.json'

class Driver:

    def __init__(self):
        self.creds = None
        self.service = None
        self.auth_accounts = None
        self.process_queue = PriorityQueue()
        self.send_queue = PriorityQueue()

        self.__set_creds_service()
        self.__set_auth_accounts()

    def __set_creds_service(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        if not self.creds or not self.creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS, SCOPES)
            self.creds = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)
        self.service = build('gmail', 'v1', credentials=self.creds)

    def __set_auth_accounts(self):
        with open('authorized_accounts.txt', 'rt') as accounts:
            self.auth_accounts = [account.strip() for account in accounts]

    def begin(self):
        _gmail_listener = gmail_listener.GmailListener(
                                    self.service,
                                    self.process_queue,
                                    self.send_queue,
                                    self.auth_accounts)
        #_file_processor = file_processor.FileProcessor(
        #                            self.service,
        #                            self.process_queue,
        #                            self.send_queue)
        #_gmail_sender = gmail_sender.GmailSender(
        #                            self.service,
        #                            self.send_queue)

        exec = ThreadPoolExecutor(max_workers = 3)
        r1 = exec.submit(_gmail_listener.listen_new_emails)
        #r2 = exec.submit(_file_processor.process_file_requests)
        #r3 = exec.submit(_gmail_sender.send_emails)

        exec.shutdown(wait = True)
        print("Finishing process...")
        print("Done.")

if __name__ == '__main__':
    d = Driver()
    d.begin()
