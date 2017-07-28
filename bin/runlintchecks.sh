#!/bin/sh

set -e

isort -rc -c labelstore tests || { echo "isort failed"; exit 1; }

flake8 labelstore tests
