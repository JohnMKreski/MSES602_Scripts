import psutil, datetime
import json

print("System Status")

bt = psutil.boot_time();
print("Boot time " + datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")) 

sensors = psutil.sensors_temperatures()
print("Sensor temperatures \n" + json.dumps(sensors))

cpu = psutil.cpu_percent(interval=1)
print("CPU percent used " + str(cpu) + "%")