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

#开始脚本测试
def start_monkey(cmd, logdir, now1, monkey_log):
    print(cmd)
    os.popen(cmd)
    cmd2 = "adb logcat -d >%s" % monkey_log
    os.popen(cmd2)
    # logcatname=logdir+"\\"+now1+r"logcat.log"
    # cmd2="adb logcat -d >%s" %(logcatname)
    # os.popen(cmd2) 用于error的分析
    #print"导出traces文件"
    tracesname = logdir + "\\" + now1 + r"traces.log"
    cmd3 = "adb shell cat /data/anr/traces.txt>%s" % tracesname
    os.popen(cmd3)
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
            ml = MMatplo.matplo()
            bm = BMenCpu.get_men_cpu(mc.package_name)
            ml.cpu = [[], []]
            ml.men = [[], []]
            ml.title = ["cpu测试", "内存测试"]
            ml.locator = 2
            for i in range(mc.sum):
                time.sleep(1)
                dn = dt.datetime.now()
                ml.cpu[0].append(dn)
                cpu = bm.top_cpu()
                ml.men[0].append(dn)
                men = bm.get_men()
                with open(mc.monkey_log, encoding='utf-8') as monkeylog:
                    temp = monkeylog.read()
                if temp.count('Monkey finished') > 0:
                    print("测试完成咯")
                    ml.cpu[1].append(cpu)
                    ml.men[1].append(men)
                    BMatPlo.cpu_men_plots(ml)
                    break
        else:
            print("设备不存在")
    else:
        print(u"配置文件不存在"+ini_file)

