# Discord-News-Bot-WIth-AI

A Discord news bot with AI chatbot functionalities thanks to the OpenAI API. The bot fetches news from the NewsAPI and sends
them every 10 mins. It can also reply with sarcastic responses to messages.

**Bot Usage:**

replace ``CLIENT_TOKEN = ''``  with your token from the discord developer portal

replace ``CHANNEL_ID =`` with the ID of the channel you would like to send news articles in it

replace ``CHAT_CHANNEL_ID = `` with the ID of the channel you would like to talk to the bot 

replace ``openai.api_key = ''`` with your API key 

Then finally replace the NewsAPI key below with yours

``url = "https://newsapi.org/v2/top-headlines"
params = {
    "country": "us",
    "apiKey": "API KEY HERE"
    # Get your news API at https://newsapi.org
}``

**NOTE:**

The news API might not send new articles of they are not found every 10 minutes.
Please do not spam messages as the bot can get rate limited. It is advisory to use add slowmode to your channel.



**Limitations**

The bot does not remember past prompts, but you could deep train your own model .
The bot can only fix 1-2 lines of code due to limitations from the OpenAI API.
The bot does not always come up with accurate responses. Feel free to rweak around with the ``prompt =`` variable to create your own behhaviours.
