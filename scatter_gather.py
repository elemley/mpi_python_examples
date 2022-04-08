#!/opt/software/Python/3.8.6-GCCcore-10.2.0/bin/python3.8
import sys
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
name=MPI.Get_processor_name()

comm.Barrier()
start = MPI.Wtime()
N_cores = 100
N = N_cores*2000
N_per_core = N // N_cores

if comm.rank == 0:
    A = np.arange(N, dtype=float)
else:
    A = np.empty(N, dtype=float)

my_A = np.empty(N_per_core, dtype=float)
sub_sums = np.empty(N_cores, dtype=float)

comm.Scatter([A,MPI.DOUBLE], [my_A,MPI.DOUBLE])

summ = 0
for num in my_A:
    summ+= num
#print(f"{comm.rank} summed up it's portion of the vector to {summ}")

comm.Gather([summ,MPI.DOUBLE],[sub_sums,MPI.DOUBLE])


if comm.rank == 0:
    big_summ = 0
    for num in sub_sums:
        big_summ+=num
    print(f"The grand total is {big_summ}")

comm.Barrier()
end = MPI.Wtime()

if comm.rank == 0:
    deltatime = end-start
    print(f"The total run-time = {deltatime:.2e}")
    








