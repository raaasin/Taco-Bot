import discord
import responses

intents = discord.Intents.all()


# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTExNDgyNTQ4OTAzNTU3OTQyNQ.GINFen.QLe6Cxaq5mko6_upV98Y_uHmIUMcK08B1fu-lc'
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    @client.event
    async def on_message(message):
        print(message.content)
        if message.author==client.user:
            return
        
        username = str(message.author)
        usermessage = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{usermessage}' ({channel})")

        if usermessage.startswith('?'):
            usermessage = usermessage[1:] 
            await send_message(message, usermessage, is_private=True)
        elif usermessage.startswith('&'):
            usermessage=usermessage[1:]
            await send_message(message, usermessage, is_private=False)

    
    client.run(TOKEN)
