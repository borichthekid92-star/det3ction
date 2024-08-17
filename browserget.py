import os
import shutil

# Define the browsers and their corresponding directories
browsers = {
    "Google Chrome": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Default"),
    "Mozilla Firefox": os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Mozilla", "Firefox", "Profiles"),
    "Microsoft Edge": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data", "Default"),
    "Internet Explorer": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Windows", "INetCache")
}

# Define the destination directory
destination_dir = os.path.join(os.environ["USERPROFILE"], "Desktop", "Browser_Data")

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Loop through each browser
for browser, source_dir in browsers.items():
    # Check if the source directory exists
    if os.path.exists(source_dir):
        # Create the destination directory for the browser
        browser_destination_dir = os.path.join(destination_dir, browser)
        if not os.path.exists(browser_destination_dir):
            os.makedirs(browser_destination_dir)
        
        # Copy the files and directories from the source to the destination
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, source_dir)
                dest_path = os.path.join(browser_destination_dir, rel_path)
                dest_dir = os.path.dirname(dest_path)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.copy2(file_path, dest_path)
        
        print(f"Copy of {browser} data created at {browser_destination_dir}")
    else:
        print(f"Source directory for {browser} does not exist.")