#!/bin/bash
echo "Installing dependencies..."
cd /home/ec2-user/web-app
pip install -r requirements.txt
chmod +x scripts/*.sh
