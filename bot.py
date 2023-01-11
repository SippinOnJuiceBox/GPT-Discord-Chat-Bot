import discord
from subprocess import Popen, PIPE
from os import chdir

chdir('C:/Users/eshbe/Desktop/gpt-2-finetuning/src')

client = discord.Client()

TOKEN = 'XXX'

@client.event
async def on_ready():
    print('Logged on as {0.user}!'.format(client))

@client.event
async def on_message(message):
    #Ensure the bot doesn't respond to itself
    if message.author == client.user:
        return

    #Bot will start generating response if a message is sent in the right channel
    if message.channel.id == 792881410381316126:
        result = []

        p = Popen('python interactive_conditional_samples.py --top_k 40 --temperature 0.8 --model_name "run1" --raw_text ' + message.content, stdout=PIPE)

        for line in p.stdout:
            result.append(line)

        try:
            msg = result[1].decode()[:-2]
            await message.channel.send(msg)
            p.terminate()
        except IndexError:
            await message.channel.send("I made an oopsie, please try again :/")
            p.terminate()

client.run(TOKEN)
