import psutil
import csv
import os
from datetime import datetime
import time

def initialize_csv(filename):
    """Initialize CSV file with headers if it doesn't exist."""
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'CPU Usage %', 'RAM Usage %'])
        print(f"Created new log file: {filename}")

def collect_system_metrics():
    """Collect current system metrics."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    return timestamp, cpu_usage, ram_usage

def log_metrics(filename):
    """Append system metrics to CSV file."""
    timestamp, cpu_usage, ram_usage = collect_system_metrics()
    
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, cpu_usage, ram_usage])
    
    print(f"[{timestamp}] CPU: {cpu_usage}% | RAM: {ram_usage}%")

def main():
    filename = 'system_health_log.csv'
    initialize_csv(filename)
    
    print("Starting system health monitoring...")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            log_metrics(filename)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == '__main__':
    main()