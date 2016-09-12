# -*- coding: utf-8 -*-
__author__ = 'shikun'
import os
import time
import datetime as dt
from BLL import BMatPlo
from BLL import BAdbCommon
from Common import OperateFile
from BLL import BMonkeyConfig
from Model import MMonkeyConfig
from Model import MMatplo
from BLL import BMenCpu
import re
from Common import Globals as go


def get_error(log):
    with open(log, encoding="utf-8") as monkey_log:
        lines = monkey_log.readlines()
        for line in lines:
            if re.findall(go.ANR, line):
                print('\033[1;31;42m')
                print("存在anr错误:", line)
                go.I_ANR += 1
            if re.findall(go.CRASH, line):
                print('\033[1;31;42m')
                print("存在crash错误:", line)
                go.I_CRASH += 1
            if re.findall(go.EXCEPTION, line):
                print('\033[1;31;42m')
                print("存在exception异常:", line)
                go.I_EXCEPTION += 1



#开始脚本测试
def start_monkey(cmd, logdir, now1, monkey_log):
    # Monkey测试结果日志:monkey_log
    os.popen(cmd )
    print(cmd)

    # Monkey时手机日志
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
            start_monkey(mc.cmd, mc.logdir, mc.now, mc.monkey_log)

            # cpu,men统计
            # ml = MMatplo.matplo()
            # bm = BMenCpu.get_men_cpu(mc.package_name)
            # ml.cpu = [[], []]
            # ml.men = [[], []]
            # ml.title = ["cpu测试", "内存测试"]
            # ml.locator = 2
            for i in range(mc.sum):
                time.sleep(0.5)
                dn = dt.datetime.now()
                # ml.cpu[0].append(dn)
                # cpu = bm.top_cpu()
                # ml.men[0].append(dn)
                # men = bm.get_men()
                with open(mc.monkey_log, encoding='utf-8') as monkeylog:
                    temp = monkeylog.read()
                if temp.count('Monkey finished') > 0:
                    print("测试完成咯")
                    # ml.cpu[1].append(cpu)
                    # ml.men[1].append(men)
                    # BMatPlo.cpu_men_plots(ml)
                    get_error(mc.monkey_log)
                    break
            # get_error(mc.monkey_log)
        else:
            print("设备不存在")
    else:
        print(u"配置文件不存在"+ini_file)

