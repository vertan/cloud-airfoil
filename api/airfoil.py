from flask import Flask, jsonify, request
import subprocess as sp
from airfoil_helper import get_flow_result

app = Flask(__name__)

@app.route('/airfoil/api/v1.0/')
def index():
    return "Airfoil API v1.0!"

@app.route('/airfoil/api/v1.0/flow/', methods=['GET'])
def get_flow():
    angle_start = request.args.get('angle_start')
    angle_stop = request.args.get('angle_stop')
    n_angles = request.args.get('n_angles')
    n_nodes = request.args.get('n_nodes')
    n_levels = request.args.get('n_levels')
    num_samples = request.args.get('num_samples')
    visc = request.args.get('visc')
    speed = request.args.get('speed')
    time = request.args.get('time')

    result = get_flow_result(angle_start, angle_stop, n_angles, n_nodes,
                             n_levels, num_samples, visc, speed, time)

    # Return the correct results here, only test data now
    return jsonify({'result': {'lift_force': 1, 'drag_force': 2, 'output': result[0]}})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
