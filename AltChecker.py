import os
import json
import requests


path = r"C:\Users\nodyt\.lunarclient\settings\game\accounts.json"


if os.path.isfile(path):
    
    with open(path) as f:
        data = json.load(f)
        
        if "accounts" in data:

            for account in data["accounts"].values():
          
                if "username" in account:
                    username = account["username"]
                    is_premium = "Premium" if not account.get("accessToken") else "Cracked"
                    print(f"{username} ({is_premium})")
        else:
            print("No Lunar Client accounts found in the file.")

    if "userAccount" in data:
        if "username" in data["userAccount"]:
            print("Added Lunar Client username:", data["userAccount"]["username"])
else:
    print("Lunar Client file not found.")

user_name = os.environ['USERNAME']
json_file_path = f'C:/Users/{user_name}/AppData/Roaming/.minecraft/usercache.json'

if os.path.isfile(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    printed_usernames = set()  
    for item in data:
        username = item['name']
        if username not in printed_usernames:  
            is_premium = "Premium"
            try:
                response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
                if response.status_code == 204:
                    is_premium = "Cracked"
            except:
                pass
            print(f"{username} ({is_premium})")
            printed_usernames.add(username)  
else:
    print(f"{json_file_path} not found.")

username_cache_path = f'C:/Users/{user_name}/AppData/Roaming/.minecraft/usernamecache.json'


if os.path.isfile(username_cache_path):
    with open(username_cache_path, 'r') as f:
        data = json.load(f)

    for username in data.values():
        if username not in printed_usernames:  
            is_premium = "Premium"
            try:
                response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
                if response.status_code == 204:
                    is_premium = "Cracked"
            except:
                pass
            print(f"{username} ({is_premium})")
            printed_usernames.add(username)  
else:
    print(f"{username_cache_path} not found.")

os.system("pause")
# made by lrxh#0001
