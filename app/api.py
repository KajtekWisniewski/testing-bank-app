from flask import Flask, request, jsonify

from .AccountRegistry import RegisterAccount
from .CustomerAccount import CustomerAccount

app = Flask(__name__)

@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f'Create account with data: {data}')
    acc = RegisterAccount.find_account_with_pesel(data["pesel"])
    if acc == None:
        acc = CustomerAccount(data["imie"], data["nazwisko"], data["pesel"])
        RegisterAccount.add_account(acc)
        return jsonify({"message": "Account Created"}), 201
    else:
        return jsonify({"message": "Account with given pesel already exists"}), 409

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

@app.route("/api/accounts/<pesel>/transfer", methods=['POST'])
def transfer_through_api(pesel):
    acc = RegisterAccount.find_account_with_pesel(pesel)
    data = request.get_json()
    if acc != None:
        if data["type"] == "incoming":
            acc.incoming_transfer(data["amount"])
            return jsonify({"message": "incoming transfer accepted for fulfillment"}), 200
        elif data["type"] == "outgoing":
            acc.outgoing_transfer(data["amount"])
            return jsonify({"message": "outgoing transfer accepted for fulfillment"}), 200
    else:
        return jsonify({"message": "account not found"}), 404

@app.route("/api/accounts/save", methods=['PATCH'])
def save_through_api():
    RegisterAccount.save()
    return jsonify({"message": "successfuly saved"}), 201

@app.route("/api/accounts/load", methods=['PATCH'])
def load_through_api():
    RegisterAccount.load()
    return jsonify({"message": "successfuly loaded"}), 201