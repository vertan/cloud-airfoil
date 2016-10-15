from test_tasks import get_flow

def get_flow_result(angle_start, angle_stop, n_angles, n_nodes,
                    n_levels, num_samples, visc, speed, time):

    results = []
    step = (angle_stop-angle_start)/n_angles
    
    for i,angle in enumerate(range(angle_start, angle_stop+1, step)):
        results[i] = get_flow(angle, n_nodes, n_levels,
                              num_samples, visc, speed, time).delay()
    for i,angle in enumerate(range(angle_start, angle_stop+1, step)):
        results[i] = results[i].get()

    # TODO Put all results in same folder
    # TODO Zip the folder
    # TODO Return the file or link to
    return results
