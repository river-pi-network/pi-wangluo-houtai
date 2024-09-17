from flask import Flask, request, jsonify
from app.services import transfer_to_bank, transfer_to_pi

app = Flask(__name__)

@app.route('/transfer/pi-to-bank', methods=['POST'])
def pi_to_bank():
    data = request.get_json()
    pi_wallet_address = data.get('pi_wallet_address')
    bank_account = data.get('bank_account')
    amount = data.get('amount')
    
    if not pi_wallet_address or not bank_account or not amount:
        return jsonify({'error': 'Missing required parameters'}), 400
    
    result = transfer_to_bank(pi_wallet_address, bank_account, amount)
    return jsonify(result), 200

@app.route('/transfer/bank-to-pi', methods=['POST'])
def bank_to_pi():
    data = request.get_json()
    pi_wallet_address = data.get('pi_wallet_address')
    bank_account = data.get('bank_account')
    amount = data.get('amount')
    
    if not pi_wallet_address or not bank_account or not amount:
        return jsonify({'error': 'Missing required parameters'}), 400
    
    result = transfer_to_pi(bank_account, pi_wallet_address, amount)
    return jsonify(result), 200
