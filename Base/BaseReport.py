import math
import re

import xlsxwriter

from Base import BaseAnalysis,  BaseCashEmnu as go
from Base.BasePickle import readInfo


class OperateReport:
    def __init__(self, wd):
        self.wd = wd
        self._crashM = []
        # self.pie(self.wd, worksheet)

    def monitor(self, info):
        worksheet = self.wd.add_worksheet("Analysis")
        worksheet.set_column("A:A", 15)
        worksheet.set_column("B:B", 10)
        worksheet.set_column("C:C", 10)
        worksheet.set_column("D:D", 10)
        worksheet.set_column("E:E", 10)
        worksheet.set_column("F:F", 10)
        worksheet.set_column("G:G", 10)
        worksheet.set_column("H:H", 10)
        worksheet.set_column("I:I", 10)
        worksheet.set_column("J:J", 10)
        worksheet.set_column("K:K", 10)
        worksheet.set_column("L:L", 10)
        worksheet.set_column("L:L", 10)
        worksheet.set_column("M:M", 10)
        worksheet.set_column("N:N", 10)
        worksheet.set_column("O:O", 10)
        worksheet.set_column("P:P", 10)
        worksheet.set_column("Q:Q", 10)
        worksheet.set_column("R:R", 10)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)
        worksheet.set_row(6, 30)
        worksheet.set_row(7, 30)
        worksheet.set_row(8, 30)
        worksheet.set_row(9, 30)
        worksheet.set_row(10, 30)
        worksheet.set_row(11, 30)
        worksheet.set_row(12, 30)

        define_format_H1 = get_format(self.wd, {'bold': True, 'font_size': 18})
        define_format_H2 = get_format(self.wd, {'bold': True, 'font_size': 14})
        define_format_H1.set_border(1)

        define_format_H2.set_border(1)
        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("blue")
        define_format_H2.set_color("#ffffff")
        worksheet.merge_range('A1:L1', 'monkey性能监控', define_format_H1)
        _write_center(worksheet, "A2", '设备名', self.wd)
        _write_center(worksheet, "B2", 'CPU', self.wd)
        _write_center(worksheet, "C2", '内存', self.wd)
        _write_center(worksheet, "D2", '分辨率', self.wd)
        _write_center(worksheet, "E2", '网络', self.wd)
        _write_center(worksheet, "F2", "耗时", self.wd)
        _write_center(worksheet, "G2", "CPU峰值", self.wd)
        _write_center(worksheet, "H2", "CPU均值", self.wd)
        _write_center(worksheet, "I2", "内存峰值", self.wd)
        _write_center(worksheet, "J2", "内存均值", self.wd)
        _write_center(worksheet, "K2", "fps峰值", self.wd)
        _write_center(worksheet, "L2", "fps均值", self.wd)
        _write_center(worksheet, "M2", "电量测试之前", self.wd)
        _write_center(worksheet, "N2", "电量测试之后", self.wd)
        _write_center(worksheet, "O2", "上行流量峰值", self.wd)
        _write_center(worksheet, "P2", "上行流量均值", self.wd)
        _write_center(worksheet, "Q2", "下行流量峰值", self.wd)
        _write_center(worksheet, "R2", "下行流量均值", self.wd)


        temp = 3
        for t in info:
            for wrap in t:
                for item in t[wrap]:
                    self.getCrashMsg(t[wrap]["header"]["monkey_log"])
                    _write_center(worksheet, "A" + str(temp), t[wrap]["header"]["phone_name"], self.wd)
                    _write_center(worksheet, "B" + str(temp), t[wrap]["header"]["kel"], self.wd)
                    _write_center(worksheet, "C" + str(temp), str(math.ceil(t[wrap]["header"]["rom"] / 1024)) + "M", self.wd)
                    _write_center(worksheet, "D" + str(temp), t[wrap]["header"]["pix"], self.wd)
                    _write_center(worksheet, "E" + str(temp), t[wrap]["header"]["net"], self.wd)
                    _write_center(worksheet, "F" + str(temp), t[wrap]["header"]["time"], self.wd)

                    cpu = readInfo(t[wrap]["cpu"])
                    men = readInfo(t[wrap]["men"])
                    fps = readInfo(t[wrap]["fps"])
                    flow = readInfo(t[wrap]["flow"])
                    print("----wrap-----")
                    print(flow)
                    _write_center(worksheet, "G" + str(temp), BaseAnalysis.maxCpu(cpu), self.wd)
                    _write_center(worksheet, "H" + str(temp), BaseAnalysis.avgCpu(cpu), self.wd)
                    _write_center(worksheet, "I" + str(temp), BaseAnalysis.maxMen(men), self.wd)
                    _write_center(worksheet, "J" + str(temp), BaseAnalysis.avgMen(men, t[wrap]["header"]["rom"]), self.wd)
                    _write_center(worksheet, "K" + str(temp), BaseAnalysis.maxFps(fps), self.wd)
                    _write_center(worksheet, "L" + str(temp), BaseAnalysis.avgFps(fps), self.wd)
                    _write_center(worksheet, "M" + str(temp), t[wrap]["header"]["beforeBattery"], self.wd)
                    _write_center(worksheet, "N" + str(temp), t[wrap]["header"]["afterBattery"], self.wd)

                    _maxFlow = BaseAnalysis.maxFlow(flow)
                    _avgFLow = BaseAnalysis.avgFlow(flow)
                    print("-----_maxFlow----------")
                    print(_maxFlow)
                    _write_center(worksheet, "O" + str(temp), _maxFlow[0], self.wd)
                    _write_center(worksheet, "Q" + str(temp), _maxFlow[1], self.wd)
                    _write_center(worksheet, "P" + str(temp), _avgFLow[1], self.wd)
                    _write_center(worksheet, "R" + str(temp), _avgFLow[1], self.wd)

                    break
                temp = temp + 1

    def getCrashMsg(self, log):
        with open(log, encoding="utf-8") as monkey_log:
            lines = monkey_log.readlines()
            for line in lines:
                if re.findall(go.ANR, line):
                    print("存在anr错误:" + line)
                    self._crashM.append(line)
                if re.findall(go.CRASH, line):
                    print("存在crash错误:" + line)
                    self._crashM.append(line)
                if re.findall(go.EXCEPTION, line):
                    print("存在crash错误:" + line)
                    self._crashM.append(line)
    def crash(self):
        if len(self._crashM):
            worksheet = self.wd.add_worksheet("crash")
            _write_center(worksheet, "A1", '崩溃统计日志', self.wd)
            temp = 2
            for item in self._crashM:
                _write_center(worksheet, "A" + str(temp), item, self.wd)
                temp = temp + 1

    def plot(self, worksheet, types, lenData, name):
        '''

        :param worksheet:
        :param types: cpu,fps,flow,battery
        :param lenData: 数据长度
        :param name: sheet名字
        :return:
        '''
        values = ""
        row = ""
        title = ""
        if types == "cpu":
            values = "="+name+"!$A$1:$A$" + str(lenData + 1)
            row = 'A' + str(lenData)
            title = "cpu使用率"
        elif types == "men":
            values = "="+name+"!$B$1:$B$" + str(lenData + 1)
            row = 'B' + str(lenData)
            title = "内存使用MB"
        elif types == "fps":
            values = "=" + name + "!$C$1:$C$" + str(lenData + 1)
            row = 'C' + str(lenData)
            title = "fps使用情况"
        elif types == "battery":
            values = "="+name+"!$D$1:$D$" + str(lenData + 1)
            row = 'D' + str(lenData)
            title = "电池剩余%"
        elif types == "flowUp":
            values = "="+name+"!$E$1:$E$" + str(lenData + 1)
            row = 'E' + str(lenData)
            title = "上行流量KB"
        elif types == "flowDown":
            values = "="+name+"!$F$1:$F$" + str(lenData + 1)
            row = 'F' + str(lenData)
            title = "下行流量KB"
        chart1 = self.wd.add_chart({'type': 'line'})
        chart1.add_series({
            'values': values
        })
        chart1.set_title({'name': title})
        # worksheet.insert_chart('A9', chart1, {'x_offset': 2, 'y_offset': 2})
        worksheet.insert_chart(row, chart1)



    def close(self):
        self.wd.close()

    def analysis(self, info):
        for t in info:
            for wrap in t:
                name = wrap + "detail" # sheet名字
                worksheet = self.wd.add_worksheet(name)
                worksheet.set_column("A:A", 10)
                worksheet.set_column("B:B", 10)
                worksheet.set_column("C:C", 10)
                worksheet.set_column("D:D", 10)
                worksheet.set_column("E:E", 10)
                worksheet.set_column("F:F", 10)

                worksheet.set_row(1, 30)
                worksheet.set_row(2, 30)
                worksheet.set_row(3, 30)
                worksheet.set_row(4, 30)
                worksheet.set_row(5, 30)
                worksheet.set_row(6, 30)
                define_format_H1 = get_format(self.wd, {'bold': True, 'font_size': 18})
                define_format_H2 = get_format(self.wd, {'bold': True, 'font_size': 14})
                define_format_H1.set_border(1)

                define_format_H2.set_border(1)
                define_format_H1.set_align("center")
                define_format_H2.set_align("center")
                define_format_H2.set_bg_color("blue")
                define_format_H2.set_color("#ffffff")

                _write_center(worksheet, "A1", 'cpu(%)', self.wd)
                _write_center(worksheet, "B1", 'men(M)', self.wd)
                _write_center(worksheet, "C1", 'fps', self.wd)
                _write_center(worksheet, "D1", 'battery(%)', self.wd)
                _write_center(worksheet, "E1", '上行流量(KB)', self.wd)
                _write_center(worksheet, "F1", '下行流量(KB)', self.wd)
                for item in t[wrap]:
                    print("------data-----")
                    temp = 2
                    cpu = readInfo(t[wrap]["cpu"])
                    for item in cpu:
                        _write_center(worksheet, "A" + str(temp), float("%.1f" % item)*10, self.wd)
                        temp = temp + 1

                    temp = 2
                    men = readInfo(t[wrap]["men"])
                    for item in men:
                        _write_center(worksheet, "B" + str(temp), math.ceil(item/1024), self.wd)
                        temp = temp + 1


                    temp = 2
                    fps = readInfo(t[wrap]["fps"])
                    for item in fps:
                        _write_center(worksheet, "C" + str(temp), item, self.wd)
                        temp = temp + 1

                    temp = 2
                    battery = readInfo(t[wrap]["battery"])
                    for item in battery:
                        _write_center(worksheet, "D" + str(temp), item, self.wd)
                        temp = temp + 1

                    temp = 2
                    flow = readInfo(t[wrap]["flow"])
                    for item in flow[0]:
                        if item > 0:
                            _write_center(worksheet, "E" + str(temp), math.ceil(item/1024), self.wd)
                        else:
                            _write_center(worksheet, "E" + str(temp), 0, self.wd)
                        temp = temp + 1

                    temp = 2
                    for item in flow[1]:
                        if item > 0:
                            _write_center(worksheet, "F" + str(temp), math.ceil(item/1024), self.wd)
                        else:
                            _write_center(worksheet, "F" + str(temp), 0, self.wd)
                        temp = temp + 1
                    self.plot(worksheet, "cpu", len(cpu), name)
                    self.plot(worksheet, "men", len(men), name)
                    self.plot(worksheet, "battery", len(battery), name)
                    self.plot(worksheet, "fps", len(fps), name)
                    self.plot(worksheet, "flowUp", len(flow[0]), name)
                    self.plot(worksheet, "flowDown", len(flow[1]), name)
                    break


