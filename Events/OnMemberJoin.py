import datetime
import discord

from discord.ext import commands
from discord import app_commands


class OnMemberJoin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        welcome_channel = member.guild.get_channel(984165652858298378)
        member_role = member.guild.get_role(933389422928465981)
        pos = sum(m.joined_at < member.joined_at for m in member.guild.members if m.joined_at is not None)

        if pos == 1:
            te = "st"
        elif pos == 2:
            te = "nd"
        elif pos == 3:
            te = "rd"
        else:
            te = "th"

        embed = discord.Embed(
            title=f"Welcome to {member.guild.name}",
            description="Here you can test out Developer X's latest projects. Also you can join Beta Testers team for Cleaner Bot too, just wait for the Beta to be open.",
            color=0xffffff,
            timestamp=datetime.datetime.now()
        )
        embed.set_author(name=member.name, icon_url=member.avatar.url)
        embed.set_footer(text=f"You are our {pos}{te} member.")
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_image(url="https://i.imgur.com/XHoSQNX.png")

        await member.add_roles(member_role)
        await welcome_channel.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(
        OnMemberJoin(bot))
