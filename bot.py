import discord
from discord.ext import commands
import os

# Create an instance of the bot with the '!' prefix
intents = discord.Intents.default()
intents.messages = True  # Enable the bot to read messages
bot = commands.Bot(command_prefix='!', intents=intents)

# Define the channel ID where the bot will delete messages
target_channel_id = 1305225698012696686  # Replace with your target channel's ID

# Define an event to listen for new messages
@bot.event
async def on_message(message):
    # Check if the message is from the specified channel and is not from the bot itself
    if message.channel.id == target_channel_id and message.author != bot.user:
        await message.delete()  # Delete the message
        print(f'Message from {message.author} deleted in {message.channel.name}')
    # Make sure the bot processes other commands (if any)
    await bot.process_commands(message)

# Run the bot using the bot's token from the environment variable
bot.run(os.getenv('DISCORD_TOKEN'))  # Replace 'DISCORD_TOKEN' with your environment variable name
