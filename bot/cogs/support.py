from discord.ext import commands


class Support(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def guide(self, ctx):
        await ctx.send("https://wii.guide")

    @commands.command()
    async def letterbomb(self, ctx):
        await ctx.send("https://wii.guide/letterbomb")

    @commands.command()
    async def cleanrip(self, ctx):
        await ctx.send("https://wii.guide/dump-games")

    @commands.command()
    async def bluebomb(self, ctx):
        await ctx.send("https://wii.guide/bluebomb")

    @commands.command()
    async def wfl(self, ctx):
        await ctx.send("https://wii.guide/wiiflow")

    @commands.command()
    async def themes(self, ctx):
        await ctx.send("https://wii.guide/themes")

    @commands.command()
    async def bootmii(self, ctx):
        await ctx.send("https://wii.guide/hbc")

    @commands.command()
    async def priiloader(self, ctx):
        await ctx.send("https://wii.guide/priiloader")

    @commands.command()
    async def cios(self, ctx):
        await ctx.send("https://wii.guide/cios")

    @commands.command()
    async def ciosmini(self, ctx):
        await ctx.send("https://wii.guide/cios-mini")

    @commands.command()
    async def usblgx(self, ctx):
        await ctx.send("https://wii.guide/usbloadergx")

    @commands.command()
    async def rc24(self, ctx):
        await ctx.send("https://wii.guide/riiconnect24")

    @commands.command()
    async def wl24(self, ctx):
        await ctx.send("https://wii.guide/wiilink24")

    @commands.command()
    async def wiimmfi(self, ctx):
        await ctx.send("https://wii.guide/wiimmfi")

    @commands.command()
    async def syscheck(self, ctx):
        await ctx.send("https://wii.guide/syscheck")

def setup(client):
    client.add_cog(Support(client))
