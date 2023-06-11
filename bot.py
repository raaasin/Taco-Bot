import discord
import responses
from discord import app_commands
from discord.ext import commands
import logging
guild=discord.Object(id=1115156465443938370)
application_id = 1114825489035579425
TOKEN = 'MTExNDgyNTQ4OTAzNTU3OTQyNQ.GINFen.QLe6Cxaq5mko6_upV98Y_uHmIUMcK08B1fu-lc'
intents = discord.Intents.all()
logger=logging.getLogger("bot")

class MyGroup(app_commands.Group):
    @app_commands.command()
    async def ping(self,interaction:discord.Interaction):
        await interaction.response.send_message(f"pong")

    @app_commands.command()
    async def pong(self,interaction:discord.Interaction):
        await interaction.response.send_message(f"ping")
   

def run_discord_bot():
    
    bot = commands.Bot(command_prefix="!",intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        mygroup=MyGroup(name="greetings",description="Welcomes users") 
        bot.tree.add_command(mygroup)
        bot.tree.copy_global_to(guild=guild)
        await bot.tree.sync(guild=guild)
    
    @bot.hybrid_command()
    async def query(ctx,query:str):
        await ctx.send(responses.handle_response(query))

    @bot.tree.command(description="Ask FAQ's", name="ask")
    async def ciao(interaction: discord.Interaction, query:str):
        await interaction.response.send_message(responses.handle_response(query))
    


    bot.run(TOKEN,root_logger=True)

