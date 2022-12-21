import psutil
import socket
import getpass
import cpuinfo
import time
from psutil._common import bytes2human
import os
import requests
from pyfiglet import Figlet
f = Figlet(font="slant")
msg = f.renderText("Sakura Linux")

def seconds_elapsed():
    return time.time() - psutil.boot_time()

def main():
    mem = psutil.virtual_memory()
    memory = bytes2human(mem.total)
    use = bytes2human(mem.used)
    # コンピュータ名を取得
    host = socket.gethostname()
    print(msg)
    print(f"{getpass.getuser()}@{host}")
    print("-------------------")
    print(f"Processor:{cpuinfo.get_cpu_info()['brand_raw']}")
    print(f"{psutil.cpu_count(logical=False)}コア{psutil.cpu_count()}スレッド")
    print(f"メモリ使用率:{use}B/{memory}B({psutil.virtual_memory().percent}%使用率)")
    t = os.popen('uptime').read()[:-1]
    print(f"連続起動時間:{t}")
    print("-------------------")
    ip = socket.gethostbyname(host)
    print(f"ローカルIPアドレス:{ip}")
    response = requests.get('http://inet-ip.info/ip')
    print(f"グローバルIPアドレス:{response.text}")
    print("-------------------")
