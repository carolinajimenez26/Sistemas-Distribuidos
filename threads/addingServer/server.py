from threading import Thread
import threading
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer as Server

class MyThread(Thread):
    def __init__(self,n1,n2):
        super(MyThread, self).__init__()
        self.n1 = n1
        self.n2 = n2

    def rangeAdd (self):
        ans = 0
        for i in range(self.n1,self.n2):
            ans += i

        return ans

def addThreads(x): #suma numeros desde el 1 hasta x
    n = 0
    l = []
    ans = []
    number = 1
    threads_required = 5 # especificados por el profesor, puede cambiar

    while (n < threads_required):
        td = MyThread(number,number+(x/threads_required))
        td.start()
        l.append(td)
        n += 1
        number += (x/threads_required)

    for td in l:
        td.join()
        ans.append(td.rangeAdd())

    return sum(ans)

port = 8080
server = Server(('localhost',port))
print ('Listening on port ', port)
#server.register_instance(MyThread())
server.register_function(addThreads)
server.serve_forever()
