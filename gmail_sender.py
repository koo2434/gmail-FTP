from apiclient import errors
import traceback
import logging

class GmailSender:
    def __init__(self, service, send_queue):
        self.service = service
        self.send_queue = send_queue

    def send_emails(self):
        print("Sending...")
        for _ in range(1):
            encoded_msg = self.send_queue.get(block=True)[1]
            print("detected: sending")
            try:
                result = (self.service.users().messages()
                        .send(userId='me', body=encoded_msg)
                        .execute())
                print('Message sent: ID #' + result['id'])
            except Exception as e:
                logging.error(traceback.format_exc())
