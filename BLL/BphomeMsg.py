__author__ = 'Administrator'
from DAL import DphoneMsg

class getPhone():
    def __init__(self, log):
        self.log = log
        self.gp = DphoneMsg.getPhone(self.log)

    def get_phone_Kernel(self):
        return self.gp.get_phone_Kernel()