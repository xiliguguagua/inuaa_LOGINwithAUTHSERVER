# i南航自动打卡--使用统一身份认证登陆
自2022年11月19日起https://m.nuaa.edu.cn/uc/wap/login网页被学校关闭，原自动打卡脚本无法登陆账号，更新为使用authserver.nuaa.edu.cn统一身份认证登陆

脚本修改自https://github.com/Wood1314/inuaa

## 介绍与使用手册

见https://github.com/Wood1314/inuaa

## 修改部分

#### 1.新增文件

```
./login.py  			实现通过authserver.nuaa.edu.cn统一身份认证进行登陆
./password/encrypt.js	拷贝自authserver.nuaa.edu.cn的加密脚本
./send_new.py  			邮件重传，减少吞邮件情况
```

#### 2.新增依赖库

```
js2p-0.74  				用于运行js脚本，无需配置js环境  
```

#### 3. config.json

```
imei					移动设备imei号
mobiletype				移动设备类型，默认android
user['cookie']			预设cookie，可为空，不为空则可绕过login直接使用eai-sess登陆打卡，抓取手机i南航cookie可避免手机i南航与脚本互相顶号
```

#### 4.精简了日志

#### 5.增加每日6点再次打卡，因为i南航提示最好6点后打卡，成功打卡不发邮件
