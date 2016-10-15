import os
with open("/home/ubuntu/config.py","w") as f:
    f.write("BROKER_URL='amqp://ubuntu:group9@"+os.environ['LOCAL_IP']+":5672//'")
