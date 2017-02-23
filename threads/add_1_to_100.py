from threading import Thread
import threading

class MyThread(Thread):
    def __init__(self,n1,n2):
        super(MyThread, self).__init__()
        self.n1 = n1
        self.n2 = n2

    def add (self):
        ans = 0
        for i in range(self.n1,self.n2):
            ans += i

        return ans

    def run (self):
        ans = 0
        for i in range(self.n1,self.n2):
            ans += i

        print ("Cuenta del " + str(self.n1) + " hasta el " + str(self.n2) + " es : " + str(ans))

n = 0
l = []
ans = []
number = 1

while (n < 5):
    td = MyThread(number,number+19)
    td.start()
    l.append(td)
    n += 1
    number += 20

for td in l:
    td.join()
    ans.append(td.add())

print ("ans: ", ans)
print ("The sum is:", sum(ans))
