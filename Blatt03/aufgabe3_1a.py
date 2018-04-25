import signal
import os
import time


def receive_signal(signum, stack):
    print("Received:", signum)


#   for i in range(1, 32):
#       if i != 9 and i != 19:
#           signal.signal(i, receive_signal)

signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)
signal.signal(signal.SIGALRM, receive_signal)
signal.signal(signal.SIGTSTP, signal.SIG_IGN)


print('My PID is:', os.getpid())
while True:
    print('Waiting...')
    time.sleep(3)
