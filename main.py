import os
import requests
from bs4 import BeautifulSoup

import discord
from discord.ext import tasks, commands
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        self.printer.start()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        
        cookies = {
            'xf_user': '750588%2CmW9DUqmniJfMf_Es4OBQSATc_Uc__Oi8-5YFVp3g',
            'forum.thotsbay.com_80b1e75de6b311375acaf5ac023ee1a7_evc': '%5B%2251c5cbd8ab1df296bfea7eb29cb5339a%22%5D',
            'xf_csrf': 'qIWuGNldGa1yvbh6',
            'xf_session': '2Qb4lzAxQza0XR_ysYrx544y6MIw-kD5',
        }
        headers = {
            'authority': 'forum.thotsbay.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'nl-NL;q=0.7',
            'cache-control': 'no-cache',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'xf_user=750588%2CmW9DUqmniJfMf_Es4OBQSATc_Uc__Oi8-5YFVp3g; forum.thotsbay.com_80b1e75de6b311375acaf5ac023ee1a7_evc=%5B%2251c5cbd8ab1df296bfea7eb29cb5339a%22%5D; xf_csrf=qIWuGNldGa1yvbh6; xf_session=2Qb4lzAxQza0XR_ysYrx544y6MIw-kD5',
            'pragma': 'no-cache',
            'referer': 'https://forum.thotsbay.com/threads/sofia-gomez-sofiiiagomez.8406/page-9',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
        }

        response = requests.get('https://forum.thotsbay.com/threads/sofia-gomez-sofiiiagomez.8406/page-999', cookies=cookies, headers=headers)

        doc = BeautifulSoup(response.content, "html.parser")

        channel = self.get_channel(983338447299285014)

        lastDiscordMessage = await channel.fetch_message(channel.last_message_id)
        
        newMessage = "⚠ New sofia alert! \n"

        latestPost = doc.findAll("div", class_="bbWrapper")[-1]
        saint = latestPost("iframe")
        for x in saint:
            newMessage += x["src"] + "\n"  

        gfycat = latestPost(attrs={"data-s9e-mediaembed-iframe":True})
        for x in gfycat:
            try:
                print("ehlo")
                if "redgif" in x["data-s9e-mediaembed-iframe"]:
                    newMessage += x["data-s9e-mediaembed-iframe"].split(",")[5].replace("\"\/\/","https://").replace("\\","").replace("\"]","") + "\n" 
                else:
                    newMessage += x["data-s9e-mediaembed-iframe"].split(",")[5].replace("\"\/\/","https://").replace("\\","").replace("/ifr","").replace("\"]","") + "\n" 
            except Exception as e:
                print("Error for x: " + x.prettify())  

        img = latestPost("img")

        for x in img:
            newMessage += x["src"] + "\n" 
        link = latestPost("a")

        for x in link:
            newMessage += x["href"] + "\n" 

        if(lastDiscordMessage.content != newMessage.strip()):
            await channel.send(newMessage)


        


client = MyClient()

client.run(os.environ['discordkey'])



