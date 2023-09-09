import discord
from sifre import  gen_pass



# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):   
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")   
    if message.content.startswith('$pass'):
        await message.channel.send(gen_pass(7))     
    elif message.content.startswith('$bye'):
        await message.channel.send("\where are you going")
    elif message.content.startswith('$I have to go to the market'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("MTE0OTMwNzI1MTI3OTAxMTk0MQ.Gx_EEN.YAjlX8CGWcQ-LTBgd_FDkT2x8LxSBCwRy40KSY")