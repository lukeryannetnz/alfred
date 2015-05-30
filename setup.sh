#!/bin/bash

echo "Installing pylink..."
pip install pylint

echo "Installing gunicorn..."
pip install gunicorn

echo "Installing raspberry pi RPi.GPIO library..."
pip install RPi.GPIO

echo "Setup done"
