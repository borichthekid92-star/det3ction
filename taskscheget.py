import subprocess

# Define the event logs to check
event_logs = ["System", "Application", "Security"]

# Loop through each event log
for log in event_logs:
    # Run the wevtutil command to query the event log
    wevtutil_command = f"wevtutil qe {log} /c:1000 /f:text"
    findstr_command = "findstr /i schtasks.exe"

    # Run the wevtutil command and pipe its output to findstr
    wevtutil_process = subprocess.Popen(wevtutil_command, shell=True, stdout=subprocess.PIPE)
    findstr_process = subprocess.Popen(findstr_command, shell=True, stdin=wevtutil_process.stdout, stdout=subprocess.PIPE)

    # Get the output from findstr
    output, _ = findstr_process.communicate()

    # Check if there's any output
    if output:
        print(f"schtasks.exe activity detected in {log} event log:")
        print(output.decode("utf-8"))
    else:
        print(f"No schtasks.exe activity detected in {log} event log.")
    