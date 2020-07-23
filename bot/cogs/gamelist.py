from bs4 import BeautifulSoup;
from discord.ext import commands
import discord
import urllib.request

class GameList(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gamelist(self, ctx):
        # Connect to the URL
        response = urllib.request.urlopen("https://wiimmfi.de/stat?m=20");

        # If one of the pages doesn't load up successfully, just kill the program
        if response.code != 200:
            raise ValueError("Wiimmfi website is down")

        # Parse HTML and save to BeautifulSoup object
        soup = BeautifulSoup(response, "html.parser");

        # Iterate through each of the games in the list
        gameList = {}
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

            # Add the game and the number of players to the dictionary
            name = list[1]
            players = list[4]
            gameList[name] = players

        # Generate the test for outputting
        output = ""
        output += "```"
        for name, players in gameList.items():
            output += f"{name}: {players}\n"
        output += "```"

        await ctx.send(output)


def setup(client):
    client.add_cog(GameList(client))