def get_format(wd, option={}):
    return wd.add_format(option)


def get_format_center(wd, num=1):
    return wd.add_format({'align': 'center', 'valign': 'vcenter', 'border': num})


def set_border_(wd, num=1):
    return wd.add_format({}).set_border(num)


def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd))


def set_row(worksheet, num, height):
    worksheet.set_row(num, height)


if __name__ == '__main__':

    workbook = xlsxwriter.Workbook('report.xlsx')
    info = [{'emulator-5554': {'cpu': 'E:\\app\\py\\monkey1\\info\\emulator-5554_cpu.pickle', 'battery': 'E:\\app\\py\\monkey1\\info\\emulator-5554_battery.pickle', 'men': 'E:\\app\\py\\monkey1\\info\\emulator-5554_men.pickle', 'flow': 'E:\\app\\py\\monkey1\\info\\emulator-5554_flow.pickle', 'header': {'rom': 770300, 'kel': '2核', 'monkey_log': 'E:\\app\\py\\monkey1\\log\\55dd9a83-3337-46d5-bb1f-6f64b85be7cbmonkey.log', 'beforeBattery': 99, 'pix': '1440x810', 'time': '10秒', 'afterBattery': 99, 'phone_name': 'GT-I9500_samsung_4.4', 'net': 'gprs'}, 'fps': 'E:\\app\\py\\monkey1\\info\\emulator-5554_fps.pickle'}}, {'DU2TAN15AJ049163': {'cpu': 'E:\\app\\py\\monkey1\\info\\DU2TAN15AJ049163_cpu.pickle', 'battery': 'E:\\app\\py\\monkey1\\info\\DU2TAN15AJ049163_battery.pickle', 'men': 'E:\\app\\py\\monkey1\\info\\DU2TAN15AJ049163_men.pickle', 'flow': 'E:\\app\\py\\monkey1\\info\\DU2TAN15AJ049163_flow.pickle', 'header': {'rom': 3085452, 'kel': '8核', 'monkey_log': 'E:\\app\\py\\monkey1\\log\\732ac6cd-dd84-4818-80ea-d9b5339c6774monkey.log', 'beforeBattery': 94, 'pix': '1080x1920', 'time': '15秒', 'afterBattery': 94, 'phone_name': 'H60-L02_Huawei_4.4', 'net': 'gprs'}, 'fps': 'E:\\app\\py\\monkey1\\info\\DU2TAN15AJ049163_fps.pickle'}}]


    tem = OperateReport(workbook)
    tem.monitor(info)
    tem.analysis(info)
    tem.crash()
    tem.close()
    # print(len(data["cpu"]))
