from apiclient import errors
import time
import traceback
import logging

SCOPES = ['https://mail.google.com/']
CREDENTIALS = 'credentials.json'
CMD_DICT = {'get', 'help', 'has', 'show'}

class GmailListener:
    def __init__(self, service,
                process_queue, send_queue,
                auth_accounts):
        self.service = service
        self.process_queue = process_queue
        self.send_queue = send_queue
        self.auth_accounts = auth_accounts
        self.recent_history_id = -1

        self.__set_recent_id()

    def __set_recent_id(self):
        results = self.service.users().messages().list(userId='me',labelIds = ['INBOX']).execute()
        messages = results.get('messages', [])
        if not messages:
            print('No messages found.')
        else:
            recent_msg = self.service.users().messages().get(userId='me', id = messages[0]['id']).execute()
            self.recent_history_id = recent_msg['historyId']

    def __get_sender_email_address(self, id):
        addr = self.service.users().messages().get(userId='me', id = id, format='metadata',
                                metadataHeaders=['From'], fields='payload/headers').execute()
        print(addr)
        addr = addr.get('payload').get('headers')[0].get('value')
        print(addr)
        return addr.split('<')[1].split('>')[0]

    def listen_new_emails(self):
        print("Listening...")
        try:
            for _ in range (10):
                results = self.service.users().history().list(userId='me', startHistoryId=self.recent_history_id).execute()
                messages = results.get('history', [])
                if not messages:
                    print('ID {0}: No new messages.'.format(self.recent_history_id))
                else:
                    latest_new_message = messages[-1]
                    id = latest_new_message.get('messages')[0].get('id')
                    recent_msg = self.service.users().messages().get(userId='me', id = id).execute()
                    recent_msg_email_addr = self.__get_sender_email_address(id)
                    recent_msg_body = recent_msg['snippet'].strip()
                    self.recent_history_id = recent_msg['historyId']

                    print(recent_msg_email_addr)
                    print(recent_msg_body)
                    print(recent_msg['historyId'])

                    self.process_queue.put((recent_msg_email_addr, recent_msg_body))

                time.sleep(3)
        except Exception as e:
            logging.error(traceback.format_exc())
