import requests
import os
from functools import reduce


def get_accounts_by_bank(bank_name, account_list):
    """
    retorna las cuentas de un banco
    """

    return list(
        filter(lambda account: account.get('institution').get('name') == bank_name, account_list)
    )

def get_kpi(bank_accounts):
    """
    obtiene el kpi en base a las cuentas de un banco
    """
    incomes = list(filter(lambda account: account.get('balance_type') == 'ASSET', bank_accounts))
    incomes = list(map(lambda account: account.get('balance', {}).get('available'), incomes))
    print('incomes')
    print(incomes)
    total_income = reduce(lambda a,b: a + b, incomes) if incomes else 0
    print(f'total income: {total_income}')

    expenses = list(filter(lambda account: account.get('balance_type') == 'LIABILITY', bank_accounts))
    expenses = list(map(lambda account: account.get('balance', {}).get('available'), expenses))
    print('expenses')
    print(expenses)
    total_expences = reduce(lambda a,b: a + b, expenses) if incomes else 0
    print(f'total expenses: {total_expences}')

    return round(total_income - total_expences, 2)


def format_bank_data(bank_name, accounts):
    """
    formatea el banco para la lista final
    """
    bank_accounts = get_accounts_by_bank(bank_name, accounts)
    print(f'bank: {bank_name}')
    return {
        'bank_name': bank_name,
        'accounts': bank_accounts,
        'kpi': get_kpi(bank_accounts)
    }


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
    accounts_by_bank = [format_bank_data(bank, accounts) for bank in bank_list]


    return {'status': 1, 'accounts': accounts_by_bank}

def get_accounts_by_bank_from_api(bank_code: str):
    url = f'{os.environ['BELVO_ACCOUNTS_LIST']}&institution={bank_code}'

    print('url to get accounts')
    print(url)
    accounts_response = requests.get(
        url,
        auth=(
            os.environ['BELVO_SECRET_ID'],
            os.environ['BELVO_SECRET_PASSWORD']
        )
    )

    return accounts_response.json().get('results', [])
