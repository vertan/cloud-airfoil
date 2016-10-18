#!/bin/bash

FLOATING_IP=$(python ~/create_worker.py)
sleep 30
scp -o "StrictHostKeyChecking no" -i ~/proj.key ~/config.py ubuntu@$FLOATING_IP:~
ssh -t -i ~/proj.key ubuntu@$FLOATING_IP <<-"ENDSSH"
mv proj.key .ssh/id_rsa
git clone git@github.com:vertan/cloud-airfoil.git
screen -d -m celery -A tasks worker --loglevel=info
screen -d -m celery -A tasks worker --loglevel=info
ENDSSH
