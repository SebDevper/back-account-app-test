import requests
import os

def get_transactions_by_account_from_api(account_id: str, link_id: str):
    base_url = os.environ['BELVO_MOVEMENTS_LIST']
    url = f'{base_url}&link={link_id}&account={account_id}'
    print('url to get movements')
    print(url)
    accounts_response = requests.get(
        url,
        auth=(
            os.environ['BELVO_SECRET_ID'],
            os.environ['BELVO_SECRET_PASSWORD']
        )
    )

    return accounts_response.json().get('results', [])