import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

staff = 784182496597901332
guild = 784110379629412353
brayden_birthday = 953779412262866964
brayden_id = 763587507714785301

GUILD = None
STAFF_CHANNEL = None
BRAYDEN_CHANNEL = None
SLEEP_TIME = 24


@bot.event
async def on_ready():
    global GUILD, STAFF_CHANNEL, BRAYDEN_CHANNEL
    GUILD = bot.get_guild(guild)
    STAFF_CHANNEL = GUILD.get_channel(staff)
    BRAYDEN_CHANNEL = GUILD.get_channel(brayden_birthday)
    await STAFF_CHANNEL.send("The bot is ready!")


@bot.command
async def loop(message):
    global SLEEP_TIME
    SLEEP_TIME = int(message)
    STAFF_CHANNEL.send(f"Brayden Bday time is set to recur every {SLEEP_TIME} hours.")

@tasks.loop(hours=SLEEP_TIME)
async def happy_bday():
    BRAYDEN_CHANNEL.send(f"HAPPY BIRTHDAY <@!{brayden_id}>")


if __name__ == "__main__":
    bot.run("OTYyNTk5ODM4ODQ1OTAyOTIw.YlJ49Q.3vR8lhXWGB1ctHepdEsft7xwJ50")
