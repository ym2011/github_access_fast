:: authour: ym2011
:: time: 2022-05-26
:: verison: 1.0
:: get and update the github'ip will be fail because  of the forbidden of the website,www.ipaddress.com
:: this DOS bat script  is to Get and update the github'ip,semi-automatically
@echo off
:: 弹窗获取管理员权限
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit

@echo off
:: 设置窗口的标题
title run_as_administrator, config github host and access quickly
cd /d %~dp0

@echo off
set keyword=github.
:: 删除旧的GitHub 配置IP地址
findstr /v /C:%keyword% "C:\Windows\System32\drivers\etc\hosts"  > "C:\Windows\System32\drivers\etc\hosts_back"
:: 不显示执行结果
move "C:\Windows\System32\drivers\etc\hosts_back" "C:\Windows\System32\drivers\etc\hosts"  >nul
:: 删除空白行，重复执行命令生成过多的空白行
findstr /v "^$" "C:\Windows\System32\drivers\etc\hosts" >"C:\Windows\System32\drivers\etc\hosts_back"
move "C:\Windows\System32\drivers\etc\hosts_back" "C:\Windows\System32\drivers\etc\hosts"  >nul
:: 打开 https://www.ipaddress.com/
:: 分别搜索：github.com	assets-cdn.github.com github.global.ssl.fastly.net 更新到下面
set github_ip=140.82.114.4 
set assets-cdn.github_ip1=185.199.108.153 
set assets-cdn.github_ip2=185.199.109.153 
set assets-cdn.github_ip3=185.199.110.153 
set assets-cdn.github_ip4=185.199.111.153 
set global.ssl.fastly.net=199.232.69.194
 
echo == == == == == == == == == == == == == == 
echo "== == hosts configuration is start, please wait for patient ... == =="

@echo off
:: 增加空行到文件末尾，分割新增的内容
::@echo. >> "C:\Windows\System32\drivers\etc\hosts"
echo %github_ip%              github.com >> "C:\Windows\System32\drivers\etc\hosts"
echo %assets-cdn.github_ip1%  assets-cdn.github.com>> "C:\Windows\System32\drivers\etc\hosts"
echo %assets-cdn.github_ip2%  assets-cdn.github.com >> "C:\Windows\System32\drivers\etc\hosts"
echo %assets-cdn.github_ip3%  assets-cdn.github.com >> "C:\Windows\System32\drivers\etc\hosts"
echo %assets-cdn.github_ip4%  assets-cdn.github.com >> "C:\Windows\System32\drivers\etc\hosts"
echo %global.ssl.fastly.net%  github.global.ssl.fastly.net >> "C:\Windows\System32\drivers\etc\hosts"
ipconfig /flushdns 
type "C:\Windows\System32\drivers\etc\hosts"
echo == == == == == == == == == == == == == == 
echo == == hosts configuration finished. == ==
echo == == == == == == == == == == == == == == 

@pause