from bs4 import BeautifulSoup
from discord.ext import commands
import lib.embedder
import urllib.request


class GameList(commands.Cog):
    def __init__(self, client):
        self.client = client
        print("Loading gamelist cog")

    def cog_unload(self):
        print("Unloading gamelist cog")

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def gamelist(self, ctx):
        # Grab the channel that this command was given from
        channel = self.client.get_channel(ctx.channel.id)

        # This lets Discord show that the bot is "typing" while it is doing
        # something
        async with channel.typing():
            # Connect to the URL
            response = urllib.request.urlopen("https://wiimmfi.de/stat?m=20")

            # If one of the pages doesn't load up successfully, just kill the program
            if response.code != 200:
                raise ValueError("Wiimmfi website is down")

            # Parse HTML and save to BeautifulSoup object
            soup = BeautifulSoup(response, "html.parser")

            # Iterate through each of the games in the list
            game_list = []
            for line in soup.find("table", id="game").find_all("tr"):
                # Set up the cells in to a usable list
                list = []
                for cell in line.find_all("td"):
                    list.append(cell.text.strip())

                # If they aren't any of the game rows
                if len(list) != 7:
                    continue

                # If the game has no players
                if list[4] == "—":
                    continue

                # Add this game's info to the dictionary
                game_list.append({
                    "id": list[0],
                    "name": list[1],
                    "players": list[4],
                    "total_logins": list[5]
                })

            # Generate the test for outputting
            output = ""
            total_count = 0
            for game in game_list:
                output += f"{game['name']}: {game['players']}\n"
                total_count += int(game['players'])

            fields = [
                ("Total Online Users:", total_count, True),
            ]

            await ctx.send(embed=lib.embedder.make_embed(
                type="info",
                title="Wiimmfi Game List",
                title_url="https://wiimmfi.de/stat?m=8",
                thumbnail="https://wiimmfi.de/images/wiimmfi-dark.png",
                content=output,
                fields=fields
            ))


def setup(client):
    client.add_cog(GameList(client))
