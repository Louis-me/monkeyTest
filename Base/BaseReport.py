import math
import xlsxwriter


class OperateReport:
    def __init__(self, wd):
        self.wd = wd
        # self.pie(self.wd, worksheet)

    def monitor(self, worksheet, header, data):

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

        worksheet.merge_range('A1:L1', 'monkey性能监控_' + header["phone_name"], define_format_H1)
        _write_center(worksheet, "A2", 'CPU', self.wd)
        _write_center(worksheet, "C2", '内存', self.wd)
        _write_center(worksheet, "E2", '分辨率', self.wd)
        _write_center(worksheet, "G2", '网络', self.wd)
        _write_center(worksheet, "H2", header["net"], self.wd)
        _write_center(worksheet, "I2", "耗时", self.wd)

        _write_center(worksheet, "B2", header["kel"], self.wd)
        _write_center(worksheet, "D2", str(math.ceil(header["rom"] / 1024)) + "M", self.wd)
        _write_center(worksheet, "F2", header["pix"], self.wd)
        _write_center(worksheet, "J2", header["time"], self.wd)

        _write_center(worksheet, "A3", 'CPU最大峰值', self.wd)
        _write_center(worksheet, "B3", 'CPU均值', self.wd)
        _write_center(worksheet, "C3", '内存使用峰值', self.wd)
        _write_center(worksheet, "D3", '内存使用均值', self.wd)
        _write_center(worksheet, "E3", 'fps峰值', self.wd)
        _write_center(worksheet, "F3", 'fps均值', self.wd)
        _write_center(worksheet, "G3", '电量测试之前', self.wd)
        _write_center(worksheet, "H3", '电量测试之后', self.wd)
        _write_center(worksheet, "I3", '上行流量峰值', self.wd)
        _write_center(worksheet, "J3", '上行流量均值', self.wd)
        _write_center(worksheet, "K3", '下行流量峰值', self.wd)
        _write_center(worksheet, "L3", '下行流量均值', self.wd)

        temp = 4
        print(data)
        _write_center(worksheet, "A" + str(temp), data["maxCpu"], self.wd)
        _write_center(worksheet, "B" + str(temp), data["avgCpu"], self.wd)
        _write_center(worksheet, "C" + str(temp), data["maxMen"], self.wd)
        _write_center(worksheet, "D" + str(temp), data["avgMen"], self.wd)

        _write_center(worksheet, "E" + str(temp), data["maxFps"], self.wd)
        _write_center(worksheet, "F" + str(temp), data["avgFps"], self.wd)
        _write_center(worksheet, "G" + str(temp), data["beforeBattery"], self.wd)
        _write_center(worksheet, "H" + str(temp), data["afterBattery"], self.wd)
        _write_center(worksheet, "I" + str(temp), data["maxFlowUp"], self.wd)
        _write_center(worksheet, "J" + str(temp), data["avgFlowUp"], self.wd)
        _write_center(worksheet, "K" + str(temp), data["maxFlowDown"], self.wd)
        _write_center(worksheet, "L" + str(temp), data["avgFlowDown"], self.wd)
        # temp = temp + 1

    def pie(self, workbook, worksheet):
        chart1 = workbook.add_chart({'type': 'pie'})
        chart1.add_series({
            'name': '自动化测试统计',
            'categories': '=测试总况!$C$3:$C$4',
            'values': '=测试总况!$D$3:$D$4',
        })
        chart1.set_title({'name': '自动化测试统计'})
        chart1.set_style(10)
        worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})
        # pie(self.wd, worksheet)


    def plot(self,workbook, worksheet, type, lenData):
        '''
        
        :param workbook: 
        :param worksheet: 
        :param type: cpu,fps,flow,battery
        :param lenData: 数据长度
        :return: 
        '''
        values = ""
        row = ""
        title = ""
        if type == "cpu":
            values = '=详细信息!$A$1:$A$' + str(lenData + 1)
            row = 'A' + str(lenData)
            title = "cpu使用率"
        elif type == "men":
            values = '=详细信息!$B$1:$B$' + str(lenData + 1)
            row = 'B' + str(lenData)
            title = "内存使用MB"
        elif type == "fps":
            values = '=详细信息!$C$1:$C$' + str(lenData + 1)
            row = 'C' + str(lenData)
            title = "fps使用情况"
        elif type == "battery":
            values = '=详细信息!$D$1:$D$' + str(lenData + 1)
            row = 'D' + str(lenData)
            title = "电池剩余%"
        elif type == "flowUp":
            values = '=详细信息!$E$1:$E$' + str(lenData + 1)
            row = 'E' + str(lenData)
            title = "上行流量KB"
        elif type == "flowDown":
            values = '=详细信息!$F$1:$F$' + str(lenData + 1)
            row = 'F' + str(lenData)
            title = "下行流量KB"
        chart1 = workbook.add_chart({'type': 'line'})
        chart1.add_series({
            'values': values
        })
        chart1.set_title({'name': title})
        # worksheet.insert_chart('A9', chart1, {'x_offset': 2, 'y_offset': 2})
        worksheet.insert_chart(row, chart1)


    def crash(self, worksheet, data):
        _write_center(worksheet, "A1", '崩溃统计日志', self.wd)
        temp = 2
        for item in data:
            _write_center(worksheet, "A" + str(temp), item, self.wd)
            temp = temp + 1

    def close(self):
        self.wd.close()

    def analysis(self, worksheet, data):
        print("------data-----")
        print(data)
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

        temp = 2
        for item in data["cpu"]:
            _write_center(worksheet, "A" + str(temp), float("%.1f" % item)*10, self.wd)
            temp = temp + 1

        temp = 2
        for item in data["men"]:
            _write_center(worksheet, "B" + str(temp), math.ceil(item/1024), self.wd)
            temp = temp + 1


        temp = 2
        for item in data["fps"]:
            _write_center(worksheet, "C" + str(temp), item, self.wd)
            temp = temp + 1

        temp = 2
        for item in data["battery"]:
            _write_center(worksheet, "D" + str(temp), item, self.wd)
            temp = temp + 1

        temp = 2
        for item in data["flow"][0]:
            _write_center(worksheet, "E" + str(temp), math.ceil(item/1024), self.wd)
            temp = temp + 1

        temp = 2
        for item in data["flow"][1]:
            _write_center(worksheet, "F" + str(temp), math.ceil(item/1024), self.wd)
            temp = temp + 1
        self.plot(self.wd, worksheet, "cpu", len(data["cpu"]))
        self.plot(self.wd, worksheet, "men", len(data["men"]))
        self.plot(self.wd, worksheet, "battery", len(data["battery"]))
        self.plot(self.wd, worksheet, "fps", len(data["fps"]))
        self.plot(self.wd, worksheet, "flowUp", len(data["flow"][0]))
        self.plot(self.wd, worksheet, "flowDown", len(data["flow"][1]))



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
    worksheet = workbook.add_worksheet("详细信息")
    data = {"cpu":[0.5, 0.5, 42.0, 42.0], "fps":[55, 53, 58, 60], "men":[152934, 148256, 147704, 147736, 147592],
            "flow":[[1278463, 1283320, 1283921, 1284041, 1301729], [320679, 324074, 325569, 325725, 331187]],"battery":[55, 53, 58, 60]}
    tem = OperateReport(workbook)
    tem.analysis(worksheet, data)
    tem.close()
    # print(len(data["cpu"]))
