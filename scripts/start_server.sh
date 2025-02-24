#!/bin/bash
echo "Starting Flask application..."
cd /home/ec2-user/app
nohup gunicorn -w 4 -b 0.0.0.0:5000 app:app > app.log 2>&1 &
