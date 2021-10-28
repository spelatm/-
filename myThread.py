import threading
from time import sleep
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.res = self.func(self.args)
        print(self.name, "finished!!!!!")

    def getResult(self):
        return self.res

def loop(nsec ):
    sleep(nsec)

def main():
    t = MyThread(loop, 5, loop.__name__)
    t.start()
    t.join()
    print("over!!")

if __name__ == '__main__':
    main()
