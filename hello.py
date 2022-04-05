#!/opt/software/Python/3.8.6-GCCcore-10.2.0/bin/python3.8
import sys
from mpi4py import MPI
print(f"Test - will this be printed by each process?")
comm = MPI.COMM_WORLD
name=MPI.Get_processor_name()
print(f"hello world -- from {name} and rank={comm.rank}")


