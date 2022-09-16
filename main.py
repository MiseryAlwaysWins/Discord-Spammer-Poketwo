from webserver import keep_alive
import requests

channelID = 1020176438558732430
headers = {
    "authorization":
    "MTAxNzgyMzg0NjQyODA2OTg5OA.GqLu1k.Zs627_eRG5hyGAlS6SICV1lOpWvCInSDiiHmWI"
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
