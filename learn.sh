#!/bin/bash

rm results.csv
rm resultsDealer.csv
rm resultsRandom.csv
python game.py
python dgame.py
python rgame.py
python plotter.py
