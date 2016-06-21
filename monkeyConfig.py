# -*- coding: utf-8 -*-
__author__ = 'shikun'
import configparser
import time
class baseReadnin():
    def __init__(self, init_file):
        config = configparser.ConfigParser()
        config.read(init_file)
        self.cmd = config['DEFAULT']['cmd']
        self.package_name = config['DEFAULT']['package_name']
        self.logdir = config['DEFAULT']['logdir'] # 本机的log存放地址
        self.remote_path = config['DEFAULT']['remote_path'] #远程服务器地址，可以给开发查看
        self.phone_msg_log = config['DEFAULT']['phone_msg_log'] #临时存放手机日志信息路径
        self.now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        self.exceptions = config['DEFAULT']['exceptions'] #异常列表监控
        self.sum = config['DEFAULT']['sum']  #事件数量
        self.activity = config['DEFAULT']['activity']
    def get_cmd(self):
        return self.cmd + " "+ str(self.sum)+" >>"+ self.logdir + "\\" + self.now + "monkey.log"
    def get_log(self):
         return self.logdir + "\\" + self.now + "monkey.log"
    def get_package_name(self):
        return self.package_name
    def get_logdir(self):
        return self.logdir
    def get_remote_path(self):
        return self.remote_path
    def get_phone_msg_log(self):
        return self.phone_msg_log
    def get_monkey_logname(self):
        monkeylogname = self.logdir + "\\" + self.now + "monkey.log"
        return monkeylogname
    def get_logcatname(self): #抓取的logcat日志
        return self.logdir + "\\" + self.now + r"logcat.log"
    def get_now(self):
        return self.now
    def get_exceptions(self):
        return self.exceptions
    def get_sum(self):
        return int(self.sum)
    def get_activity(self):
        return self.activity
# if not os.path.isfile(self.file):
# t = baseReadnin(Base.getDir.BaseGetPreDir('conf.ini')).get_host()