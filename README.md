# Discord Bot README

## Introduction

This Discord bot is designed for various malicious actions. Its primary and only purpose is to disrupt Discord servers. Below, you will find a description of the bot's functionality and how to use its commands.

## Bot Features

### General Features

1. **Prefix:** The bot's command prefix is `!`. You can change this prefix by modifying the line `bot = commands.Bot(command_prefix='!', intents=intents)`.

2. **Temporary Unavailability:** When a user sends specific commands (e.g., `!play`, `!stop`, `!song`, `!station`, `!volume`), the bot responds with a message indicating that its functions are temporarily unavailable. This is done to disguise the bot as a regular music bot.

3. **Help Command:** The `!help` command displays a list of available commands and their descriptions for general bot usage.

### Administrative Features

1. **Clear Command:** The `!clear` command allows users to delete a specified number of messages from the current channel. Usage: `!clear <amount>`.

2. **Kick and Ban Commands:** The `!x` command has two subcommands, `k` for kicking all members and `b` for banning all members on the server. Usage: `!x k` or `!x b`.

3. **Clear Channels and Roles:** The `!clearchannel` command deletes all channels on the server, and the `!clearroles` command deletes all roles on the server.

4. **Mass Operations:** The `!vse` command performs a series of mass actions, including deleting roles and channels, banning members, creating channels and roles, and sending messages to channels.

### Custom Mass Operations

1. **Custom Mass Operations (`!y`):** The `!y` command allows users to perform custom mass actions, including kicking or banning members, creating channels and roles, and sending messages. Usage: `!y <action> <name> <name1> <num_channels> <num_roles> <num_messages>`.

2. **Custom Mass Operation Help (`!y_help`):** The `!y_help` command provides detailed information on how to use custom mass operations.

## Installation and Setup

1. Clone or download the bot's code from the provided source.

2. Install the required dependencies using `pip install discord.py asyncio`.

3. Replace `'your token here'` with your actual Discord bot token in the `bot.run('your token here')` line at the end of the code.

4. Optionally, customize the bot's prefix or other settings.

5. Run the bot using `python your_bot_file.py`.

## Usage

After running the bot and adding it to your Discord server, you can use the provided commands in any text channel where the bot has the necessary permissions.

Example command usages:

- `!help`: Display the list of available commands.
- `!clear 5`: Delete the last 5 messages in the current channel.
- `!x k`: Kick all members from the server.
- `!clearchannel`: Delete all channels on the server.
- `!clearroles`: Delete all roles on the server.
- `!vse`: Perform a series of mass actions.
- `!y k exampleRole exampleMessage 4 5 6`: Custom mass action to kick members, create channels and roles, and send messages.

## Notes

- This bot has powerful administrative commands, so use it with caution, and ensure you have the necessary permissions before running commands like `!x` or `!vse`.

- Always follow Discord's [Terms of Service](https://discord.com/terms) and [Community Guidelines](https://discord.com/guidelines) when using bots on your server.

- You can further customize and expand the bot's functionality by adding more commands and features to suit your needs.

- Remember to keep your bot token confidential and do not share it publicly.

Enjoy using your Discord bot!
