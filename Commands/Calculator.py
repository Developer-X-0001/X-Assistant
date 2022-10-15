# -----------Required Imports-----------
import datetime
import aiosqlite
import discord
from discord import app_commands, ButtonStyle
from discord.ui import View, button, Button
from discord.ext import commands


# -----------Calculator Buttons-----------
class CalculatorButtons(View):
    def __init__(self):
        super().__init__(timeout=None)

    # -----------Buttons [1, 2, 3, x, Exit]-----------
    @button(label="1", style=ButtonStyle.gray, custom_id="button_1", row=2)
    async def button_1(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "1"
        
        else:
            new_expression = str(data[0]) + "1"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="2", style=ButtonStyle.gray, custom_id="button_2", row=2)
    async def button_2(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "2"
        
        else:
            new_expression = str(data[0]) + "2"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="3", style=ButtonStyle.gray, custom_id="button_3", row=2)
    async def button_3(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "3"
        
        else:
            new_expression = str(data[0]) + "3"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="×", style=ButtonStyle.blurple, custom_id="button_x", row=2)
    async def button_x(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "*"
        
        else:
            new_expression = str(data[0]) + "*"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now(),
            color=discord.Color.blurple()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="Exit", style=ButtonStyle.red, custom_id="button_exit", row=2)
    async def button_exit(self, interaction: discord.Interaction, button: Button):
        await calc_db.execute(f"DELETE FROM UserCalcExpressions WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        button.disabled = True
        self.button_1.disabled = True
        self.button_2.disabled = True
        self.button_3.disabled = True
        self.button_4.disabled = True
        self.button_5.disabled = True
        self.button_6.disabled = True
        self.button_7.disabled = True
        self.button_8.disabled = True
        self.button_9.disabled = True
        self.button_0.disabled = True
        self.button_00.disabled = True
        self.button_add.disabled = True
        self.button_div.disabled = True
        self.button_x.disabled = True
        self.button_sub.disabled = True
        self.button_exit.disabled = True
        self.button_back.disabled = True
        self.button_equal.disabled = True
        self.button_dot.disabled = True
        self.button_clear.disabled = True

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```css\n[CALCULATOR CLOSED]\n```",
            timestamp=datetime.datetime.now(),
            color=discord.Color.red()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=self)

    # -----------Buttons [4, 5, 6, ÷, ←]-----------
    @button(label="4", style=ButtonStyle.gray, custom_id="button_4", row=1)
    async def button_4(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "4"
        
        else:
            new_expression = str(data[0]) + "4"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="5", style=ButtonStyle.gray, custom_id="button_5", row=1)
    async def button_5(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "5"
        
        else:
            new_expression = str(data[0]) + "5"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="6", style=ButtonStyle.gray, custom_id="button_6", row=1)
    async def button_6(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "6"
        
        else:
            new_expression = str(data[0]) + "6"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="÷", style=ButtonStyle.blurple, custom_id="button_div", row=1)
    async def button_div(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "/"
        
        else:
            new_expression = str(data[0]) + "/"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now(),
            color=discord.Color.blurple()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="←", style=ButtonStyle.red, custom_id="button_back", row=1)
    async def button_back(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = ""
        
        else:
            new_expression = str(data[0])[:-1]


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now(),
            color=discord.Color.red()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    # -----------Buttons [7, 8, 9, +, Clear]-----------
    @button(label="7", style=ButtonStyle.gray, custom_id="button_7", row=0)
    async def button_7(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "7"
        
        else:
            new_expression = str(data[0]) + "7"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="8", style=ButtonStyle.gray, custom_id="button_8", row=0)
    async def button_8(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "8"
        
        else:
            new_expression = str(data[0]) + "8"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="9", style=ButtonStyle.gray, custom_id="button_9", row=0)
    async def button_9(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "9"
        
        else:
            new_expression = str(data[0]) + "9"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="+", style=ButtonStyle.blurple, custom_id="button_add", row=0)
    async def button_add(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "+"
        
        else:
            new_expression = str(data[0]) + "+"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now(),
            color=discord.Color.blurple()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="Clear", style=ButtonStyle.red, custom_id="button_clear", row=0)
    async def button_clear(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()

        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = NULL WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```0```",
            timestamp=datetime.datetime.now(),
            color=discord.Color.red()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    # -----------Buttons [00, 0, ., -, =]-----------
    @button(label="00", style=ButtonStyle.gray, custom_id="button_00", row=3)
    async def button_00(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "00"
        
        else:
            new_expression = str(data[0]) + "00"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="0", style=ButtonStyle.gray, custom_id="button_0", row=3)
    async def button_0(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "0"
        
        else:
            new_expression = str(data[0]) + "0"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label=".", style=ButtonStyle.gray, custom_id="button_dot", row=3)
    async def button_dot(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "."
        
        else:
            new_expression = str(data[0]) + "."


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="-", style=ButtonStyle.blurple, custom_id="button_sub", row=3)
    async def button_sub(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        if data[0] is None:
            new_expression = "-"
        
        else:
            new_expression = str(data[0]) + "-"


        await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{new_expression}' WHERE user_id = {interaction.user.id}")
        await calc_db.commit()

        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{new_expression}```",
            timestamp=datetime.datetime.now(),
            color=discord.Color.blurple()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

    @button(label="=", style=ButtonStyle.green, custom_id="button_equal", row=3)
    async def button_equal(self, interaction: discord.Interaction, button: Button):
        async with calc_db.execute(f"SELECT expression FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        
        try:
            result = str(eval(data[0]))
            await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{result}' WHERE user_id = {interaction.user.id}")
            await calc_db.commit()
            
        except:
            result = "An error occurred!"
            await calc_db.execute(f"UPDATE UserCalcExpressions SET expression = '{result}' WHERE user_id = {interaction.user.id}")
            await calc_db.commit()
        
        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```{result}```",
            timestamp=datetime.datetime.now(),
            color=discord.Color.green()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")

        await interaction.response.edit_message(embed=embed, view=CalculatorButtons())

# -----------Calculator Class-----------
class Calculator(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # -----------Calculator Command-----------
    @app_commands.command(name="calculator", description="Opens a calculator")
    async def calculator(self, interaction: discord.Interaction):
        async with calc_db.execute(f"SELECT user_id FROM UserCalcExpressions WHERE user_id = {interaction.user.id}") as cursor:
            data = await cursor.fetchone()
        
        embed = discord.Embed(
            title=f"{interaction.user.name}'s Calculator",
            description=f"```0```",
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text="Press \"Exit\" when you are done calculating.")
        
        if data is None:
            await calc_db.execute(f"INSERT INTO UserCalcExpressions VALUES ({interaction.user.id}, NULL)")
            await calc_db.commit()
            await interaction.response.send_message(embed=embed, view=CalculatorButtons(), ephemeral=True)
        
        else:
            await calc_db.execute(f"DELETE FROM UserCalcExpressions WHERE user_id = {interaction.user.id}")
            await calc_db.execute(f"INSERT INTO UserCalcExpressions VALUES ({interaction.user.id}, NULL)")
            await calc_db.commit()
            await interaction.response.send_message(embed=embed, view=CalculatorButtons(), ephemeral=True)

    # -----------On-Ready Event-----------
    @commands.Cog.listener()
    async def on_ready(self):
        global calc_db
        calc_db = await aiosqlite.connect("./Databases/data.db")
        await calc_db.execute("CREATE TABLE IF NOT EXISTS UserCalcExpressions (user_id, expression, PRIMARY KEY(user_id))")

# -----------Setup Function-----------


async def setup(bot: commands.Bot):
    await bot.add_cog(
        Calculator(bot))
