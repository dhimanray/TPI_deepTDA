#!/bin/bash
for i in {1..13}
do
	cp -r template run$i
	cd run$i
	j=$(( 2*$i + 12 ))
	sed -i "s/CORE/${j}/g" run_gromacs.sh
	./run_gromacs.sh &
	cd ..
done
