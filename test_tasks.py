rom subprocess import call
## currently this file expects that airfoil, naca2gmsh and run.sh is in the same directoary

def mesh_gen_simple():
    call(["./run.sh", "0", "1", "2", "200", "0"])

def mesh_gen(start_angle, stop_angle, n_angles, n_nodes, n_ref_levels):
    call(["./run.sh", start_angle, stop_angle, n_angles, n_nodes, n_ref_levels])

def convert_msh_simple():
    call(["dolfin-convert", "./msh/r0a0n200.msh", "./test_mesh.xml"])

def convert_msh(input_msh, output_msh):
    call(["dolfin-convert", input_msh, output_msh])

def airfoil_run_simple():
    call(["./airfoil", "10", "0.0001", "10", "0.02", "./test_mesh.xml"])

def airfoil_run(n_samples, visc, vel, T, mesh):
    call(["./airfoil", n_samples, visc, vel, T, mesh])

def get_flow(angle, n_nodes, n_ref_levels, n_samples, visc, vel, T):
    mesh_gen(angle, angle, "1", n_nodes, n_ref_levels)
    input_mesh = "./msh/r" + n_ref_levels + "a" + angle + "n" + n_nodes + ".msh"
    output_mesh = "./airfoil_msh/r" + n_ref_levels + "a" + angle + "n" + n_nodes + ".xml"
    convert_msh(input_mesh, output_mesh)
    airfoil_run(n_samples, visc, vel, T, output_mesh)
    ## results folder
    return output_mesh
