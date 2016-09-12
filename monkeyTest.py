# -*- coding: utf-8 -*-
__author__ = 'shikun'
import os
from BLL import BAdbCommon
from Common import OperateFile
from BLL import BMonkeyConfig
from Model import MMonkeyConfig
import re
from Common import Globals as go
from BLL import BphomeMsg
from Common import Cprint
def get_error(log):
    cp = Cprint.Color() # 在cmd中输出带颜色的命名
    with open(log, encoding="utf-8") as monkey_log:
        lines = monkey_log.readlines()
        for line in lines:
            if re.findall(go.ANR, line):
                # print('\033[1;31;42m')
                # print("存在anr错误:", line)
                cp.print_red_text("存在anr错误:"+ line)
                go.I_ANR += 1
            if re.findall(go.CRASH, line):
                # print('\033[1;31;42m')
                cp.print_red_text("存在crash错误:"+line)
                go.I_CRASH += 1
            if re.findall(go.EXCEPTION, line):
                # print('\033[1;31;42m')
                cp.print_red_text("存在exception异常:"+line)
                go.I_EXCEPTION += 1
        if go.I_ANR == 0 and go.I_CRASH == 0 and go.I_EXCEPTION == 0:
            cp.print_green_text("恭喜，没有任何错误")

 # 存手机信息
def get_phome(phonelog):
    bg = BphomeMsg.getPhone("log.txt").get_phone_Kernel()
    logname = phonelog + "_" + bg[0]["phone_model"] + bg[0]["phone_name"] + bg[0]["release"] + ".txt"
    of = OperateFile.base_file(logname, "w+")
    if of.mkdir_file():
        result = "手机型号：" + bg[0]["phone_name"] + "\n"
        result += "手机名字：" + bg[0]["phone_model"] + "\n"
        result += "系统版本：" + bg[0]["release"] + "\n"
        result += "手机分辨率：" + bg[3] + "\n"
        result += "手机运行内存：" + bg[1] + "\n"
        result += "CPU核数：" + bg[2] + "\n"
        of.write_txt(result)

#开始脚本测试
def start_monkey(cmd, logdir, now1):

    # Monkey测试结果日志:monkey_log
    os.popen(cmd )
    print(cmd)

    # Monkey时手机日志,logcat
    logcatname = logdir+"\\"+now1+r"logcat.log"
    cmd2 = "adb logcat -d >%s" %(logcatname)
    os.popen(cmd2)

if __name__ == '__main__':
    ini_file = 'monkey.ini'
    ba = BAdbCommon
    if OperateFile.base_file(ini_file, "r").check_file():
        if ba.attached_devices():
            mconfig = MMonkeyConfig.monkeyconfig()
            mc = BMonkeyConfig.monkeyConfig(mconfig, ini_file)
            # 打开想要的activity
            ba.open_app(mc.package_name, mc.activity)
            temp = ""
             # monkey开始测试
            start_monkey(mc.cmd, mc.logdir, mc.now)
            while True:
                with open(mc.monkey_log, encoding='utf-8') as monkeylog:
                    if monkeylog.read().count('Monkey finished') > 0:
                        print("测试完成咯")
                        get_error(mc.monkey_log)
                        get_phome(mc.phone_msg_log)
                        break
        else:
            print("设备不存在")
    else:
        print(u"配置文件不存在"+ini_file)

