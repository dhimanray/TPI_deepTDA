#!/bin/bash
source source_libtorch.sh
source source_gromacs_cuda.sh

gmx_mpi grompp -f md.mdp -c prd.gro -p topol_01.top -o prd.tpr

export OMP_NUM_THREADS=2

mpiexec -n 1 gmx_mpi mdrun -deffnm prd -plumed plumed.dat -pin on -pinoffset 0
