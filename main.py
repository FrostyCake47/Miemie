import discord
import praw
import os
from datetime import date

DCLIENT_SECRET = os.getenv("MIEMIE_DCLIENT_SECRET")
RCLIENT_SECRET = os.getenv("MIEMIE_RCLIENT_SECRET")
RCLIENT_ID = os.getenv("MIEMIE_RCLIENT_ID")
REDDIT_USER = os.getenv("MIEMIE_USER")
REDDIT_PASS = os.getenv("MIEMIE_PASS")
DISCORD_TOKEN = os.getenv("MIEMIE_DCLIENT_SECRET")

def isNewDay():
    with open("./dates.txt", "r+") as f:
        dates = f.read().split()

        if str(date.today()) not in dates:
            #f.write(str(date.today()) + " ")
            f.close()
            print("its a new day, yes it is")
            return True
        
    print("no dates for you")
    return False


def getMemes():
    reddit = praw.Reddit(
    client_id=RCLIENT_ID,
    client_secret=RCLIENT_SECRET,
    password=REDDIT_PASS,
    user_agent="<Console:Frosty:1.0>",
    username=REDDIT_USER,
    )

    memes = [meme.url for meme in reddit.subreddit("memes").top(time_filter="day", limit=3) if meme.url.startswith('https://i')]
    print("got the stuffs")
    return memes

def sendMemes(memes):
    client = discord.Client(intents=discord.Intents().all())

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

        channel = client.get_channel(1109168201163624528)
        for meme in memes:
            await channel.send(meme)

        quit()

    client.run('MIEMIE_DCLIENT_SECRET')
    return

def main():
    if isNewDay():
        memes = getMemes()
        sendMemes(memes)


if __name__ == "__main__":
    main()
