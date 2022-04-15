:: authour: ym2011
:: time: 2021-12-09
:: verison: 1.0

@echo off
:: 弹窗获取管理员权限
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit


@echo off
title run_as_administrator, config github host and access quickly
cd /d %~dp0

@echo off
add_github_host.exe
