__author__ = 'Administrator'
import os
import re
import math
class getPhone():
    def __init__(self, cmd_log) :
        self.cmd_log = cmd_log
    def getModel(self):
        os.system('adb shell cat /system/build.prop >'+self.cmd_log)
        l_list = {}
        with open(self.cmd_log, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.split('=')
                #Android 系统，如anroid 4.0
                if (line[0] == 'ro.build.version.release'):
                    l_list["release"] = line[1].replace("\n", " ")
                    #手机名字
                if (line[0]=='ro.product.model'):
                    l_list["phone_name"] = line[1].replace("\n", " ")
                    #手机品牌
                if (line[0]=='ro.product.brand'):
                     l_list["phone_model"] = line[1].replace("\n", " ")

        # 删除本地存储的手机信息文件
        if os.path.exists(self.cmd_log):
            os.remove(self.cmd_log)
        return l_list

    def get_men_total(self):
        os.system("adb shell cat /proc/meminfo >" + self.cmd_log)
        men_total = ""
        with open(self.cmd_log, "r") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.split('=')
                    if line[0]:
                        men_total = re.findall(r"\d+", line[0])[0]
                        break
        if os.path.exists(self.cmd_log):
            os.remove(self.cmd_log)
        # return  str(math.ceil(int(men_total)/1024)) + "M"
        return int(men_total)
    # 得到几核cpu
    def get_cpu_kel(self):
        os.system("adb shell cat /proc/cpuinfo >" + self.cmd_log)
        cpu_kel = 0
        with open(self.cmd_log, "r") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.split(':')
                    if line[0].find("processor") >= 0:
                       cpu_kel += 1
        if os.path.exists(self.cmd_log):
            os.remove(self.cmd_log)
        return str(cpu_kel) + "核"
    # print(get_cpu_kel("d:\\men.txt"))

    # 得到手机分辨率
    def get_app_pix(self):
        result = os.popen("adb shell wm size", "r")
        return result.readline().split("Physical size:")[1]

    def get_phone_Kernel(self):
        pix = self.get_app_pix()
        men_total = self.get_men_total()
        phone_msg = self.getModel()
        cpu_sum = self.get_cpu_kel()
        return phone_msg, men_total, cpu_sum, pix