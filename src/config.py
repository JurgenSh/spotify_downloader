import json
import os

def save_api_credentials(client_id, client_secret):
    credentials = {'client_id': client_id, 'client_secret': client_secret}
    with open('credentials.json', 'w') as f:
        json.dump(credentials, f)

def load_api_credentials():
    if os.path.exists('credentials.json'):
        with open('credentials.json', 'r') as f:
            credentials = json.load(f)
            return credentials.get('client_id'), credentials.get('client_secret')
    return None, None

def get_api_credentials(force_new=False):
    if not force_new:
        client_id, client_secret = load_api_credentials()
        if client_id and client_secret:
            return client_id, client_secret

    client_id = input("Please enter your Spotify Client ID: ")
    client_secret = input("Please enter your Spotify Client Secret: ")

    save_api_credentials(client_id, client_secret)

    return client_id, client_secret
