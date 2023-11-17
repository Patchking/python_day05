import threading
import random
import time

class Doctor(threading.Thread):
    def __init__(self, id, left, right):
        threading.Thread.__init__(self)
        self.id = id
        self.left = left
        self.right = right

    def run(self):
        time.sleep(random.uniform(0.1, 1))
        with self.left:
            with self.right:
                print(f'Doctor {self.id}: BLAST!')

if __name__ == '__main__':
    tools = [threading.Lock() for _ in range(5)]

    r1 = range(9, 14)
    doctors = [Doctor(r1[i], tools[i], tools[(i + 1) % 5]) for i in range(5)]
    for doc in doctors:
        doc.start()

    for doctor in doctors:
        doctor.join()
