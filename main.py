from webserver import keep_alive
import requests

channelID = 1020176438558732430
headers = {
    "authorization":
    "no u"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
