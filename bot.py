import discord
import responses
from discord import app_commands
from discord.ext import commands
import logging
import em
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
   
class signup(app_commands.Group):
    @app_commands.command()
    async def register(self,interaction: discord.Interaction, epicid:str,email:str):
        await interaction.response.defer()
        val = em.reg(epicid,email)
        await interaction.followup.send(val)
    

def run_discord_bot():
    
    bot = commands.Bot(command_prefix="!",intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        mygroup=MyGroup(name="greetings",description="Welcomes users") 
        bot.tree.add_command(mygroup)
        sign=signup(name="signup",description="Register to participate in tournaments")
        bot.tree.add_command(sign)
        bot.tree.copy_global_to(guild=guild)
        await bot.tree.sync(guild=guild)

    @bot.tree.command(description="Ask FAQ's", name="ask")
    async def ask(interaction: discord.Interaction, query:str):
        await interaction.response.defer()
        answer_text = responses.handle_response(query)
        await interaction.followup.send(answer_text)
    


    bot.run(TOKEN,root_logger=True)

