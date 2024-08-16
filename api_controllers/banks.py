import requests
import os

def get_all_banks_from_api():
    banks_response = requests.get(
        os.environ['BELVO_BANK_LIST'],
        auth=(
            os.environ['BELVO_SECRET_ID'],
            os.environ['BELVO_SECRET_PASSWORD']
        )
    )
    return banks_response.json().get('results', [])