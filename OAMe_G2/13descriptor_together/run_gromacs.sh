#!/bin/bash

source source_libtorch.sh
source source_gromacs_cuda.sh

gmx_mpi grompp -f NVT.mdp -c b.gro -p topol.top -o prd.tpr

export OMP_NUM_THREADS=1

mpiexec -n 1 gmx_mpi mdrun -deffnm prd -nsteps 100000000 -plumed plumed.dat -pin on -pinoffset 6
