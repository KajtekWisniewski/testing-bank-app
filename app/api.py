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
        return jsonify({"imie": acc.imie, "nazwisko": acc.nazwisko, "pesel": acc.pesel, "balance": acc.balance}), 201
    else:
        return jsonify({"message": "account not found"}), 404
    
@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def change_acc_by_pesel(pesel):
    acc = RegisterAccount.find_account_with_pesel(pesel)
    data = request.get_json()
    if acc != None:
        acc.imie = data["imie"]
        acc.nazwisko = data["nazwisko"]
        acc.pesel = data["pesel"]
        acc.balance = data["balance"]
        return jsonify({"imie": acc.imie, "nazwisko": acc.nazwisko, "pesel": acc.pesel, "balance": acc.balance}), 201
    else:
        return jsonify({"message": "account not found"}), 404

@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_acc_by_pesel(pesel):
    acc = RegisterAccount.find_account_with_pesel(pesel)
    if acc != None:
        RegisterAccount.listOfAccounts.remove(acc)
        return jsonify({"message": "successfuly deleted"}), 201
    else:
        return jsonify({"message": "account not found"}), 404
    

    
@app.route("/api/accounts/PURGE", methods=['DELETE'])
def empty_cls_list():
    RegisterAccount.listOfAccounts = []
    return jsonify({"message": "sucessfuly emptied the list"}), 201