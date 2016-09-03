__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False


# def autolabel(ax, rects):
#     for rect in rects:
#         height = rect.get_height()
#         ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height), ha='center', va='bottom')
#
# #柱形
# def  mat_bar(args_list, title='monkey异常报告', xtitle=u'错误次数', ytitle=u'错误类型'):
#     N = len(args_list[0])
#     print(N)
#     ind = np.arange(N)  # the x locations for the groups
#     width = 0.35       # the width of the bars
#     fig, ax = plt.subplots()
#     rects1 = ax.bar(ind, args_list[0], width, color='r')
#     #womenMeans = args_list[1]
#     #rects2 = ax.bar(ind+width, womenMeans, width, color='y')
#
#     # add some
#     ax.set_ylabel(ytitle)
#     ax.set_xlabel(xtitle)
#     ax.set_title(title)
#     ax.set_xticks(ind+width)
#     ax.set_xticklabels(args_list[1])
#
#     #ax.legend((rects1[0], rects2[0]), ('Men', 'Women') )
#     autolabel(ax, rects1)
#     #autolabel(ax, rects2)
#     plt.yticks(np.arange(0, 10, 1))
#     plt.savefig("monkey.png", dpi=plt.gcf().dpi)
#     plt.show()
#
# #曲线[1, 2, 3, 4, 5]  [1, 4, 9, 16, 25]
# def mat_plot(args_list, title='登陆', xtitle='请求数量', ytitle='响应时间', xlim=20, ylim=3):
#     x1 = args_list[0]# Make x, y arrays for each graph
#     y1 = args_list[1]
#     #x2 = [1, 2, 4, 6, 8]
#     #y2 = [2, 4, 8, 12, 16]
#     plt.plot(x1, y1, 'r')# use pylab to plot x and y
#     #pl.plot(x2, y2, 'g')
#     plt.title(title)# give plot a title
#     plt.xlabel(xtitle)# make axis labels
#     plt.ylabel(ytitle)
#     plt.xlim(0.0, int(xlim))
#     plt.ylim(0.0, int(ylim))
#     plt.show()
#
#  #饼状
# def mat_pie(args_list, title="登陆"):
#     #list_arg = [['Frogs', 'Hogs', 'Dogs', 'Logs'], ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'], [15, 30, 45, 10]]
#     plt.figure(1, figsize=(6,6))
#     pie_sum = []
#     pie_title = []
#     pie_color = []
#     for i in range(len(args_list[2])): #[0 30, 0, 10] 对lsit中包含0的筛选出去
#         if args_list[2][i] != 0:
#             pie_sum.append(args_list[2][i])
#             pie_title.append(args_list[0][i])
#             pie_color.append(args_list[1][i])
#
#     labels = pie_title
#     sizes = pie_sum
#     colors = pie_color
#     plt.title(title, loc=u'left')
#     #explode = (0, 0, 0, 0.1) # 对应sizes，数值越大就会凸出饼形
#     plt.pie(sizes, labels=labels, colors=colors,
#             autopct='%1.1f%%', shadow=True, startangle=90)
#     # Set aspect ratio to be equal so that pie is drawn as a circle.
#     plt.axis('equal')
#     plt.show()

def cpu_men_plots(mplot):
    print(mplot.men)
    print(mplot.cpu)
    print(mplot.locator)
    import matplotlib.pyplot as pl
    import matplotlib.dates as mdates
    import datetime

    # 处理异常数据，有时候得到数据(占用情况)会比时间多一次循环的数据，造成xy的数据不一致，而引起报错
    if len(mplot.cpu[0]) != len(mplot.cpu[1][0]):
        mplot.cpu[1][0]= mplot.cpu[1][0][0:len(mplot.cpu[0])]

    if len(mplot.men[0]) != len(mplot.men[1][0]):
        mplot.men[1][0]= mplot.men[1][0][0:len(mplot.men[0])]
    # print(men[0])
    # print(men[1][0])


    a1 = pl.subplot(311)
    a1.set_title("CPU")
    a1.set_ylabel("占用情况%")
    a1.plot(mplot.cpu[0], mplot.cpu[1][0])
    a1.xaxis.set_major_locator(mdates.SecondLocator(interval=mplot.locator))
    a1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

    a2 = pl.subplot(312)
    a2.set_title("内存")
    a2.set_ylabel("使用情况 K")
    a2.plot(mplot.men[0], mplot.men[1][0])
    a2.xaxis.set_major_locator(mdates.SecondLocator(interval=mplot.locator))
    a2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

    # a3 = pl.subplot(313)
    # a3.set_title("流量")
    # a3.set_ylabel("使用情况 K")
    # a3.plot(x,list2)
    # a3.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

    # a1.margins(x=0.2)
    pl.tight_layout()
    pl.show()