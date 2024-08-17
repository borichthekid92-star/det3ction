import win32evtlog
import re

# Define the event logs to monitor
event_logs = ["Security", "System", "Application", "Windows PowerShell"]

# Define the event IDs to monitor
event_ids = [
    4624,  # Logon
    4625,  # Logoff
    4634,  # Logon failure
    4647,  # User initiated logoff
    4672,  # Special privileges assigned to new logon
    4697,  # Services started
    4698,  # Services stopped
    4699,  # Scheduled task registered
    4700,  # Scheduled task updated
    4701,  # Scheduled task deleted
    4720,  # User account created
    4722,  # User account enabled
    4723,  # User account changed
    4724,  # User account deleted
    4725,  # User account disabled
    4726,  # User account locked out
    4732,  # User added to local group
    4733,  # User removed from local group
    4735,  # Security-enabled local group created
    4737,  # Security-enabled local group changed
    4738,  # Security-enabled local group deleted
    4740,  # User account mapped for logon
    4767,  # User account unlocked
    4776,  # Account mapped for logon by system
    4781,  # The system time was changed
    4799,  # A security-enabled local group was deleted
    4800,  # The workstation was locked
    4801,  # The workstation was unlocked
    5136,  # Windows Firewall rule added
    5137,  # Windows Firewall rule changed
    5138,  # Windows Firewall rule deleted
    6144,  # Security policy in the group policy objects was applied
    6145,  # One or more errors occurred while applying security policy
]

# Define the output file
output_file = "C:\\EventLogAnalysis.txt"

# Clear the output file
with open(output_file, "w") as f:
    f.write("")

# Loop through each event log
for event_log in event_logs:
    print(f"Analyzing {event_log} event log...")

    # Get the events from the log
    handle = win32evtlog.OpenEventLog(None, event_log)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(handle, flags, 0)

    # Loop through each event
    for event in events:
        event_id = event.EventID
        event_time = event.TimeGenerated
        event_message = event.StringInserts

        # Extract relevant information from the event message
        username = None
        computer_name = None
        ip_address = None
        process_name = None
        service_name = None

        if event_id == 4624:
            username = re.search(r"Account Name:\s*(.*)\s*", event_message).group(1)
            computer_name = re.search(r"Workstation Name:\s*(.*)\s*", event_message).group(1)
            ip_address = re.search(r"Source Network Address:\s*(.*)\s*", event_message).group(1)
        elif event_id == 4697:
            service_name = re.search(r"Service Name:\s*(.*)\s*", event_message).group(1)
        elif event_id == 4720:
            username = re.search(r"Account Name:\s*(.*)\s*", event_message).group(1)

        # Output the event information to the file
        with open(output_file, "a") as f:
            f.write(f"Event ID: {event_id}\n")
            f.write(f"Event Time: {event_time}\n")
            f.write(f"Event Message: {event_message}\n")
            f.write(f"Username: {username}\n")
            f.write(f"Computer Name: {computer_name}\n")
            f.write(f"IP Address: {ip_address}\n")
            f.write(f"Process Name: {process_name}\n")
            f.write(f"Service Name: {service_name}\n")
            f.write("\n")