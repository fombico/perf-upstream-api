#!/bin/bash

pip install --upgrade pip
pip install -r /app/requirements.txt

gunicorn app:app -c /app/conf/gunicorn_conf.py --reload
