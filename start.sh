#!/bin/bash

gunicorn -w 4 'main:app'
