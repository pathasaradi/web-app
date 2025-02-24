#!/bin/bash
echo "Stopping existing Flask application..."
pkill -f "gunicorn" || pkill -f "flask"
