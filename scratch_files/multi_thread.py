import multiprocessing
import time

def function_a(finished_event):
    print("Process A started")
    for _ in range(10):
        print("Hello from Function A")
        time.sleep(1)  # Simulate some work and make output readable
    print("Process A finished")
    finished_event.set()  # Signal that the process has finished

def function_b(finished_event):
    print("Process B started")
    print("Hello from Function B")
    time.sleep(1)  # Simulate some work by sleeping for a short time
    print("Process B finished")
    finished_event.set()
if __name__ == '__main__':
    # Create an event to signal completion of Process A
    finished_event = multiprocessing.Event()

    # Create a process for each function
    process_a = multiprocessing.Process(target=function_a, args=(finished_event,))
    process_b = multiprocessing.Process(target=function_b, args=(finished_event,))

    # Start each process
    process_a.start()
    process_b.start()

    # Wait for the event to be set by Process A indicating it has finished
    finished_event.wait()

    # After the event is set, you could optionally terminate any process if needed
    # However, in this case, Process A should already be finished naturally.
    if process_b.is_alive():
        process_b.terminate()
        print("Process B was manually terminated after completion signal.")





    # if process_a.is_alive():
    #     process_a.terminate()
    #     print("Process A was manually terminated after completion signal.")

