
#find out local ip
#ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'

ip = '192.168.0.229'
BROKER_URL = 'amqp://ubuntu:group9@'+ip+':5672//'
