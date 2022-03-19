from redbot.core import commands

class MyCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot
        bot.add_dev_env_value("mycog", lambda ctx: self)
        bot.add_dev_env_value("mycogdata", lambda ctx: self.settings[ctx.guild.id])

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")