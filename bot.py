import discord 
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
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
        
@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

token = os.getenv('DISCORD_TOKEN')
if not token:
    raise RuntimeError("DISCORD_TOKEN não configurado")

bot.run(token)
