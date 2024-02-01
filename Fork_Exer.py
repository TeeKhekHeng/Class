"""Parent process creates a list of numbers, and the child process modifies the list by squaring each number. 
   This utilizes a shared list between the parent and child processes. """

import os

def add_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] + 1
    return numbers

def multiply_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] *2
    return numbers

def main():
    numbers = [1,2,3,4,5]
    print(f"Parent process (PID {os.getpid()}): Original numbers:{numbers}")

    pid = os.fork()

    if pid ==0: # Child process
        print(f"Child process (PID{os.getpid()}): Squaring numbers...")
        add_numbers(numbers)
        print(f"Child process (PID{os.getpid()}): Modified numbers:{numbers}")
    else: # Parent process
        os.waitpid(pid, 0) # wait for the child process to complete
        print(f"Parent process (PID{os.getpid()}): Child process finished.")
        multiply_numbers(numbers)
        print(f"Parent process (PID{os.getpid()}): Modified numbers by child process: {numbers}")

if __name__ == "__main__":
    main()
