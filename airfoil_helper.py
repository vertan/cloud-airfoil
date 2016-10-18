from tasks import get_flow

def get_flow_result(angle_start, angle_stop, n_angles, n_nodes,
                    n_levels, num_samples, visc, speed, time, run_id):
    step = (angle_stop-angle_start)/n_angles
    
    for i,angle in enumerate(range(angle_start, angle_stop+1, step)):
        results[i] = get_flow(angle, n_nodes, n_levels,
                              num_samples, visc, speed, time, run_id).delay()
    for i,angle in enumerate(range(angle_start, angle_stop+1, step)):
        results[i] = results[i].get()
    
    # TODO wait until all work is done
    # TODO give user link to swift folder
    # TODO "extra" give python script for download
    return 1
