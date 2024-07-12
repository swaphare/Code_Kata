#!/bin/sh
set -e

# Generate the fixed-width file
python generate_fixed_width.py

# Parse the fixed-width file to CSV
python parse_fixed_width.py

exec "$@"
