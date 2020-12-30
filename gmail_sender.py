from queue import *
from apiclient import errors
import traceback
import logging

class GmailSender:
    def __init__(self, service, send_queue,
                    debug):
        self.service = service
        self.send_queue = send_queue

        self.debug = debug

    def send_emails(self):
        print("Sending...")
        while self.debug[0] is not True:
            encoded_msg = None
            try:
                encoded_msg = self.send_queue.get(timeout = 3)[1]
            except Empty:
                continue
            print("detected: sending")
            try:
                result = (self.service.users().messages()
                        .send(userId='me', body=encoded_msg)
                        .execute())
                print('Message sent: ID #' + result['id'])
            except Exception as e:
                logging.error(traceback.format_exc())

        print("STOP: Sending")
