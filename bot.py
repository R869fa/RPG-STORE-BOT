import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

async def processar_transação(ctx, item_id: int, acao: str):
    Item = {
    1: "Espada",
    2: "Poção de Cura"
}       
    Item = Item.get (item_id)
    if not Item:
        await ctx.send("Item Inválido!")
        return
    
    await ctx.send(f"Você {acao} uma {Item}!")

bot = commands.Bot(command_prefix="!", intents=intents)
@bot.command()
async def loja(ctx):
    await ctx.send("Bem-vindo à loja! Itens disponíveis:\n1. Espada - 100 moedas\n2. Poção de Cura - 50 moedas")

@bot.command()
async def comprar(ctx, item_id: int):
        await processar_transação(ctx, item_id, "comprou")
        await ctx.send()

@bot.command()
async def vender(ctx, item_id: int):
        await processar_transação(ctx, item_id, "vendeu")

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