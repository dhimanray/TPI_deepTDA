#!/bin/bash

for i in {1..13}
do
	cd run$i
	gmx_mpi trjconv -f prd.xtc -s prd.tpr -pbc whole -o prd_whole.xtc
	cd ..
done	
