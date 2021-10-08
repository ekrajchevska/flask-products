#!/bin/bash
# exit by default on all errors
set -e
gunicorn wsgi:app --bind 0.0.0.0:5000 --workers=1 --timeout 1000 