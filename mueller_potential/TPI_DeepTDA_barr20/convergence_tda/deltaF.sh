#!/bin/bash

rm deltaF.dat
touch deltaF.dat

./FES_from_Reweighting.py --colvar ../COLVAR --cv deepTDA.node-0 --kt 1 --sigma 0.05 --stride 4000 --deltaFat 0.0

for i in {1..100}
do
        sed -n '4s/.\{14\}//p' fes-rew_$i.dat >> deltaF.dat
done
