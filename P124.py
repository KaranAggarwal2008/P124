from flask import Flask, jsonify, request
app = Flask(__name__)
contact = [{
    'id': 1,
    'Contact': '9915654677',
    'Name': 'Karan',
    'done': False
},
    {
    'id': 2,
    'Contact': '8360612056',
    'Name': 'ALternate',
    'done': False
}
]
@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "PLEASE PROVIDE THE DATA"
        }, 400)
    contacts = {
        'id': contact[-1]['id'] + 1,
        'Contact': request.json['Contact'],
        'Name': request.json.get('Name', ""),
        'done': False
    }
    contact.append(contacts)
    return jsonify(
        {
            "status": "success",
            "message": "Contacts Added succefully"
        }
    )
@app.route("/get-data", methods=["GET"])
def get_task():
    return jsonify({
        "data": contact
    })
if(__name__ == "__main__"):
    app.run(debug=True)
