#!/bin/bash

cd boot2sol

mkdir -p ../check

git reset --hard origin/master
git log --format="%H" > ../check/commits


while read p; do
  echo $p
done < ../check/commits
