"""
Persistent Discord bot for pronunciation practice.

Run:  python bot.py

Requires DISCORD_TOKEN in .env or environment.
This is separate from send_lesson.py (which runs on GitHub Actions).
"""

import os
import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", "").strip()
TEST_GUILD_ID = os.environ.get("TEST_GUILD_ID", "").strip()

if not DISCORD_TOKEN:
    print("ERROR: DISCORD_TOKEN not set. Add it to .env or environment.")
    sys.exit(1)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        for cmd in bot.tree.get_commands():
            print(f"  Registered: /{cmd.name}")
        if TEST_GUILD_ID:
            guild = discord.Object(id=int(TEST_GUILD_ID))
            bot.tree.clear_commands(guild=guild)
            bot.tree.copy_global_to(guild=guild)
            synced = await bot.tree.sync(guild=guild)
            print(f"Synced {len(synced)} slash command(s) to guild {TEST_GUILD_ID}")
            for s in synced:
                print(f"  -> /{s.name}")
        else:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} slash command(s) globally")
    except Exception as e:
        print(f"Failed to sync commands: {e}")


@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: Exception):
    print(f"COMMAND ERROR: {error}")
    import traceback
    traceback.print_exc()


async def main():
    async with bot:
        await bot.load_extension("cogs.practice")
        await bot.start(DISCORD_TOKEN)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
