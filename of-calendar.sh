#!/bin/bash

python src/main.py -i tests/sample-in.txt -t csv
python src/main.py -i tests/sample-in.txt -t csv -o tests/sample-out.csv

