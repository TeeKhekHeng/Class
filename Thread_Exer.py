import _thread as thread, time

def counter(myId, count):
    for j in range(count):
        time.sleep(1)
        print('[%s] => %s' % (myId, j))
    
for i in range(5):
    thread.start_new_thread(counter, (i,3))
    
time.sleep(6)
print('Main thread exiting. ')

