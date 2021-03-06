from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import os.path
from queue import *
from concurrent.futures import ThreadPoolExecutor, wait
import time
import requests

import gmail_listener
import file_processor
import gmail_sender

SCOPES = ['https://mail.google.com/']
CREDENTIALS = './credential.json'

class Driver:

    def __init__(self):
        self.creds = None
        self.service = None
        self.auth_accounts = None
        self.process_queue = Queue()
        self.send_queue = PriorityQueue()

        self.__set_creds_service()
        self.__set_auth_accounts()

        self.debug = [False] # For debug, remove before deploying

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

    def console_reader(self):
       con = input()
       if con == 'stop' or con == 'Stop':
           self.debug[0] = True

    def begin(self):
        _gmail_listener = gmail_listener.GmailListener(
                                    self.service,
                                    self.process_queue,
                                    self.send_queue,
                                    self.auth_accounts,
                                    self.debug)
        _file_processor = file_processor.FileProcessor(
                                    self.service,
                                    self.process_queue,
                                    self.send_queue,
                                    self.debug)
        _gmail_sender = gmail_sender.GmailSender(
                                    self.service,
                                    self.send_queue,
                                    self.debug)

        exec = ThreadPoolExecutor(max_workers = 4)
        r1 = exec.submit(_gmail_listener.listen_new_emails)
        r2 = exec.submit(_file_processor.process_requests)
        r3 = exec.submit(_gmail_sender.send_emails)

        r4 = exec.submit(self.console_reader)

        print("Starting...")
        exec.shutdown(wait=True)
        print("Finishing process...")
        print("Done.")

def is_internet_on():
    try:
        r = requests.get('https://8.8.8.8')
        return True
    except (requests.ConnectionError, requests.Timeout) as err:
        return False

if __name__ == '__main__':
    if is_internet_on():
        d = Driver()
        d.begin()
    else:
        print("Check internet connection.")
