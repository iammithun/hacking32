import subprocess

# Get the list of WiFi profiles
a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Extract the profile names
a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]

# Iterate over each profile and get the password if available
for i in a:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, ""))

input()
