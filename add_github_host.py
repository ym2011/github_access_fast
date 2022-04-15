import platform
import re

from lxml import etree
import requests
import os

"python 3"
host_file = ""


def search_host_file():
    global host_file
    for disk in ["C", "D", "E"]:
        if os.path.exists(disk + ":\Windows\System32\drivers\etc\hosts"):
            host_file = disk + ":\Windows\System32\drivers\etc\hosts"
    if len(host_file) == 0:
        raise Exception("没有找到host文件")


def get_ip(domain):
    try:
        selector = etree.HTML(requests.get("https://websites.ipaddress.com/" + domain).text)
        find_ip_address = False
        for t in selector.xpath('//main//section[1]//tr//text()'):
            if "IP Address" in t:
                find_ip_address = True
                continue
            if find_ip_address:
                return t
    except:
        pass

    raise Exception("no ip find")


# it's different if domain is assets-cdn.github.com
def add_cdn(domain):
    f = open(host_file, encoding='utf-8', mode='a')
    list_ip = []
    for i in range(1, 5):
        selector = etree.HTML(requests.get("https://websites.ipaddress.com/" + domain).text)
        ip = selector.xpath('//main/section[2]/table/tbody/tr[1]/td/div/ul/li[%s]/strong//text()' % i)
        list_ip.append(ip)
    for i in range(0, 4):
        f.write("\n" + str(list_ip[i]).lstrip("['").rstrip("']") + "  " + domain)
        # print(str(list_ip[i]).lstrip("['").rstrip("']") + "   " + domain)
    f.close()


"""
    selector = etree.HTML(requests.get("https://websites.ipaddress.com/" + domain).text)
    ip1 = selector.xpath('//main/section[2]/table/tbody/tr[1]/td/div/ul/li[1]/strong//text()')
    list_ip.append(ip1)
    ip2 = selector.xpath('//main/section[2]/table/tbody/tr[1]/td/div/ul/li[2]/strong//text()')
    list_ip.append(ip2)
    ip3 = selector.xpath('//main/section[2]/table/tbody/tr[1]/td/div/ul/li[3]/strong//text()')
    list_ip.append(ip3)
    ip4 = selector.xpath('//main/section[2]/table/tbody/tr[1]/td/div/ul/li[4]/strong//text()')
    list_ip.append(ip4)
    for i in list_ip:
        f.write("\n"+ i + "assets-cdn.github.com")
    f.close()
"""
"""
    f.write("\n"+"185.199.108.153 assets-cdn.github.com")
    f.write("\n"+"185.199.109.153 assets-cdn.github.com")
    f.write("\n"+"185.199.110.153 assets-cdn.github.com")
    f.write("\n"+"185.199.111.153 assets-cdn.github.com")
    f.close()
"""


def append_to_host(text):
    old_host = read_host()
    delete_github_host()
    try:
        f = open(host_file, encoding="utf-8", mode="w")
        f.write(old_host + "\n" + text)
        f.close()
        # print(text)
    except Exception as e:
        print("您好,写入host失败了，请用管理员方式运行bat!!!")
        raise e
        pass


"""
    old_host = read_host()
    print(old_host)
    if text in old_host:
        print(text + " 无需更新")
    else:
        try:
            f = open(host_file, encoding="utf-8", mode="w")
            f.write(old_host + "\n" + text)
            f.close()
            print(text)
        except Exception as e:
            print("您好,写入host失败了，请用管理员方式运行bat!!!")
            raise e
            pass
"""


def add_host(domain):
    append_data = get_ip(domain) + "    " + domain
    append_to_host(append_data)


def read_host():
    f = open(host_file, encoding="utf-8", mode="r")
    host_text = f.read()
    f.close()
    return host_text


# do it jus for updating the hosts for github.com
def delete_github_host():
    list_host = []
    matchPattern = re.compile(r'github.')
    file1 = open(host_file, encoding='utf-8', mode='r')
    while True:
        line = file1.readline()
        if not line:
            # print("Read file End or Error")
            break
        elif matchPattern.search(line):
            pass
        else:
            # file2.seek(-len(line[-1]), os.SEEK_END)
            list_host.append(line)
        line.strip("\n")
    file1.close()
    file2 = open(host_file, encoding='utf-8', mode='w+')
    for i in list_host:
        if i != '\n':   # 移除空行
            file2.write(i)
    #    file2.write("\n")
    file2.close()
    return file2  # <_io.TextIOWrapper name='1.txt' mode='w' encoding='utf-8'


"""
def delete_blank_line():
    file1 = open(r'1.txt', 'r', encoding="utf-8")
    file2 = open(r'2.txt', 'w', encoding="utf-8")
    lines = file1.readlines()
    for line in lines:
        if line.split():
            file2.writelines(line)
        else:
            file2.writelines("")
    file1.close()
    file2.close()
    os.remove("1.txt")
    os.rename("2.txt", "1.txt")
"""


def systemtype():
    # fix the bug for exe in windows when the program finished  without any promotion.
    if platform.system() == "Windows":
        os.system("ipconfig /flushdns")
        print(os.system("pause"))
    else:
        exit()


if __name__ == '__main__':
    search_host_file()
    delete_github_host()
    print("==         设置host开始，请耐心等待....     ==")
    add_host("github.com")
    add_host("github.global.ssl.fastly.net")
    add_cdn("assets-cdn.github.com")
    # print("==         设置host结束         ==")
    # print("----new host file--------")
    # delete_blank_line()
    print(read_host())
    print("==   设置host结束，新的hosts 文件如上所示：  ==")
    print("==   执行刷新DNS缓存，请稍等  ==")
    systemtype()
