#!/bin/bash

#source source_libtorch.sh
#source source_gromacs_cuda.sh

for i in {1..20}
#for i in 1
do
	cp -r template run$i
	cd run$i
	
	j=$(( 2*$i-2 ))

	gmx_mpi grompp -f md.mdp -c prd.gro -p topol_01.top -o prd.tpr

	export OMP_NUM_THREADS=1

	if [ $i -gt 10 ]
	then
		g=0
	else
		g=1
	fi
	
	mpiexec -n 1 gmx_mpi mdrun -deffnm prd -plumed plumed_rate.dat -pin on -pinoffset $j -gpu_id $g &

	#python3 rescale_time.py
	
	cd ..

done
