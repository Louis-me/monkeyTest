__author__ = 'Administrator'
import threading
import  time
class Bthread(threading.Thread):
    def __init__(self, func=None):
        threading.Thread.__init__(self)
        self.func = func
        #print(type(self.func))
    def run(self):
        self.func
