#!/bin/bash

# TODO Dockerfile amazonlinux:2018.03

DIR="$(dirname ${BASH_SOURCE[0]})"
# echo "Script directory is $DIR"
# echo "Changing to grandparent"
cd $DIR/../../
#NEWDIR=`pwd`
# echo "Changed to directory $NEWDIR"
rm -rf build || true
mkdir build
cp -R app/ build
find build -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
pip install -r app/requirements.txt --target build
cd build
chmod -R 755 .
zip -r ../myDeploymentPackage.zip .