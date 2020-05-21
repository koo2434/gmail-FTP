from queue import *
import platform
import base64
import os
import mimetypes
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import traceback
import logging

CMD_DICT = {'get', 'help', 'show'}
# help is redundant as help request is taken cared of in GmailListener
# but is included for the sake of legibility.

class FileProcessor:
    def __init__(self, service,
                process_queue, send_queue,
                debug):
        self.service = service
        self.process_queue = process_queue
        self.send_queue = send_queue
        self.from_email = service.users().getProfile(userId='me').execute()['emailAddress']

        self.debug = debug

    def __get_encoded_plain_message(self, to_email, from_email,
                                            subject, body):
        print("plain")
        message = MIMEText(body)
        message['to'] = to_email
        message['from'] = from_email
        message['subject'] = subject

        return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

    def __get_encoded_multimedia_message(self, to_email, from_email,
                                            subject, body, file_path):
        print("Multimedia")
        message = MIMEMultipart()
        message['to'] = to_email
        message['from'] = from_email
        message['subject'] = subject

        message.attach(MIMEText(body))

        with open(file_path, 'rb') as f:
            part = MIMEApplication(
                f.read(),
                Name=basename(file_path)
            )
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file_path)
        message.attach(part)

        return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

    def process_requests(self):
        print("Processing...")
        try:
            while self.debug[0] is not True:
                tup = None
                try:
                    tup = self.process_queue.get(timeout = 3)
                except Empty:
                    print("Processor: Empty queue")
                    continue
                print("detected: process")
                to_email = tup[0].strip()
                req = tup[1].split(' ')[0].strip().lower()

                if req is None or req == 'help' or req not in CMD_DICT:
                    print("Req not in correct form")
                    with open('./instruction.txt', 'r') as inst_file:
                        instruction = inst_file.read()
                        instruction = instruction.replace('$SYSTEM_NAME$',
                                                        platform.uname()[1] + "'s", 1)

                        encoded_msg = self.__get_encoded_plain_message(
                                                        to_email,
                                                        self.from_email,
                                                        'Request Processed',
                                                        instruction)

                        self.send_queue.put((0, encoded_msg))
                        print("in send_queue")
                elif req == 'get':
                    print(tup[1].split(' ', 1)[1])
                    file_path = tup[1].split(' ', 1)[1].split('&quot;')[1]
                    if (not os.path.exists(file_path)) or (not os.path.isfile(file_path)):
                        print("Get not found")
                        body = 'Requested file NOT FOUND: ' + file_path
                        encoded_msg = self.__get_encoded_plain_message(
                                                        to_email,
                                                        self.from_email,
                                                        'Requested file NOT FOUND',
                                                        body)
                        self.send_queue.put((0, encoded_msg))
                    else:
                        print("Get found")
                        body = 'Requested file: ' + file_path
                        encoded_msg = self.__get_encoded_multimedia_message(
                                                        to_email,
                                                        self.from_email,
                                                        'Requested file FOUND',
                                                        body,
                                                        file_path)
                        self.send_queue.put((1, encoded_msg))
                elif req == 'show':
                    path = request.split('"')[1]
                    pass
        except Exception:
            logging.error(traceback.format_exc())
        print("STOP: Processing")
