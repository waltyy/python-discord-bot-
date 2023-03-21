import discord, random, os, logging
from jokeapi import Jokes
from discord.ext import commands
import utils

TOKEN = os.environ['MY_TOKEN']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)


@bot.command(name="roll")
async def roll(ctx, num):
  for i in range(int(num)):
    d = random.randint(1, 6)
    await ctx.channel.send(f"Rolling a D6 : {d}")


@bot.command(name="ask")
async def ask(ctx, *words):
  st = ""
  for word in words:
    st += word
  if st.endswith("?"):
    s = "cool question nerd"
    await ctx.channel.send(s)
  else:
    await ctx.channel.send("That's not a question")


@bot.command(name="joke", aliases=["jokes", "j", "J"])  #aliases means it run the funtion if the user spells joke with an s or if the user simply puts /j
async def joke(ctx):
  j = await Jokes()
'''
  blacklist = ["racist"]
  if not ctx.message.channel.is_nsfw():
    blacklist.append("nsfw")
  '''
  #the blacklist code is from the jokeapi package and it makes sure that the "racist" jokes dont come up when it is in the blacklist list. The       "blacklist.append" adds the "nsfw" to the blacklist list IF the channel is not nsfw which works with line 38. To make sure the blacklist code       works i have to add (blacklist=blacklist) to line 42.
    joke = await j.get_joke()
    msg = ""
  if joke["type"] == "single":
    msg = joke["joke"]
    #this code makes the joke in one line.
  else:
    msg = joke["setup"]
    msg += f"||{joke['delivery']}||"
    #this code makes the joke into two parts. the 2nd part will be blacked out and will need the user to click it to reveil the joke.
  await ctx.send(msg)
  #the jokes come from r/jokes on reddit.


#Rock-Paper-Scissors Game: In this game, your bot will prompt the player to choose either rock, paper, or scissors. The bot will then randomly choose one of the options as well. The game will continue until the player decides to quit or until a predetermined number of rounds has been played. The player with the most wins at the end of the game is declared the winner.



@bot.command(name = "rps")
async def rps(ctx, message):
  answer = message.lower()
  choices = ["rock", "paper", "scissors", "help"]
  computers_answer =  random.choice(choices)
  if answer not in choices:
    await ctx.channel.send("That is not an option in the game paper, scissors, rock.")
  elif answer == "help":
    await ctx.channel.send("To play Rock, Paper, Scissors with me, enter '.rps rock/paper/scissors'")
  else:
    if computers_answer == answer:
      await ctx.channel.send(f"Tie! We both picked {answer}")
    elif computers_answer == "rock":
      if answer == "paper":
        await ctx.channel.send(f"You win! I picked {computers_answer} and you picked {answer}")
      elif answer == "scissors":
        await ctx.channel.send(f"You lose:( I picked {computers_answer} and you picked {answer}")
    elif computers_answer == "paper":
      if answer == "scissors":
        await ctx.channel.send(f"You win! I picked {computers_answer} and you picked {answer}")
      elif answer == "rock":
        await ctx.channel.send(f"You lose:( I picked {computers_answer} and you picked {answer}")
    elif computers_answer == "scissors":
      if answer == "rock":
        await ctx.channel.send(f"You win! I picked {computers_answer} and you picked {answer}")
      elif answer == "paper":
        await ctx.channel.send(f"You lose:( I picked {computers_answer} and you picked {answer}")

bot.run(TOKEN)
