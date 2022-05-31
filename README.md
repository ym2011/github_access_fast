# github_access_fast
github 访问加速脚本,主要适用于windows；如果配置后，发现GitHub无法打开，需要重新进行配置。

# 原理
1、通过修改系统的hosts文件，绕过国内的dns解析，直接访问GitHub的CDN节点，解决DNS污染的问题。   
2、CDN节点地址：https://www.ipaddress.com/ 中用xpath抓取出ip 配置到hosts文件。    
3、加速方法介绍：https://www.cnblogs.com/faqbug/p/13387493.html    

# 使用说明

默认Windows环境：点击运行：github_fast_windows.bat

存在python3环境：点击运行：github_fast_python.bat

网络原因，无法访问，故只能手动配置方式：点击运行：github_fast_manual.bat

# 其它方法  
## GitHub 加速下载

https://ghproxy.com/ 
http://toolwa.com/github/

https://gh.api.99988866.xyz/   

## GitHub 加速访问和下载  
https://github.com.cnpmjs.org/  例如： https://github.com.cnpmjs.org/xx/xx.git    

https://hub.fastgit.org/  例如：https://hub.fastgit.org/xx/xx.git           

https://www.gitclone.com/  例如：git clone https://gitclone.com/github.com/xx/xx.git      
