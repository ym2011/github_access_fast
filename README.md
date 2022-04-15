# github_access_fast
github 访问加速脚本,主要适用于windows；如果配置后，发现GitHub无法打开，需要重新进行配置。

# 原理
1、通过修改系统的hosts文件，绕过国内的dns解析，直接访问GitHub的CDN节点，解决DNS污染的问题。 
2、CDN节点地址：https://www.ipaddress.com/ 中用xpath抓取出ip 配置到hosts文件。 
3、加速方法介绍：https://www.cnblogs.com/faqbug/p/13387493.html  

# 缺乏Python环境
1、运行：run_in_windows.bat

# 存在python3环境
1、安装好python3 以及 pip
2、运行：run_with_python.bat

# 其它方法  
## GitHub 加速下载

https://ghproxy.com/ 
http://toolwa.com/github/

https://gh.api.99988866.xyz/   

## GitHub 加速访问和下载  
https://github.com.cnpmjs.org/  例如： https://github.com.cnpmjs.org/xx/xx.git    

https://hub.fastgit.org/  例如：https://hub.fastgit.org/xx/xx.git           

https://www.gitclone.com/  例如：git clone https://gitclone.com/github.com/xx/xx.git      

## 手动添加
获取从 https://websites.ipaddress.com/  获取github.com，github.global.ssl.fastly.net， assets-cdn.github.com等IP，然后添加到C:\Windows\System32\drivers\etc\hosts 如下所示：
140.82.113.3    github.com   

199.232.69.194    github.global.ssl.fastly.net  

185.199.108.153    assets-cdn.github.com
185.199.109.153    assets-cdn.github.com
185.199.110.153    assets-cdn.github.com
185.199.111.153    assets-cdn.github.com 

最后打开cmd.exe , 进行输入命令：ipconfig /flushdns  进行更新。 