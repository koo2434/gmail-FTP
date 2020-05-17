from google.cloud import pubsub_v1
from googleapiclient.discovery import build
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://mail.google.com/']
def get_creds():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials2.json', SCOPES)
        creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

service = build('gmail', 'v1', credentials=get_creds())
#Push
request = {
    'labelIds': ['INBOX'],
    'topicName': 'projects/quickstart-1589434138460/topics/dev_gmail_listener'
}
print(service.users().watch(userId='me',body=request).execute())

'''
project_id = "quickstart-1589434138460"
subscription_name = "dev_gmail_subscriber"
timeout = 30.0  # "How long the subscriber should listen for
# messages in seconds"

subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_name}`
subscription_path = subscriber.subscription_path(
    project_id, subscription_name
)

def callback(message):
    print("Received message: {}".format(message))
    message.ack()

streaming_pull_future = subscriber.subscribe(
    subscription_path, callback=callback
)
print("Listening for messages on {}..\n".format(subscription_path))

# Wrap subscriber in a 'with' block to automatically call close() when done.
with subscriber:
    print("waiting")
    streaming_pull_future.result(timeout=timeout)
    '''
