from flask import Flask, json
from instruments.instrument import Instrument
from instruments.users import User
import json

app = Flask(__name__)


instruments_list = {}
user_list = {}


@app.route('/')
def index():
    return "hello world"


@app.route('/instruments')
def get_instruments():
    instruments = []
    for instrument_id in instruments_list:
        instruments.append(instruments_list[instrument_id].to_json())

    response = app.response_class(
        response=json.dumps(instruments_list),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/user')
def get_User():
    users = []
    for User_id in user_list:
        users.append(user_list[User_id].to_json())

    response = app.response_class(
        response=json.dumps(users),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run()

def addNewInstrument(instrument):
    musicalInstrument = Instrument(instrument)
    instrument_add = json.load(musicalInstrument.MakeAInstrumentDictionary())
    instruments_list[instrument_add['id']] = instrument_add


def addNewUser(user):
    newUser = User(user)
    print(newUser)
    user_add = json.load(newUser.MakeAUserDictionary())
    user_list[user_add["id"]] = user_add
