from flask import Flask, request, jsonify

from .AccountRegistry import RegisterAccount
from .CustomerAccount import CustomerAccount

app = Flask(__name__)

@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f'Create account with data: {data}')
    acc = CustomerAccount(data["imie"], data["nazwisko"], data["pesel"])
    RegisterAccount.add_account(acc)
    return jsonify({"message": "Account Created"}), 201

@app.route("/api/accounts/count", methods=['GET'])
def how_many_accs():
    count = RegisterAccount.how_many_accs()
    return jsonify({"message": f"There are {count} accounts in the database"}), 201

@app.route("/api/accounts/<pesel>", methods=['GET'])
def find_acc_with_pesel(pesel):
    acc = RegisterAccount.find_account_with_pesel(pesel)
    if acc != None:
        return jsonify({"name": acc.imie, "nazwisko": acc.nazwisko, "pesel": acc.pesel})
    else:
        return jsonify({"message": "account not found"}), 404