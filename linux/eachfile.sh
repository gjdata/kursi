#!/bin/bash
FILES=./crypto/*
for f in $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  sed -e 's/$/"$f"/' -i $f
done



