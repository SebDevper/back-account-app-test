import requests
import os


def get_accounts_by_bank(bank_name, account_list):
    """
    retorna las cuentas de un banco
    """

    return list(filter(lambda account: account.get('institution').get('name') == bank_name, account_list))


def get_accounts():
    """
    retorna una lista de cuentas agrupadas por banco
    """
    accounts_response = requests.get(
        os.environ['BELVO_ACCOUNTS_API'],
        auth=(
            os.environ['BELVO_SECRET_ID'],
            os.environ['BELVO_SECRET_PASSWORD']
        )
    )

    # obtener lista de bancos
    accounts = accounts_response.json().get('results', [])
    bank_list = [account.get('institution').get('name') for account in accounts]
    bank_list = sorted(set(bank_list))

    # buscar las cuentas de cada banco y agregarlas
    accounts_by_bank = [{'bank_name': bank, 'acccounts': get_accounts_by_bank(bank, accounts)} for bank in bank_list]


    return {'status': 1, 'accounts': accounts_by_bank}
