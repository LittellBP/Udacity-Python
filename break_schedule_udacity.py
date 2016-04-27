import webbrowser
import time

print("Started at "+time.ctime())
for i in range(0, 3):
    time.sleep(60*60*2)
    webbrowser.open("https://www.youtube.com/watch?v=a5iUSuQSMB4")
