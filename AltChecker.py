import json
import os
import requests


def is_premium(username):
    try:
        response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
        return "Premium" if response.status_code == 200 else "Cracked"
    except:
        return "Unknown"


def print_accounts(accounts):
    printed_usernames = set()
    for account in accounts.values():
        if "username" in account:
            username = account["username"]
            is_prem = "Premium" if account.get("accessToken") else "Cracked"
            print(f"{username} ({is_prem})")
            printed_usernames.add(username)
    return printed_usernames


def print_usercache(json_file_path, printed_usernames):
    if os.path.isfile(json_file_path):
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        for item in data:
            username = item['name']
            if username not in printed_usernames:
                is_prem = is_premium(username)
                print(f"{username} ({is_prem})")
                printed_usernames.add(username)
    else:
        print(f"{json_file_path} not found.")
    return printed_usernames


def print_usernamecache(username_cache_path, printed_usernames):
    if os.path.isfile(username_cache_path):
        with open(username_cache_path, 'r') as f:
            data = json.load(f)

        for user_id, username in data.items():
            if username not in printed_usernames:
                is_prem = is_premium(username)
                print(f"{username} ({is_prem})")
                printed_usernames.add(username)
    else:
        print(f"{username_cache_path} not found.")


if __name__ == "__main__":
    path = os.path.join(os.getenv("USERPROFILE"), ".lunarclient", "settings", "game", "accounts.json")
    if os.path.isfile(path):
        with open(path) as f:
            data = json.load(f)

            if "accounts" in data:
                printed_usernames = print_accounts(data["accounts"])
            else:
                print("No Lunar Client accounts found in the file.")
                printed_usernames = set()

        if "userAccount" in data and "username" in data["userAccount"]:
            print("Added Lunar Client username:", data["userAccount"]["username"])
            printed_usernames.add(data["userAccount"]["username"])
    else:
        print("Lunar Client file not found.")
        printed_usernames = set()

    user_name = os.getenv("USERNAME")
    json_file_path = os.path.join(os.getenv("APPDATA"), ".minecraft", "usercache.json")
    printed_usernames = print_usercache(json_file_path, printed_usernames)

    username_cache_path = os.path.join(os.getenv("APPDATA"), ".minecraft", "usernamecache.json")
    print_usernamecache(username_cache_path, printed_usernames)

    os.system("pause")
