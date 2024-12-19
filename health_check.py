import psutil
import time

def monitor_server():
    print("Starting server monitoring...\n")
    print("Press Ctrl+C to stop the script.")
    
    while True:
        try:
            # CPU usage
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Memory usage
            memory = psutil.virtual_memory()
            total_memory = memory.total / (1024 ** 3)  # Convert to GB
            used_memory = memory.used / (1024 ** 3)   # Convert to GB
            memory_percent = memory.percent
            
            # Disk usage
            disk = psutil.disk_usage('/')
            total_disk = disk.total / (1024 ** 3)  # Convert to GB
            used_disk = disk.used / (1024 ** 3)   # Convert to GB
            disk_percent = disk.percent
            
            # Display server health
            print(f"\nServer Health at {time.ctime()}:")
            print(f"CPU Usage: {cpu_usage}%")
            print(f"Memory Usage: {used_memory:.2f} GB / {total_memory:.2f} GB ({memory_percent}%)")
            print(f"Disk Usage: {used_disk:.2f} GB / {total_disk:.2f} GB ({disk_percent}%)")
            
            time.sleep(5)  # Check every 5 seconds
            
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")
            break

if __name__ == "__main__":
    monitor_server()

