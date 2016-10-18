from subprocess import call
from celery import Celery
import swiftclient
import os
## currently this file expects that airfoil, naca2gmsh and run.sh is in the same directoary

# Name of swift container
container_name = 'PotatisProject'

# Setup connection to swift client container
config = {'user':os.environ['OS_USERNAME'],
          'key':os.environ['OS_PASSWORD'],
          'tenant_name':os.environ['OS_TENANT_NAME'],
          'authurl':os.environ['OS_AUTH_URL']}
conn = swiftclient.Connection(auth_version=3, **config)

def mesh_gen_simple():
    call(["sudo","./run.sh", "0", "1", "2", "200", "0"])

def mesh_gen(start_angle, stop_angle, n_angles, n_nodes, n_ref_levels):
    call(["sudo","./run.sh", start_angle, stop_angle, n_angles, n_nodes, n_ref_levels])

def convert_msh_simple():
    call(["sudo","dolfin-convert", "./msh/r0a0n200.msh", "./test_mesh.xml"])

def convert_msh(input_msh, output_msh):
    call(["sudo","dolfin-convert", input_msh, output_msh])

def airfoil_run_simple():
    call(["sudo","./airfoil", "10", "0.0001", "10", "0.02", "./test_mesh.xml"])

def airfoil_run(n_samples, visc, vel, T, mesh):
    call(["sudo","./airfoil", n_samples, visc, vel, T, mesh])

app = Celery()
app.config_from_object('config')

@app.task
def get_flow(angle, n_nodes, n_ref_levels, n_samples, visc, vel, T, run_id):
    mesh_gen(angle, angle, "1", n_nodes, n_ref_levels)
    input_mesh = "./msh/r" + n_ref_levels + "a" + angle + "n" + n_nodes + ".msh"
    output_mesh = "./airfoil_msh/r" + n_ref_levels + "a" + angle + "n" + n_nodes + ".xml"
    convert_msh(input_mesh, output_mesh)
    airfoil_run(n_samples, visc, vel, T, output_mesh)
    ## save results to swift container
    for file_name in os.listdir("./results"):
        with open('./results/' + file_name, 'r') as current_file:
            conn.put_object(container_name, "Airfoil_" + run_id + "/" + os.path.basename(current_file.name), contents= current_file.read(), content_type='text/plain')
    ##
    return 1

@app.task
def get_flow_simple():
    mesh_gen_simple()
    convert_msh_simple()
    airfoil_run_simple()
