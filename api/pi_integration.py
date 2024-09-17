import requests
from config.config import Config

def check_balance(pi_wallet_address):
    url = f"{Config.PI_NETWORK_BASE_URL}/wallet/{pi_wallet_address}/balance"
    headers = {'Authorization': f'Bearer {Config.PI_NETWORK_API_KEY}'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('balance')
    else:
        return None

def transfer_to_bank(pi_wallet_address, bank_account, amount):
    balance = check_balance(pi_wallet_address)
    
    if balance is None or balance < amount:
        return {'error': 'Insufficient balance'}
    
    # 模拟与银行系统的交互
    # 这里调用银行API完成转账
    # transfer_to_bank_api_call(bank_account, amount)
    
    return {'success': True, 'message': f'{amount} Pi transferred to bank account {bank_account}'}
