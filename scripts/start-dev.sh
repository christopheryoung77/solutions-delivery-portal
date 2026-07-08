#!/bin/bash

cd /opt/sdp/solutions-delivery-portal

source ~/.venvs/atlas/bin/activate

echo "========================================="
echo " Atlas Development Environment"
echo "========================================="

python --version

git branch --show-current

echo

python run.py
