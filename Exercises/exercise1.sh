#!/bin/bash

FIRST_STRING=$1
SECOND_STRING=$2
DIR=$3

for filename in $(ls -p -LR $DIR | grep -v / );
do
   if [[ $filename == *"$FIRST_STRING"* ]]; then
     NEW_NAME=`echo $filename | sed -e "s/${FIRST_STRING}/${SECOND_STRING}/g"`
     mv $DIR$filename $DIR$NEW_NAME
   fi;
done;
