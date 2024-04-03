import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!")
@bot.command()
async def loja(ctx):
    await ctx.send("Bem-vindo à loja! Itens disponíveis:\n1. Espada - 100 moedas\n2. Poção de Cura - 50 moedas")

@bot.command()
async def comprar(ctx, item_id: int):
    if item_id == 1:
        await ctx.send("Você comprou uma Espada!")
    elif item_id == 2:
        await ctx.send("Você comprou uma Poção de Cura!")
    else:
        await ctx.send("Item inválido!")

bot.run('MTIyNDkyMTExMjkyNDc4NjcwOA.GMRwXK.HaZ-oMczCPfCbJm1LsunsOLX1sOao8FodnCBSc')