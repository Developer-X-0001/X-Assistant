import os
import config
import discord

from discord.ext import commands

class X_Assistant(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="x.",
            intents=discord.Intents.all(),
            activity=discord.Game(name="with Developer X"),
            status=discord.Status.online
        )
    
    async def setup_hook(self):
        for filename in os.listdir("./Commands"):
            if filename.endswith(".py"):
                await self.load_extension(f"Commands.{filename[:-3]}")
                print(f"Loaded {filename}")
            else:
                pass

        for filename in os.listdir("./Events"):
            if filename.endswith(".py"):
                await self.load_extension(f"Events.{filename[:-3]}")
                print(f"Loaded {filename}")
            else:
                pass

        await bot.tree.sync()

bot = X_Assistant()

@bot.event
async def on_ready():
    print(f"{bot.user} is online with {round(bot.latency * 1000)}ms Latency.")

@bot.command(name="reload")
@commands.is_owner()
async def reload(ctx: commands.Context, cog:str):
    # Reloads the file, thus updating the Cog class.
    await bot.reload_extension(f"commands.{cog}")
    await ctx.send(f"🔁 {cog} reloaded!")

@bot.command(name="load")
@commands.is_owner()
async def load(ctx: commands.Context, cog:str):
    # Reloads the file, thus updating the Cog class.
    await bot.load_extension(f"commands.{cog}")
    await ctx.send(f"🆙 {cog} loaded!")
    
bot.run(config.TOKEN)
