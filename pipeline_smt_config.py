# pipeline_smt_config.py

from m5.objects import *
from common import Options, Simulation

# Configure the pipeline with SMT enabled
class SMTConfig:
    def __init__(self, num_threads=2):
        self.num_threads = num_threads
        self.cpu = TimingSimpleCPU()
        self.cpu.numThreads = num_threads

    def run(self, program1, program2):
        # Assign different workloads to different threads
        self.cpu.workload = [program1, program2]
        root = Root(full_system=False, system=System(cpu=self.cpu, mem_mode='timing'))
        Simulation.run(root)

# Run simulation
if __name__ == "__main__":
    smt_config = SMTConfig(num_threads=2)
    smt_config.run(program1="int_benchmark", program2="fp_benchmark")
