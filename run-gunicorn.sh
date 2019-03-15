#!/bin/sh
. venv/bin/activate
gunicorn main:app
