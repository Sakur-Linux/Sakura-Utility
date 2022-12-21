from pyfiglet import Figlet
f = Figlet(font="slant")
msg = f.renderText("Sakura Linux")

def help():
    print(msg)
    print("−−−−−−−−−−−−")
    print("hw_info:ハードウェア情報を表示します")
    print("speedtest:speedtestを実行します")
    print("gmenu:作成中")
    print("−−−−−−−−−−−−")