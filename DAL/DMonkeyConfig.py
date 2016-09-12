__author__ = 'Administrator'
import configparser
import time
def monkeyConfig(mmonkeyconfig, init_file):
    config = configparser.ConfigParser()
    config.read(init_file)
    mmonkeyconfig.package_name = config['DEFAULT']['package_name']
    mmonkeyconfig.logdir = config['DEFAULT']['logdir']
    mmonkeyconfig.remote_path = config['DEFAULT']['remote_path']
    mmonkeyconfig.now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    mmonkeyconfig.activity = config['DEFAULT']['activity']
    mmonkeyconfig.sum = int(config['DEFAULT']['sum'])
    mmonkeyconfig.monkey_log = mmonkeyconfig.logdir + "\\" + mmonkeyconfig.now + r"monkey.log"
    mmonkeyconfig.cmd = config['DEFAULT']['cmd'] + " " + str(mmonkeyconfig.sum) + ">>" + mmonkeyconfig.monkey_log
    mmonkeyconfig.phone_msg_log = mmonkeyconfig.logdir + "\\"
    return mmonkeyconfig
