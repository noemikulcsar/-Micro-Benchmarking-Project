import time

NUM_ELEMENTS = 100000
total_time = 0

for _ in range(10):
    start = time.perf_counter()
    array = [i for i in range(NUM_ELEMENTS)]
    end = time.perf_counter()
    total_time += (end - start) * 1e9

with open("./results/python_static_allocation_results.txt", "w") as f:
    f.write(f"Average: {total_time / 10:.6f} ns\n")
