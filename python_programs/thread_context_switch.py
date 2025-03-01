import threading
import time

NUM_ITERATIONS = 1000

def worker():
    for _ in range(NUM_ITERATIONS):
        pass

total_time = 0

for _ in range(10):
    thread1 = threading.Thread(target=worker)
    thread2 = threading.Thread(target=worker)
    start = time.perf_counter_ns()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end = time.perf_counter_ns()
    total_time += (end - start)

with open("./results/python_thread_context_switch_results.txt", "w") as f:
    f.write(f"Average: {total_time / 10:.6f} ns\n")
