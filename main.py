import discord, random, os
from discord.ext import commands

TOKEN = os.environ['MY_TOKEN']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "!", intents = intents)


@bot.command(name = "roll")
async def roll(ctx,num):
  for i in range(int(num)):
    d = random.randint(1,6)
    await ctx.channel.send(f"Rolling a D6 : {d}")

@bot.command(name = "ask")
async def ask(ctx, *words):
  st = ""
  for word in words:
    st+= word
  if st.endswith("?"):
    s = "cool question nerd"
    await ctx.channel.send(s)
  else:
    await ctx.channel.send("That's not a question")








bot.run(TOKEN)