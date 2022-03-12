#!/bin/bash

filepath=$1

python3 -m frontend --filepath $filepath
./backend/main.sh $filepath
