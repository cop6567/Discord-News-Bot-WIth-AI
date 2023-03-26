# Discord News bot in Python by cop6567 at Github
# https://github.com/cop6567

import discord
import asyncio
import requests
import schedule
import openai
import tempfile
import os
from discord.ext import commands

openai.api_key = 'OPENAI API KEY HERE'
# Get the API key at https://platform.openai.com/docs/api-reference


CLIENT_TOKEN = 'YOUR CLIENT TOKEN HERE'
# Get your token from the discord developer portal


CHANNEL_ID = 1086650821804032040
CHAT_CHANNEL_ID = 920424429085933678

url = "https://newsapi.org/v2/top-headlines"
params = {
    "country": "us",
    "apiKey": "API KEY HERE"
    # Get your news API at https://newsapi.org
}

intents = discord.Intents.all()
intents.members = True

client = discord.Client(intents=intents)

latest_url = ""



def ask_connor(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    return response.choices[0].text.strip()


prompt = "Connor is a chatbot that reluctantly answers questions with sarcastic responses, as well completes code and fixes code and puts ``` ``` around code:\n\nYou: "

history = []

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id != CHAT_CHANNEL_ID:
        return
    connor_response = ask_connor(prompt + message.content + "\nCONNOR:")
    channel = client.get_channel(CHAT_CHANNEL_ID)
    await channel.send(connor_response)
    conversation = (message.content, connor_response)
    history.append(conversation)


def get_latest_article():
    global latest_article
    response = requests.get(url, params=params)
    articles = response.json()['articles']
    latest_article = articles[0]
    return latest_article



async def send_article():
    global latest_url
    latest_article = get_latest_article()
    if latest_article['url'] != latest_url:
        channel = await client.fetch_channel(CHANNEL_ID)
        message = f"New article: {latest_article['title']} - {latest_article['url']}"
        await channel.send(message)
        latest_url = latest_article['url']
        response_text = f'\n {message}'

        prompt = "Come up with a sarcastic response to this news article: " + response_text
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        sarcastic_response = response.choices[0].text.strip()
        if sarcastic_response:
            await channel.send(sarcastic_response)
    else:
        return 'no update found'


@client.event
async def on_ready():
    print('Bot is ready to use.')
    schedule.every(10).minutes.do(send_article)

    while True:
        await send_article()
        await asyncio.sleep(10*60)  # wait for 10 minutes before sending the next article



client.run(CLIENT_TOKEN)
