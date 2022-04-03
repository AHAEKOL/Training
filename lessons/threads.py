import threading
import time

balance = 0

def worker():
    global balance
    for x in range(1000000):
        balance += 1

THREADS = 10
threads = []

for x in range(THREADS):
    th = threading.Thread(target=worker)
    threads.append(th)
    th.start()

for th in threads:
    th.join()

print(f"The balance is: {balance} $")

