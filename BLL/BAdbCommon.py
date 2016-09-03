__author__ = 'Administrator'
from DAL.DAdbCommon import *
# 检查设备是否存在
def attached_devices():
   return AndroidDebugBridge().attached_devices()

def open_app(packagename,activity):
    return AndroidDebugBridge().open_app(packagename, activity)