#!/bin/bash
#SBATCH --job-name=runa
#SBATCH --output=runa-%j.out
#SBATCH --partition=general
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=20

###Load wanted modules here
module load Python/3.8.6-GCCcore-10.2.0

module load OpenMPI/4.0.5-GCC-10.2.0 

#place the base file name for your python code here
file=scatter_gather

mpirun -n 40 --mca mtl psm python $file.py > $file.out



