import multiprocessing
import time

def function_a():
    print("Process A started")
    for _ in range(10):
        print("Hello from Function A")
        time.sleep(1)  # Simulate some work and make output readable
    print("Process A finished")

def function_b():
    print("Process B started")
    print("Hello from Function B")
    time.sleep(1)  # Simulate some work by sleeping for a short time
    print("Process B finished")

if __name__ == '__main__':
    # Create a process for each function
    process_a = multiprocessing.Process(target=function_a)
    process_b = multiprocessing.Process(target=function_b)

    # Start each process
    process_a.start()
    process_b.start()

    # Do not call join() to let them run independently
