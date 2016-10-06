from flask import Flask, jsonify
import subprocess as sp

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

    # TODO Run the calculation script here for real result data, i.e.
    # cmd = './airfoil'
    # params = [cmd, num_samples, visc, speed, time, mesh]
    cmd = 'echo'
    params = [cmd, 'Hello Airfoil!']
    # Runs a specified program on command line
    output = sp.check_output(params)
    
    # TODO Spawn docker instance via docker-py?

    lift_force = 3.0
    drag_force = 2.12
    
    return jsonify({'result': {'lift_force': lift_force, 'drag_force': drag_force, 'output': output}})

if __name__ == '__main__':
    app.run(debug=True)
