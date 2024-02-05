import os

def square_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2

def main():
    numbers = [1, 2, 3, 4, 5]
    print(f"Parent process (PID {os.getpid()}): Original numbers: {numbers}")
    pid = os.fork()
    if pid == 0: # Child process
        print(f"Child process (PID {os.getpid()}): Squaring numbers...")
        square_numbers(numbers)
        print(f"Child process (PID {os.getpid()}): Modified numbers: {numbers}")
    else: # Parent process
        os.waitpid(pid, 0) # Wait for the child process to complete
        print(f"Parent process (PID {os.getpid()}): Child process finished.")
        print(f"Parent process (PID {os.getpid()}): Modified numbers by child process: {numbers}")

if __name__ == "__main__":
    main()

"""
Parent process (PID <parent_PID>): Original numbers: [1, 2, 3, 4, 5]
Child process (PID <child_PID>): Squaring numbers...
Child process (PID <child_PID>): Modified numbers: [1, 4, 9, 16, 25]
Parent process (PID <parent_PID>): Child process finished.
Parent process (PID <parent_PID>): Modified numbers by child process: [1, 4, 9, 16, 25]
"""