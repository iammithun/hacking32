import subprocess

def fetch_output(command):
    """Fetch the output of a command and handle encoding errors."""
    try:
        return subprocess.check_output(command, encoding='latin-1', errors='ignore')
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command: {' '.join(command)}. Error: {e}")
        return ""

# Fetch the output of the command that shows WLAN profiles
data = fetch_output(['netsh', 'wlan', 'show', 'profiles'])

# Extract profile names
profiles = [line.split(":")[1][1:-1] for line in data.split('\n') if "All User Profile" in line]

# Iterate over each profile to get the password (if any)
for profile in profiles:
    # Fetch the details of the profile
    results = fetch_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
    if results:
        # Extract the key content (password)
        password_lines = [line.split(":")[1][1:-1] for line in results.split('\n') if "Key Content" in line]
        if password_lines:
            print("{:<30} {:<}".format(profile, password_lines[0]))
        else:
            print("{:<30} {:<}".format(profile, "No password found"))
    else:
        
        print("{:<30} {:<}".format(profile, "Failed to retrieve details"))

input("Press Enter to exit...")
