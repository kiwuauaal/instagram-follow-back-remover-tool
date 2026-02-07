#!/bin/bash

echo "========================================"
echo "Instagram Analyzer - Demo/Test Run"
echo "========================================"
echo

echo "Running demo with sample data..."
echo

python3 instagram_analyzer.py -f sample_followers.json -w sample_following.json --show-all --save demo_results.txt

echo
echo "Demo complete! Check demo_results.txt for output."
echo