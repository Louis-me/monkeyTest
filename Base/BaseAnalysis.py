import math


# total 是rom容量
def avgMen(men, total):
    if len(men):
        _men = [math.ceil(((men[i]) / total) * 1024) for i in range(len(men))]
        return str(math.ceil(sum(_men) / len(_men))) + "%"
    return "0%"


def avgCpu(cpu):
    if len(cpu):
        return str(math.ceil(sum(cpu) / len(cpu))) + "%"
    return "0%"


def avgFps(fps):
    if len(fps):
        return '%.2f' % float(str(math.ceil(sum(fps) / len(fps))))
    return 0.00


def maxMen(men):
    if len(men):
        print("men=" + str(men))
        return str(math.ceil((max(men)) / 1024)) + "M"
    return "0M"


def maxCpu(cpu):
    print("maxCpu="+str(cpu))
    if len(cpu):
        return str(max(cpu)) + "%"
    return "0%"


def maxFps(fps):
    return str(max(fps))


def maxFlow(flow):
    _flowUp = []
    _flowDown = []
    for i in range(len(flow[0])):
        if i + 1 == len(flow[0]):
            break
        _flowUp.append(math.ceil((flow[0][i + 1] - flow[0][i]) / 1024))

    for i in range(len(flow[1])):
        if i + 1 == len(flow[1]):
            break
        _flowDown.append(math.ceil((flow[1][i + 1] - flow[1][i]) / 1024))

    maxFpsUp = str(max(_flowUp)) + "KB"  # 上行流量
    maxFpsDown = str(max(_flowDown)) + "KB"  # 下行流量
    return maxFpsUp, maxFpsDown

def avgFlow(flow):
    _flowUp = []
    _flowDown = []
    for i in range(len(flow[0])):
        if i + 1 == len(flow[0]):
            break
        _flowUp.append((flow[0][i + 1] - flow[0][i])/1024)

    for i in range(len(flow[1])):
        if i + 1 == len(flow[1]):
            break
        _flowDown.append((flow[1][i + 1] - flow[1][i])/1024)
    avgFpsUp = str(math.ceil(sum(_flowUp) / len(_flowUp))) + "KB"
    avgFpsDown = str(math.ceil(sum(_flowDown) / len(_flowDown))) + "KB"
    return avgFpsUp, avgFpsDown

if __name__ == '__main__':
    flow = [[93919172, 94987124, 96309507], [14250800, 14285269, 14331153]]
    print(avgFlow(flow))
    print(maxFlow(flow))
