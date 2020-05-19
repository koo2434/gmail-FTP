from queue import *
import os
import platform

CMD_DICT = {'get', 'help', 'show'}
# help is redundant as help request is taken cared of in GmailListener
# but is included for the sake of legibility.

class FileProcessor:
    def __init__(self, service,
                process_queue, send_queue):
        self.service = service
        self.process_queue = process_queue
        self.send_queue = send_queue

    def process_request(self):
        request = self.process_queue.get(block=True)

        req = request.split(' ')[0].strip().lower()
        if req is None or req == 'help' or req not in CMD_DICT:
            with open('./instruction.txt', 'r') as inst_file:
                instruction = inst_file.read()
                instruction = instruction.replace('$SYSTEM_NAME$', platform.uname()[1] + "'s", 1)
                self.send_queue.put((0, 'm', instruction))
        elif req == 'get':
            file_path = request.split('"')[1]
            if (not os.path.exists(file_path)) or (not os.path.isfile(file_path)):
                self.send_queue.put((0, 'm', "FILE NOT FOUND: " + file_path))
            else:

                pass
                #self.send_queue.put((1, 'g', file_path))
        elif req == 'show':
            path = request.split('"')[1]

            pass
