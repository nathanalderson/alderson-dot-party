#!/bin/sh
. venv/bin/activate
exec gunicorn main:app
