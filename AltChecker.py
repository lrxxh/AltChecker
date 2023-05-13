import json
import os
import requests


ACCOUNTS_FILE_PATH = os.path.join(os.getenv("USERPROFILE"), ".lunarclient", "settings", "game", "accounts.json")
USERCACHE_FILE_PATH = os.path.join(os.getenv("APPDATA"), ".minecraft", "usercache.json")
USERNAMECACHE_FILE_PATH = os.path.join(os.getenv("APPDATA"), ".minecraft", "usernamecache.json")


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
            is_prem = "Premium" if not account.get("accessToken") else "Cracked"
            print(f"{username} ({is_prem})")
            printed_usernames.add(username)
    return printed_usernames


def print_cache(json_file_path, printed_usernames, key="name"):
    if os.path.isfile(json_file_path):
        with open(json_file_path, 'r') as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                print(f"Failed to decode JSON data in {json_file_path}.")
                return printed_usernames

        for item in data:
            username = item[key]
            if username not in printed_usernames:
                is_prem = is_premium(username)
                print(f"{username} ({is_prem})")
                printed_usernames.add(username)
    else:
        print(f"{json_file_path} not found.")
    return printed_usernames


if __name__ == "__main__":
    if os.path.isfile(ACCOUNTS_FILE_PATH):
        with open(ACCOUNTS_FILE_PATH) as f:
            data = json.load(f)

            if "accounts" in data:
                printed_usernames = print_accounts(data["accounts"])
            else:
                print("No Lunar Client accounts found in the file.")
                printed_usernames = set()

        if "userAccount" in data and "username" in data["userAccount"]:
            print(f"Added Lunar Client username: {data['userAccount']['username']}")
            printed_usernames.add(data["userAccount"]["username"])
    else:
        print("Lunar Client file not found.")
        printed_usernames = set()

    printed_usernames = print_cache(USERCACHE_FILE_PATH, printed_usernames)
    print_cache(USERNAMECACHE_FILE_PATH, printed_usernames)

    os.system("pause")
# made by lrxh#0001
