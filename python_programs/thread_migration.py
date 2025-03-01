from multiprocessing import Process
import time
import os

NUM_ITERATIONS = 1000

def task():
    for _ in range(NUM_ITERATIONS):
        pass

total_time = 0

for _ in range(10):
    process1 = Process(target=task)
    process2 = Process(target=task)
    start = time.perf_counter_ns()
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end = time.perf_counter_ns()
    total_time += (end - start)

with open("./results/python_thread_migration_results.txt", "w") as f:
    f.write(f"Average: {total_time / 10:.6f} ns\n")
