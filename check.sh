#!/bin/sh
for challenge in $(ls)
do
  if [ -d $challenge ] && [ -f $challenge/INPUT.txt ] && [ -f $challenge/ANSWER.txt ] && [ -f $challenge/solution.py ]
  then
    result=$(cat $challenge/INPUT.txt | python3 $challenge/solution.py)
    expected=$(cat $challenge/ANSWER.txt)
    if [ ! "$result" = "$expected" ]
    then
      echo "Error: challenge $challenge -> result: $result, expected: $expected"
    fi
  fi
done