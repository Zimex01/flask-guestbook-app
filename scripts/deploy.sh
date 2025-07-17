#!/bin/bash

docker build -t zimex01/flask-guestbook-app:latest .

eb init -p docker flask-guestbook-app --region eu-west-1
eb create flask-guestbook-env
eb deploy