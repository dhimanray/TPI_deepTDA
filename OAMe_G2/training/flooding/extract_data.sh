#!/bin/bash

for i in {1..13}
do
	cd run$i
	cp ../template/plumed_data.dat .
	plumed driver --ixtc prd_whole.xtc --plumed plumed_data.dat
	cd ..
done
