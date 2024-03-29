# http://docs.openstack.org/developer/python-novaclient/ref/v2/servers.html
import time, os, sys
import inspect
from os import environ as env

from  novaclient import client
import keystoneclient.v3.client as ksclient
from keystoneauth1 import loading
from keystoneauth1 import session


flavor = "c1.small" 
private_net = "g2015034-net_2"
floating_ip_pool_name = "public"
floating_ip = None
key = "proj_9"

loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(auth_url=env['OS_AUTH_URL'],
                                username=env['OS_USERNAME'],
                                password=env['OS_PASSWORD'],
                                project_name=env['OS_PROJECT_NAME'],
                                user_domain_name=env['OS_USER_DOMAIN_NAME'],
                                project_domain_name=env['OS_PROJECT_DOMAIN_NAME'])


sess = session.Session(auth=auth)
nova = client.Client('2.1', session=sess)
#print "user authorization completed."

image = nova.images.find(name="Group9Worker1.0")
flavor = nova.flavors.find(name=flavor)

if private_net != None:
    net = nova.networks.find(label=private_net)
    nics = [{'net-id': net.id}]
else:
    sys.exit("private-net not defined.")

    #takes input config file
cfg_file_path = sys.argv[1]
if os.path.isfile(cfg_file_path):
    userdata = open(cfg_file_path)
else:
    sys.exit("cloud-cfg.txt is not in current working directory")
            
secgroup = nova.security_groups.find(name="default")
secgroups = [secgroup.id]

if floating_ip_pool_name != None: 
    floating_ip = nova.floating_ips.create(floating_ip_pool_name)
else: 
    sys.exit("public ip pool name not defined.")
    
    
#print "Creating instance ... "                                                        
instance = nova.servers.create(name="group9worker", key_name=key, image=image, flavor=flavor, userdata=userdata, nics=nics,security_groups=secgroups)
#inst_status = instance.status
#print "waiting for 10 seconds.. "
time.sleep(10)

#while inst_status == 'BUILD':
    #print "Instance: "+instance.name+" is in "+inst_status+" state, sleeping for 5 seconds more..."
#    time.sleep(5)
instance = nova.servers.get(instance.id)
#    inst_status = instance.status
    
#print "Instance: "+ instance.name +" is in " + inst_status + "state"
        
#if floating_ip.ip != None: 
instance.add_floating_ip(floating_ip)
print floating_ip.ip
#print "Instance booted! Name: " + instance.name + " Status: " +instance.status+ ", floating IP attached " + floating_ip.ip

#else:
    #print "Instance booted! Name: " + instance.name + " Status: " +instance.status+ ", floating IP missing"

