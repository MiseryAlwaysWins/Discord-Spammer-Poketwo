from webserver import keep_alive
import requests

channelID = PUT THE CHANNEL ID
headers = {
    "authorization":
    "ODU1MDY3ODkwMzYwOTA5ODI0.GtSrFe.Vqy4fQNsF_Q8XWn0R2iLAqQvkj5jNSe2NZisKw"
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
