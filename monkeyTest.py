# -*- coding: utf-8 -*-
import datetime
import time

import math
import xlsxwriter

__author__ = 'shikun'
import os
from Base import AdbCommon
from Base import OperateFile
from Base import BaseMonkeyConfig
import re
from Base import BaseCashEmnu as go
from Base import BasePhoneMsg
from Base import BaseReport
from Base import BaseMonitor
from Base import BaseAnalysis
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
workbook = xlsxwriter.Workbook('report.xlsx')
bo = BaseReport.OperateReport(workbook)

def get_error(log):
    crash = []
    with open(log, encoding="utf-8") as monkey_log:
        lines = monkey_log.readlines()
        for line in lines:
            if re.findall(go.ANR, line):
                print("存在anr错误:"+ line)
                crash.append(line)
            if re.findall(go.CRASH, line):
                print("存在crash错误:" + line)
                crash.append(line)
            if re.findall(go.EXCEPTION, line):
                print("存在crash错误:" + line)
                crash.append(line)
    if len(crash):
        worksheet2 = workbook.add_worksheet("异常日志")
        bo.crash(worksheet2, crash)

def report(app,sumTime):
    header = get_phome()
    worksheet1 = workbook.add_worksheet("性能监控")
    app["maxMen"] = BaseAnalysis.maxMen(BaseMonitor.men)
    app["avgMen"] = BaseAnalysis.avgMen(men=BaseMonitor.men, total=header["rom"])
    app["maxCpu"] = BaseAnalysis.maxCpu(BaseMonitor.cpu)
    app["avgCpu"] = BaseAnalysis.avgCpu(BaseMonitor.cpu)
    app["maxFps"] = BaseAnalysis.avgFps(BaseMonitor.fps)
    app["avgFps"] = BaseAnalysis.avgFps(BaseMonitor.fps)
    app["afterBattery"] = BaseMonitor.get_battery()
    _maxFlow = BaseAnalysis.maxFlow(BaseMonitor.flow)
    _avgFLow = BaseAnalysis.avgFlow(BaseMonitor.flow)
    app["maxFlowUp"] = _maxFlow[0]
    app["maxFlowDown"] = _maxFlow[1]
    app["avgFlowUp"] = _avgFLow[0]
    app["avgFlowDown"] = _avgFLow[1]
    header["time"] = sumTime
    header["net"] = app["net"]
    bo.monitor(worksheet=worksheet1, header=header, data=app)
    print("---monkey_log------")
    print(app["monkey_log"])
    get_error(log=app["monkey_log"])

    worksheet3 = workbook.add_worksheet("详细信息")
    app = {}
    app["cpu"] = BaseMonitor.cpu
    app["men"] = BaseMonitor.men
    app["flow"] = BaseMonitor.flow
    app["battery"] = BaseMonitor.battery
    app["fps"] = BaseMonitor.fps
    bo.analysis(worksheet3, app)
    bo.close()


    # 手机信息
def get_phome():
    bg = BasePhoneMsg.getPhone("log.txt").get_phone_Kernel()
    app = {}
    app["phone_name"] = bg[0]["phone_name"] + "_" + bg[0]["phone_model"]
    app["pix"] = bg[3]
    app["rom"] = bg[1]
    app["kel"] = bg[2]
    return app


#开始脚本测试
def start_monkey(cmd, log):

    # Monkey测试结果日志:monkey_log
    os.popen(cmd )
    print(cmd)

    # Monkey时手机日志,logcat
    logcatname = log + r"logcat.log"
    cmd2 = "adb logcat -d >%s" %(logcatname)
    os.popen(cmd2)

    #"导出traces文件"
    tracesname = log + r"traces.log"
    cmd3 = "adb shell cat /data/anr/traces.txt>%s" % tracesname
    os.popen(cmd3)
if __name__ == '__main__':
    ba = AdbCommon.AndroidDebugBridge()
    if ba.attached_devices():
        mc = BaseMonkeyConfig.monkeyConfig(PATH("monkey.ini"))
        # 打开想要的activity
        ba.open_app(mc["package_name"], mc["activity"])
        temp = ""
         # monkey开始测试
        start_monkey(mc["cmd"], mc["log"])
        time.sleep(1)
        starttime = datetime.datetime.now()
        pid = BaseMonitor.get_pid(mc["package_name"])
        cpu_kel = BaseMonitor.get_cpu_kel()
        while True:
            with open(mc["monkey_log"], encoding='utf-8') as monkeylog:
                BaseMonitor.cpu_rate(pid, cpu_kel)
                BaseMonitor.get_men(mc["package_name"])
                BaseMonitor.get_fps(mc["package_name"])
                BaseMonitor.get_battery()
                BaseMonitor.get_flow(pid, mc["net"])
                time.sleep(1) # 每1秒采集检查一次
                if monkeylog.read().count('Monkey finished') > 0:
                    endtime = datetime.datetime.now()
                    print("测试完成咯")
                    app = {"beforeBattery": BaseMonitor.get_battery(), "net": mc["net"], "monkey_log": mc["monkey_log"]}
                    report(app, str((endtime - starttime).seconds) + "秒")
                    # get_error(mc["monkey_log"])
                    # get_phome(mc.phone_msg_log)
                    break
    else:
        print("设备不存在")