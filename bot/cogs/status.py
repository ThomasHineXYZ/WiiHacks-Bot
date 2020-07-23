from discord.ext import commands
import discord

class Status(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def status(self, ctx):
        example = self.client.get_cog('Example')
        await example.test(ctx);

def setup(client):
    client.add_cog(Status(client))
