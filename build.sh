#!/bin/bash

python manage.py compilemessages

pylint ./alfredapi/*
