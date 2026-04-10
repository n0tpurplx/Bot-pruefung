import discord

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

client.run('YOUR_TOKEN_HERE')
