__author__ = 'Administrator'
from schematics.models import Model
from schematics.types import StringType,IntType
class monkeyconfig(Model):
    cmd = StringType()
    package_name = StringType()
    logdir = StringType() #本机的log存放地址
    remote_path = StringType()  #远程服务器地址，可以给开发查看
    phone_msg_log = StringType() #临时存放手机日志信息路径
    now = StringType()
    exceptions = StringType() #异常列表监控
    sum = StringType() #事件数量
    activity = StringType()
    monkey_log = StringType()

