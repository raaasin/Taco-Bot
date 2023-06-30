import discord
import responses
from discord import app_commands
from discord.ext import commands
import logging
import em
import creds
guild=discord.Object(id=creds.id)
application_id = creds.application_id
TOKEN = creds.TOKEN
intents = discord.Intents.all()
logger=logging.getLogger("bot")
#fun commands Ping and Pong
class MyGroup(app_commands.Group):
    @app_commands.command()
    async def ping(self,interaction:discord.Interaction):
        await interaction.response.send_message(f"pong")

    @app_commands.command()
    async def pong(self,interaction:discord.Interaction):
        await interaction.response.send_message(f"ping")


class tourney(app_commands.Group):
    @app_commands.command()
    async def register(self,interaction: discord.Interaction,teammate1:str,teammate2:str,sub:str,coach:str):
        await interaction.response.defer()
        uid=interaction.user.id
        val = em.reg(uid)
        await interaction.followup.send(val,ephemeral=True)
    @app_commands.command()
    async def deregister(self,interaction: discord.Interaction,otp:str):
        await interaction.response.defer()
        uid=interaction.user.id
        va = em.verify(uid,otp)
        await interaction.followup.send(va,ephemeral=True)
    @app_commands.command()
    async def change_email(self,interaction: discord.Interaction,email:str):
        await interaction.response.defer()
        uid=interaction.user.id
        v=em.ce(uid,email)
        await interaction.followup.send(v,ephemeral=True)
        
    @app_commands.command()
    async def resend_otp(self,interaction: discord.Interaction):
        await interaction.response.defer()
        uid=interaction.user.id
        v=em.rotp(uid)
        await interaction.followup.send(v,ephemeral=True)
   
class signup(app_commands.Group):
    @app_commands.command()
    async def register(self,interaction: discord.Interaction,email:str):
        await interaction.response.defer()
        uid=interaction.user.id
        val = em.reg(uid,email)
        await interaction.followup.send(val,ephemeral=True)
    @app_commands.command()
    async def verify(self,interaction: discord.Interaction,otp:str):
        await interaction.response.defer()
        uid=interaction.user.id
        va = em.verify(uid,otp)
        await interaction.followup.send(va,ephemeral=True)
    @app_commands.command()
    async def change_email(self,interaction: discord.Interaction,email:str):
        await interaction.response.defer()
        uid=interaction.user.id
        v=em.ce(uid,email)
        await interaction.followup.send(v,ephemeral=True)
        
    @app_commands.command()
    async def resend_otp(self,interaction: discord.Interaction):
        await interaction.response.defer()
        uid=interaction.user.id
        v=em.rotp(uid)
        await interaction.followup.send(v,ephemeral=True)

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

