__author__ = 'Administrator'
import os
import utils
import psutil

# 取到流量后可以用步骤后的流量减去步骤前的流量得到步骤消耗流量！也可以用时间差来计算！

def getFlow():
    pid = utils.get_app_pid("com.fanbeiwang")
    flow_info = os.popen("adb shell cat /proc/"+pid+"/net/dev").readlines()
    t = []
    for info in flow_info:
        temp_list = info.split()
        t.append(temp_list)
    print(t[16][1]) #总的接受流量
    print(t[16][9]) #总的发送流量

getFlow()