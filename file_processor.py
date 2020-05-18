
import threading
import time
from Queue import Queue

CMD_DICT = {'get', 'help', 'has', 'show'}
# help is redundant as help request is taken cared of in GmailListener
# but is included for the sake of legibility.

class FileProcessor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.file_request_queue = Queue(maxsize = 5)

    def __is_valid_request(self, file_request):
        file_request = file_request.trim()
        parsed_request = file_request.split(" ")
        if parsed_request is None or parsed_request[0].lower() not in CMD_DICT:
            return false
        cmd = parsed_request[0].lower()

        if cmd is 'get':
