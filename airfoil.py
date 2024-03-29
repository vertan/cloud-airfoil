from flask import Flask, jsonify, request
import subprocess as sp
from airfoil_helper import get_flow_result

app = Flask(__name__)

global_run_id = 10

@app.route('/airfoil/api/v1.0/')
def index():
    return "Airfoil API v1.0!"

@app.route('/airfoil/api/v1.0/flow/', methods=['GET'])
def get_flo():
    angle_start = request.args.get('angle_start', 10, type=int)
    angle_stop = request.args.get('angle_stop', 15, type=int)
    n_angles = request.args.get('n_angles', 5, type=int)
    n_nodes = request.args.get('n_nodes', 200, type=int)
    n_levels = request.args.get('n_levels', 0, type=int)
    num_samples = request.args.get('num_samples', 10, type=int)
    visc = request.args.get('visc', 0.001, type=float)
    speed = request.args.get('speed', 10, type=int)
    time = request.args.get('time', 0.02, type=int)

    print angle_start, angle_stop, n_angles, n_nodes, n_levels, num_samples, visc, speed, time

    global global_run_id
    result = get_flow_result(angle_start, angle_stop, n_angles, n_nodes,
                             n_levels, num_samples, visc, speed, time, global_run_id)
    
    global_run_id+=1

    # Return the correct results here, only test data now
    #return jsonify({'result': {'lift_force': 1, 'drag_force': 2, 'output': result[0]}})
    #return "What."
    return "The result will soon be available on this URL: http://130.238.29.253:8080/swift/v1/PotatisProject/?prefix=Airfoil_" + str(global_run_id-1) + "/"
if __name__ == '__main__':
    app.run(host='0.0.0.0')
