__author__ = 'Administrator'
import configparser
import time
def monkeyConfig(mmonkeyconfig, init_file):
    config = configparser.ConfigParser()
    config.read(init_file)
    mmonkeyconfig.package_name = config['DEFAULT']['package_name']
    mmonkeyconfig.logdir = config['DEFAULT']['logdir']
    mmonkeyconfig.remote_path = config['DEFAULT']['remote_path']
    mmonkeyconfig.phone_msg_log = config['DEFAULT']['phone_msg_log']
    mmonkeyconfig.now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    mmonkeyconfig.activity = config['DEFAULT']['activity']
    mmonkeyconfig.sum = int(config['DEFAULT']['sum'])
    mmonkeyconfig.monkey_log = mmonkeyconfig.logdir + "\\" + mmonkeyconfig.now + r"monkey.log"
    mmonkeyconfig.cmd = config['DEFAULT']['cmd'] + " " + str(mmonkeyconfig.sum) + ">>" + mmonkeyconfig.monkey_log
    return mmonkeyconfig
        #     self.cmd = config['DEFAULT']['cmd']
        # self.package_name = config['DEFAULT']['package_name']
        # self.logdir = config['DEFAULT']['logdir'] # 本机的log存放地址
        # self.remote_path = config['DEFAULT']['remote_path'] #远程服务器地址，可以给开发查看
        # self.phone_msg_log = config['DEFAULT']['phone_msg_log'] #临时存放手机日志信息路径
        # self.now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        # self.exceptions = config['DEFAULT']['exceptions'] #异常列表监控
        # self.sum = config['DEFAULT']['sum']  #事件数量
        # self.activity = config['DEFAULT']['activity']