from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/airfoil/api/v1.0/')
def index():
    return "Airfoil API v1.0!"

@app.route('/airfoil/api/v1.0/flow/', methods=['GET'])
def get_flow():
    # TODO Make it possible to get real input from user
    num_samples = 1
    visc = 0.0001
    speed = 10
    time = 1
    mesh = "./test_mesh.xml"

    # TODO Run the calculation script here for real result data
    # TODO Spawn docker instance via docker-py

    lift_force = 3.0
    drag_force = 2.12
    
    return jsonify({'result': {'lift_force': lift_force, 'drag_force': drag_force}})

if __name__ == '__main__':
    app.run(debug=True)
