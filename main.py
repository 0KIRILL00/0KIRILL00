import random
import discord
import os




from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)
@bot.command()
async def mem(ctx):
    lst = os.listdir('image')
    rand_img = random.choice(lst)
    with open('image/' + rand_img, 'rb') as f:

        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

bot.run("")
