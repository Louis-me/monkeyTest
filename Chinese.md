# monkey 压力测试android 征
* python3 
* 统计性能信息cpu,men,fps,battery,flow
* 支持wifi,gprs统计
* 统计crash信息
* 支持多安卓设备
 


## monkey.ini 配置文件

``` 

cmd=monkey -p com.jianshu.haruki --throttle 500 --ignore-timeouts --ignore-crashes   --monitor-native-crashes -v -v -v 200 >
package_name=com.jianshu.haruki
activity = com.baiji.jianshu.account.SplashScreenActivity
net = wifi 
```

- throttle 每次事件等待500毫秒
- net 支持gprs和wifi


![monkey结果](img/analysis.PNG  "monkey结果")

![monkey结果](img/monitor.png  "monkey结果")

![monkey结果](img/crash.PNG  "monkey结果")







