__author__ = 'shikun'
# -*- coding: utf-8 -*-
import subprocess
pkg_name = "com.dgm.user"
cpu = []
men = []
def top_cpu(pkg_name):
    print("------------------------")
    cmd = "adb shell dumpsys cpuinfo | grep " + pkg_name
    temp = []
    # print(cmd)
    # cmd = "adb shell top -n %s -s cpu | grep %s$" %(str(times), pkg_name)
    top_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    for info in top_info:
        temp.append(info.split()[2].decode()) # bytes转换为string
        # print("cpu占用:%s" %cpu)
    for i in temp:
         if i != "0%":
            cpu.append(i.split("%")[0])
    return cpu

def get_men(pkg_name):
    cmd = "adb shell  dumpsys  meminfo %s"  %(pkg_name)
    print(cmd)
    temp = []
    m = []
    men_s = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    for info in men_s:
        temp.append(info.split())
        # print("内存占用:%s" %men[19][1].decode()+"K")
    m.append(temp)
    for t in m:
        men.append(t[19][1].decode())
    return men
