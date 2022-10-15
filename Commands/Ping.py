import discord

from discord.ext import commands
from discord import app_commands


class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check bot's latency")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=f"Current Latency: `{round(self.bot.latency * 1000)}`ms", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(
        Ping(bot))
