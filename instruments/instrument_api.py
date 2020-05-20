from flask import Flask, json, abort, request
from instruments.users import GetUser, addNewUser
from instruments.instrument import GetInstruments,  addNewInstrument
from instruments.instrument import add_key_to_instrument

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/instruments')
def get_all_instruments():
    response = app.response_class(
        response=json.dumps(GetInstruments()),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/users')
def get_users():
    response = app.response_class(
        response=json.dumps(GetUser()),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/add/instruments/<instrument_type>', methods=["GET", "POST"])
def add_new_instrument(instrument_type):
    addNewInstrument({"type": instrument_type})
    response = app.response_class(
        response=json.dumps({"type": instrument_type}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/add/user/<firstName>/<lastName>', methods=["GET", "POST"])
def add_new_user(firstName,lastName):
    addNewUser({"firstName": firstName, "lastName": lastName})
    response = app.response_class(
        response=json.dumps({"firstName": firstName, "lastName": lastName}),
        status=200,
        mimetype='application/json'
    )
    return response



@app.route("/instruments/<instrument_id>", methods=["GET"])
def get_instrument_by_instrument_id(instrument_id):
    instruments = GetInstruments()

    response = app.response_class(
        response=json.dumps(instruments[instrument_id]),
        status=200,
        mimetype='application/json'
    )
    return response



@app.route('/instruments/<instrument_id>/users/<user_id>', methods=["GET", "POST"])
def add_instrument_to_users(instrument_id, user_id):
    instruments = GetInstruments()
    users = GetUser()
    if instrument_id in instruments.keys() and user_id in users.keys():
        add_key_to_instrument("user_id", user_id, instrument_id)
    response = app.response_class(
        response=json.dumps({'user_id': user_id, "id": instrument_id}),
        status=200,
        mimetype='application/json'
    )
    return response




@app.route('/instruments/user/<user_id>', methods= ["GET", "Post"])
def get_instrument_by_user_id(user_id):
    instruments = GetInstruments()
    instrumentDict = {}

    for i in instruments.values():
        if i["user_id"] == user_id:
            instrumentDict[i["user_id"]] = i

    response = app.response_class(
         response=json.dumps(instrumentDict),
         status=200,
         mimetype='application/json'
    )
    return response



@app.route("/add/link/instruments/<id_instrument>", methods= ["GET", "POST"])
def add_video_to_Instrument(id_instrument):
    video = request.args.get("video")
    instruments = GetInstruments()

    if id_instrument in instruments.keys():
        add_key_to_instrument("video", video, id_instrument)

        response = app.response_class(
            response=json.dumps({id_instrument: video}),
            status=200,
            mimetype='application/json'

        )
        return response







@app.route('/users/<user_id>',methods=['DELETE'])
def delete_user_id(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if len(em) == 0:
    abort(404)
    empDB.remove(em[0])
    return jsonify({'response':'Success'})


if __name__ == '__main__':
    app.run()
