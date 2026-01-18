import psutil, datetime
import json

print("\n=== System Status ===\n")

# Boot time
boot_timestamp = psutil.boot_time()
boot_time = datetime.datetime.fromtimestamp(boot_timestamp)
print(f"Boot time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")

# CPU info
cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU usage: {cpu_percent}%")

# Temperature sensors
temps = psutil.sensors_temperatures()
print("\nTemperature sensors (readable):")

if not temps:
    print("  No temperature sensors detected.")
else:
    for sensor_name, entries in temps.items():
        print(f"  {sensor_name}:")
        for entry in entries:
            label = entry.label or "Unnamed"
            print(
                f"    {label}: "
                f"{entry.current}°C "
                f"(high={entry.high}°C, critical={entry.critical}°C)"
            )

# Raw JSON output
print("\nTemperature sensors (raw JSON):")
print(json.dumps(temps, indent=2, default=str))

print("\n=====================\n")