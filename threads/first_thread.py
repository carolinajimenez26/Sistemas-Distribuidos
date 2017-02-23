from threading import Thread
import threading

class MyThread(Thread):
    def add (self,a,b):
        return a + b

    def __init__(self,id):
        super(MyThread, self).__init__()
        self.id = id

    def run (self):
        #print ("2 + 3 = ", self.add(2,3))
        print ("I'm thread#", self.id)

n = 1
l = []
while (n <= 5):
    td = MyThread(n)
    td.start()
    l.append(td)
    n += 1

for td in l:
    td.join()

#print("Current threads: ", threading.enumerate())
#print ("Number of threads alive: ", threading.active_count())
