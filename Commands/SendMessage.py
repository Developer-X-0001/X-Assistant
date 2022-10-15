import discord

from discord.ext import commands
from discord import app_commands


class SendMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="send", description="Send message to someone in DMs (Owner Only)")
    @app_commands.describe(user="Member whom you want to send DM", message="The message you want to send")
    async def send(self, interaction: discord.Interaction, user: discord.Member, message: str):
        try:
            await user.send(content=message)
            await interaction.response.send_message(content=f"<:mailsent:1026906494257594419> **{user.name}** has received your message.", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message(content=f"<:error:954610357761105980> **{user.name}** has their DMs closed.", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(
        SendMessage(bot))
