import os

def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    numbers = [2, 4, 6, 8, 10]
    print(f"Parent process (PID {os.getpid()}): Generating numbers: {numbers}")
    pid = os.fork()
    if pid == 0: # Child process
        print(f"Child process (PID {os.getpid()}): Calculating sum...")
        total_sum = sum_numbers(numbers)
        print(f"Child process (PID {os.getpid()}): Sum of numbers: {total_sum}")
    else: # Parent process
        print(f"Parent process (PID {os.getpid()}): Waiting for child process to finish....")
        os.waitpid(pid, 0) # Wait for the child process to complete
        print(f"Parent process (PID {os.getpid()}): Child process finished.")
        print(f"Parent process (PID {os.getpid()}): Sum of numbers calculated by child process: {numbers}")

if __name__ == "__main__":
    main()

"""
Parent process (PID <parent_PID>): Generating numbers: [2, 4, 6, 8, 10]
Parent process (PID <parent_PID>): Waiting for child process to finish....
Child process (PID <child_PID>): Calculating sum...
Child process (PID <child_PID>): Sum of numbers: 30
Parent process (PID <parent_PID>): Child process finished.
Parent process (PID <parent_PID>): Sum of numbers calculated by child process: [2, 4, 6, 8, 10]
"""
