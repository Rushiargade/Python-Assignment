import psutil
import time

# Set the CPU usage threshold (in percent)
CPU_THRESHOLD = 80

print("Monitoring CPU usage...")

try:
    while True:  # Runs forever until interrupted
        # Get current CPU usage percentage
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Check if usage exceeds the threshold
        if cpu_usage > CPU_THRESHOLD:
            print(f"Alert! CPU usage exceeds threshold: {int(cpu_usage)}%")
        
        # Optional: sleep for a short interval (already done by interval=1)
except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")
