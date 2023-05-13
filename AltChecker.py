import os
import json
import requests

# Path to the accounts.json file
path = r"C:\Users\nodyt\.lunarclient\settings\game\accounts.json"

# Check if the file exists
if os.path.isfile(path):
    # Read the contents of the file
    with open(path) as f:
        data = json.load(f)
        # Check if the "accounts" field exists in the JSON data
        if "accounts" in data:
            # Loop through each account in the "accounts" object
            for account in data["accounts"].values():
                # Check if the account has a "username" field
                if "username" in account:
                    username = account["username"]
                    is_premium = "Premium" if not account.get("accessToken") else "Cracked"
                    print(f"{username} ({is_premium})")
        else:
            print("No Lunar Client accounts found in the file.")
    # check if user added a Lunar Client account
    if "userAccount" in data:
        if "username" in data["userAccount"]:
            print("Added Lunar Client username:", data["userAccount"]["username"])
else:
    print("Lunar Client file not found.")

# Minecraft usernames from usercache.json
user_name = os.environ['USERNAME']
json_file_path = f'C:/Users/{user_name}/AppData/Roaming/.minecraft/usercache.json'

# Check if the file exists
if os.path.isfile(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    for item in data:
        username = item['name']
        is_premium = "Premium"
        try:
            response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
            if response.status_code == 204:
                is_premium = "Cracked"
        except:
            pass
        print(f"{username} ({is_premium})")
else:
    print(f"{json_file_path} not found.")

# Minecraft usernames from usernamecache.json
username_cache_path = f'C:/Users/{user_name}/AppData/Roaming/.minecraft/usernamecache.json'

# Check if the file exists
if os.path.isfile(username_cache_path):
    with open(username_cache_path, 'r') as f:
        data = json.load(f)

    for username in data.values():
        is_premium = "Premium"
        try:
            response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
            if response.status_code == 204:
                is_premium = "Cracked"
        except:
            pass
        print(f"{username} ({is_premium})")
else:
    print(f"{username_cache_path} not found.")

os.system("pause")
# made by lrxh#0001
