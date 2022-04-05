#!/opt/software/Python/3.8.6-GCCcore-10.2.0/bin/python3.8
import sys
from mpi4py import MPI

comm = MPI.COMM_WORLD
name=MPI.Get_processor_name()

comm.Barrier()
start = MPI.Wtime()

a = [0,1,2,3,4,5]
print(f"I am rank {comm.rank} and the list is {a}")

comm.Barrier()
end = MPI.Wtime()

if comm.rank == 0:
    deltatime = end-start
    print(f"The total run-time = {deltatime:.2e}")
    








