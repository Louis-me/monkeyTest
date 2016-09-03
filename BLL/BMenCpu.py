__author__ = 'Administrator'
from DAL import DMenCpu
class get_men_cpu():
    def __init__(self, pkg_name):
        self.pkg_name = pkg_name
        self.dm = DMenCpu.get_cpu_men(self.pkg_name)
    def top_cpu(self):
       return self.dm.top_cpu()
    def get_men(self):
       return self.dm.get_men()
