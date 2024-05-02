import threading
import time

class ControlledThread(threading.Thread):
    def __init__(self, name, num_times):
        super().__init__()
        self.name = name
        self.num_times = num_times
        self.stop_requested = False

    def run(self):
        for i in range(self.num_times):
            if self.stop_requested:
                break
            print(f"Hello {self.name}")
            time.sleep(1)  # Simulate work

    def stop(self):
        self.stop_requested = True

# Create two threads with specific names and iteration counts
thread1 = ControlledThread(name="Thread 1", num_times=5)
thread2 = ControlledThread(name="Thread 2", num_times=2)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

# Check if they need to be stopped, though they should have stopped already
if thread1.is_alive():
    thread1.stop()

if thread2.is_alive():
    thread2.stop()

print("Both threads have finished execution.")
