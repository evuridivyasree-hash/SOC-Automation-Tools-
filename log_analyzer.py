# Simple Python script to find failed login attempts in a log file
def analyze_logs(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
        
    failed_attempts = [line for line in logs if "Failed password" in line]
    
    print(f"Total Failed Login Attempts Found: {len(failed_attempts)}")
    for attempt in failed_attempts:
        print(attempt.strip())

# This demonstrates basic string matching for SOC alert automation
