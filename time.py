from datetime import datetime as d

while True:
    date = d.now()
    print(date.strftime("%Y-%m-%d %H:%M:%S"))
