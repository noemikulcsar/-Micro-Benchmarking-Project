import time
import threading

NUM_THREADS = 1000
total_time = 0

def dummy_function():
    pass

for _ in range(10):
    start = time.perf_counter()
    threads = [threading.Thread(target=dummy_function) for _ in range(NUM_THREADS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end = time.perf_counter()
    total_time += (end - start) * 1e9

with open("./results/python_thread_creation_results.txt", "w") as f:
    f.write(f"Average: {total_time / 10:.6f} ns\n")
