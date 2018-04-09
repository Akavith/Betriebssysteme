import threading

globalCounter = 0


class MyThread(threading.Thread):
    delta = 0

    def __init__(self, delta):
        threading.Thread.__init__(self)
        self.delta = delta

    def run(self):
        global globalCounter
        for i in range(0,1000):
            globalCounter += self.delta


threads = []

for i in range(0,5):
    threads.append(MyThread(1))
    threads[-1].start()

for i in range(0,5):
    threads.append(MyThread(-1))
    threads[-1].start()

for counter, thread in enumerate(threads):
    thread.join()
    print("Thread Nr. " + str(counter + 1) + " joined")

print(globalCounter)

