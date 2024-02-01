import _thread, time

done = False

def worker(counter, i):
    while not done:
        time.sleep(1)
        input("Press enter")
        counter += 1
        print(counter)

_thread.start_new_thread(worker, (0, 1))

done = True