import os
import requests
from bs4 import BeautifulSoup

import discord
from discord.ext import tasks, commands



class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        self.lastPosted = ""
        super().__init__(*args, **kwargs)
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        self.printer.start()

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

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

        channel = self.get_channel(983068813186699264)


        latestPost = doc.findAll("div", class_="bbWrapper")[-1]
        if(latestPost != self.lastPosted):
            saint = latestPost("iframe")
            for x in saint:
                await channel.send(x["src"])
            gfycat = latestPost("span")
            for x in gfycat:
                try:
                    await channel.send(x["data-s9e-mediaembed-iframe"].split(",")[5].replace("\"\/\/","https://").replace("\\","").replace("/ifr","").replace("\"]",""))
                except:
                    print("i crashed")   
            img = latestPost("img")
            for x in img:
                await channel.send(x["src"])
        self.lastPosted = latestPost
        


client = MyClient()

client.run("OTgzMDI3ODkzODEyNzQ4MzE5.GFU17s.AvAQDViAh-K76LLZBNbs9yXnQsPiKJ60_57h-0")



