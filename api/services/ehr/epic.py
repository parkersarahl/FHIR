# services/ehr/epic.py
from urllib import response
from services.ehr.base import EHRVendor
import requests
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.x509 import load_pem_x509_certificate

from config import (
    EPIC_CLIENT_ID,
    EPIC_REDIRECT_URI,
    EPIC_AUTH_URL,
    EPIC_SCOPES,
    EPIC_TOKEN_URL,
    EPIC_CLIENT_SECRET,
)

EPIC_FHIR_URL = "https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4"
CLIENT_ID = EPIC_CLIENT_ID 
EPIC_TOKEN_URL = EPIC_TOKEN_URL
EPIC_AUTH_URL = EPIC_AUTH_URL

class EpicEHR(EHRVendor):
    @staticmethod
    def exchange_code_for_token(code: str) -> dict:
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": EPIC_REDIRECT_URI,
            "client_id": EPIC_CLIENT_ID,
            #"client_secret": EPIC_CLIENT_SECRET,
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        #print("🔥 exchange_code_for_token() was called!")
        #print("Sending token exchange request with:", data)
        response = requests.post(EPIC_TOKEN_URL, data=data, headers=headers)
        #print("Response status:", response.status_code)
        #print("Response text:", response.text)


        if response.status_code != 200:
            raise Exception(f"Token exchange failed: {response.status_code}, {response.text}")

        return response.json()  # access_token, id_token, etc.
