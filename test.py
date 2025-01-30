import time
import datetime
file = "result" + str(datetime.datetime.now()) + ".txt"
with open(file, "w") as f:
    f.write("Hello World")
