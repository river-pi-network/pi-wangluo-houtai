import requests
from config.config import Config

def transfer_to_pi(bank_account, pi_wallet_address, amount):
    # 模拟调用银行API进行转账
    url = f"{Config.BANK_BASE_URL}/transfer"
    data = {
        'account': bank_account,
        'amount': amount,
        'destination_wallet': pi_wallet_address
    }
    headers = {'Authorization': f'Bearer {Config.BANK_API_KEY}'}
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        return {'success': True, 'message': f'{amount} transferred to Pi wallet {pi_wallet_address}'}
    else:
        return {'error': 'Bank transfer failed'}
