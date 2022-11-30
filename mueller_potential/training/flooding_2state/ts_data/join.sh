#!/bin/bash

rm combined_ts.dat
touch combined_ts.dat
for i in {1..30}
do
        if [ $((i%2)) -eq 0 ]
        then
                cat data_$i >> combined_ts.dat
        else
                tac data_$i >> combined_ts.dat
        fi
done

