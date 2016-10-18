#!/bin/bash

FLOATING_IP=$(python $HOME/cloud-airfoil/create_worker.py $HOME/cloud-airfoil/worker-cfg.txt)
sleep 20
scp -o "StrictHostKeyChecking no" -i $HOME/cloud-airfoil/proj.key $HOME/config.py ubuntu@$FLOATING_IP:~
ssh -t -i $HOME/cloud-airfoil/proj.key ubuntu@$FLOATING_IP <<-"ENDSSH"
mv proj.key .ssh/id_rsa
sudo chmod 600 .ssh/id_rsa
git clone git@github.com:vertan/cloud-airfoil.git
screen -d -m celery -A tasks worker --loglevel=info
screen -d -m celery -A tasks worker --loglevel=info
ENDSSH
