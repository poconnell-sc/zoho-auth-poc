import os
import requests
import time

class ZohoAuth:
    def __init__(self, client_id, client_secret, refresh_token, redirect_uri, token_url=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.redirect_uri = redirect_uri
        self.token_url = token_url or "https://accounts.zoho.com/oauth/v2/token"
        self.access_token = None
        self.expiry = 0  # Unix timestamp

    def get_token(self):
        if not self.access_token or time.time() > self.expiry:
            self.refresh_access_token()
        return self.access_token

    def refresh_access_token(self):
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
            "redirect_uri": self.redirect_uri,
            "grant_type": "refresh_token"
        }
        resp = requests.post(self.token_url, data=payload)
        resp.raise_for_status()
        token_data = resp.json()

        self.access_token = token_data['access_token']
        self.expiry = time.time() + token_data.get('expires_in', 3600) - 60  # buffer before expiry