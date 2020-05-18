from queue import *

CMD_DICT = {'get', 'help', 'show'}
# help is redundant as help request is taken cared of in GmailListener
# but is included for the sake of legibility.

class FileProcessor:
    def __init__(self, service,
                process_queue, send_queue):
        self.service = service
        self.process_queue = process_queue
        self.send_queue = send_queue

    def __is_valid_request(self, file_request):
        file_request = file_request.trim()
        parsed_request = file_request.split(" ")
        if parsed_request is None or parsed_request[0].lower() not in CMD_DICT:
            return false
        req = parsed_request[0].lower()

        if req is 'get':
