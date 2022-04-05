#!/opt/software/Python/3.8.6-GCCcore-10.2.0/bin/python3.8
import sys
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
name=MPI.Get_processor_name()

comm.Barrier()
start = MPI.Wtime()
N_cores = 80
N = N_cores*1000

A = np.arange(N, dtype=float)

summ = 0
for num in A:
    summ+= num
print(f"The grand total is {summ}")

comm.Barrier()
end = MPI.Wtime()

if comm.rank == 0:
    deltatime = end-start
    print(f"The total run-time = {deltatime:.2e}")
    








