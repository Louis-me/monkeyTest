# -*- coding: utf-8 -*-
__author__ = 'shikun'
import os
import time
import re
import monkeyConfig
from adb_common import AndroidDebugBridge as ai
import matplotlibBase as mt
import MenCpu as m
import datetime as dt
CPU = [[],[]] # time,使用情况
MEN = [[],[]] #当前时间，和内存使用情况
C0 = []
C1 = []
M0 = []
M1 = []
# 得到手机信息
def getPhoneMsg(cmd_log):
    l_list = []
    f = open(cmd_log, "r")
    lines = f.readlines()
    for line in lines:
        line = line.split('=')
        #Android 系统，如anroid 4.0
        if (line[0] == 'ro.build.version.release'):
            l_list.append(line[1])
            #手机名字
        if (line[0]=='ro.product.model'):
            l_list.append(line[1])
            #手机品牌
        if (line[0]=='ro.product.brand'):
            l_list.append(line[1])
    f.close()
    return l_list

#开始脚本测试
def start_monkey(cmd, logdir, now1, logcatname):
    print(cmd)
    os.popen(cmd)
    # os.kill()
    #print"使用Logcat导出日志"
    cmd2 = "adb logcat -d >%s" % logcatname
    os.popen(cmd2)
    #print"导出traces文件"
    tracesname = logdir + "\\" + now1 + r"traces.log"
    cmd3 = "adb shell cat /data/anr/traces.txt>%s" % tracesname
    os.popen(cmd3)

#获取error,
# logcatname,mote_pah(服务器存储地址)t
# log_list:version,model,brand
######################
def geterror(log_list, logcatname, remote_path, now1):
    # 这里的错误异常可以写到配置文件中
    NullPointer = "java.lang.NullPointerException"
    NullPointer_count = 0
    IllegalState = "java.lang.IllegalStateException"
    IllegalState_count = 0
    IllegalArgument = "java.lang.IllegalArgumentException"
    IllegalArgument_count = 0
    ArrayIndexOutOfBounds = "java.lang.ArrayIndexOutOfBoundsException"
    ArrayIndexOutOfBounds_count = 0
    RuntimeException = "java.lang.RuntimeException"
    RuntimeException_count = 0
    SecurityException = "java.lang.SecurityException"
    SecurityException_count = 0
    f = open(logcatname, "r")
    lines = f.readlines()
    errfile = "%s\error.log" % remote_path
    if os.path.exists(errfile):
        os.remove(errfile)
    fr = open(errfile, "a")
    fr.write(log_list[0])
    fr.write("\n")
    fr.write(log_list[1])
    fr.write("\n")
    fr.write(log_list[2])
    fr.write("\n")
    fr.write(now1)
    fr.write("\n")
    count = 0
    for line in lines:
        if re.findall(NullPointer, line):
            NullPointer_count += 1
        if re.findall(IllegalState, line):
            IllegalState_count += 1
        if re.findall(IllegalArgument, line):
            IllegalArgument_count += 1
        if re.findall(ArrayIndexOutOfBounds, line):
            ArrayIndexOutOfBounds_count += 1
        if re.findall(RuntimeException, line):
            RuntimeException_count += 1
        if re.findall(SecurityException, line):
            SecurityException_count += 1

         # 这里的日志文件放到服务器去
        if re.findall(NullPointer, line) or re.findall(IllegalState, line) or re.findall(IllegalArgument, line) or \
                re.findall(ArrayIndexOutOfBounds, line) or re.findall(RuntimeException, line) or re.findall(SecurityException, line):
            count += 1
            a = lines.index(line)
            for var in range(a, a+22):
                # 这个22是表示从找到某个出错的信息开始，打印log22行，这个数据你可以根据自己的需要改。基本上22行能把所有的出错有关的log展现出来了。
                print(lines[var])
                fr.write(lines[var])
            fr.write("\n")
    f.close()
    fr.close()
     # #柱形
    if count > 0:
        list_arg = [[NullPointer_count, IllegalState_count, IllegalArgument_count, ArrayIndexOutOfBounds_count],
                    ['空指针', '类型转换', '参数异常', '数组越界']]
        matplotlibBase.mat_bar(list_arg)
        pass
    else:
        print(u"没有任何异常")

if __name__ == '__main__':
    ini_file = 'monkey.ini'
    if os.path.isfile(ini_file):
        if ai().attached_devices():

            mc = monkeyConfig.baseReadnin(ini_file)
            ai().open_app(mc.get_package_name(), mc.get_activity())
            os.system('adb shell cat /system/build.prop >'+mc.get_phone_msg_log()) #存放的手机信息
            ll_list = getPhoneMsg(mc.get_phone_msg_log())
            # monkey开始测试
            sum = mc.get_sum()
            temp = ""
            monkeylog = ""
            start_monkey(mc.get_cmd(), mc.get_logdir(), mc.get_now(), mc.get_logcatname())
            for i in range(sum):
                time.sleep(1)
                print(i)
                dn = dt.datetime.now()
                CPU[0].append(dn)
                m.top_cpu(mc.get_package_name())
                # CPU[1].append(m.top_cpu(mc.get_package_name()))
                MEN[0].append(dn)
                m.get_men(mc.get_package_name())
                # MEN[1].append(m.get_men(mc.get_package_name()))
                monkeylog = open(mc.get_logdir() + "\\" + mc.get_now()+"monkey.log")
                temp = monkeylog.read()
                monkeylog.close()
                if temp.count('Monkey finished')>0:
                    print("测试完成咯")
                    CPU[1].append(m.cpu)
                    MEN[1].append(m.men)
                    # geterror(ll_list, mc.get_log(), mc.get_remote_path(), mc.now)
                    mt.cpu_men_plots(CPU, MEN)
                    break

        else:
            print("设备不存在")
    else:
        print(u"配置文件不存在"+ini_file)

