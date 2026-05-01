"""
Practice cog — /practice slash command + voice message reply listener.

User flow:
  1. /practice → bot replies with today's target phrase
  2. User replies to that message with a voice message
  3. Bot transcribes, scores, and replies with a detailed embed
"""

import asyncio
import random
import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional
from zoneinfo import ZoneInfo

import discord
from discord import app_commands
from discord.ext import commands

import io

from characters import CHARACTERS
from pronunciation.db import get_user_stats, log_score
from pronunciation.format import build_score_embed
from pronunciation.score import score_pronunciation
from pronunciation.transcribe import transcribe
from send_lesson import TIMEZONE, get_todays_character, load_pronunciation_mp3

AUDIO_CONTENT_TYPES = {"audio/ogg", "audio/mpeg", "audio/mp4", "audio/wav", "audio/x-m4a"}


@dataclass
class PracticePhrase:
    hanzi: str
    pinyin: str
    english: str
    char: str


def _current_slot() -> int:
    """Pick the most recent lesson slot based on current Pacific time."""
    now = datetime.now(ZoneInfo(TIMEZONE))
    hour = now.hour
    if hour < 15:
        return 0
    if hour < 18:
        return 1
    return 2


def _phrase_from_char_data(char_data: dict) -> PracticePhrase:
    return PracticePhrase(
        char_data["example_cn"],
        char_data["example_pinyin"],
        char_data["example_en"],
        char_data["char"],
    )


def _get_today_phrase() -> PracticePhrase:
    slot = _current_slot()
    char_data, _ = get_todays_character(slot)
    if char_data is None:
        return PracticePhrase("你好", "nǐ hǎo", "Hello", "你")
    return _phrase_from_char_data(char_data)


def _get_random_phrase() -> PracticePhrase:
    return _phrase_from_char_data(random.choice(CHARACTERS))


def _is_voice_message(message: discord.Message) -> bool:
    if message.attachments:
        for att in message.attachments:
            if att.content_type and any(t in att.content_type for t in AUDIO_CONTENT_TYPES):
                return True
            if att.filename and att.filename.endswith((".ogg", ".mp3", ".m4a", ".wav")):
                return True
    if message.flags.value & (1 << 13):
        return True
    return False


def _find_audio_attachment(message: discord.Message) -> Optional[discord.Attachment]:
    for att in message.attachments:
        if att.content_type and any(t in att.content_type for t in AUDIO_CONTENT_TYPES):
            return att
        if att.filename and att.filename.endswith((".ogg", ".mp3", ".m4a", ".wav")):
            return att
    return None


class PracticeCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self._prompt_messages: dict[int, str] = {}

    async def _send_practice_prompt(self, interaction: discord.Interaction, phrase: PracticePhrase):
        audio_mp3 = load_pronunciation_mp3(phrase.char)
        files = []
        if audio_mp3:
            files.append(discord.File(io.BytesIO(audio_mp3), filename="pronunciation.mp3"))

        await interaction.response.send_message(
            f"Read this aloud and reply to this message with a voice message:\n\n"
            f"**{phrase.hanzi}**\n"
            f"{phrase.pinyin}\n"
            f"*\"{phrase.english}\"*",
            files=files,
        )
        response = await interaction.original_response()
        self._prompt_messages[response.id] = phrase.hanzi

    @app_commands.command(name="practice", description="Practice pronouncing today's Chinese phrase")
    @app_commands.describe(phrase="Custom phrase to practice (optional — defaults to today's lesson)")
    async def practice(self, interaction: discord.Interaction, phrase: Optional[str] = None):
        try:
            if phrase:
                target = PracticePhrase(phrase, "", "")
                await interaction.response.send_message(
                    f"Read this aloud and reply to this message with a voice message:\n\n"
                    f"**{phrase}**"
                )
                response = await interaction.original_response()
                self._prompt_messages[response.id] = phrase
            else:
                target = _get_today_phrase()
                await self._send_practice_prompt(interaction, target)
        except Exception as e:
            print(f"ERROR in /practice: {e}")
            import traceback
            traceback.print_exc()
            if not interaction.response.is_done():
                await interaction.response.send_message("Something went wrong. Please try again.")
            else:
                await interaction.followup.send("Something went wrong. Please try again.")

    @app_commands.command(name="randompractice", description="Practice a random Chinese phrase")
    async def random_practice(self, interaction: discord.Interaction):
        try:
            target = _get_random_phrase()
            await self._send_practice_prompt(interaction, target)
        except Exception as e:
            print(f"ERROR in /random: {e}")
            import traceback
            traceback.print_exc()
            if not interaction.response.is_done():
                await interaction.response.send_message("Something went wrong. Please try again.")
            else:
                await interaction.followup.send("Something went wrong. Please try again.")

    @app_commands.command(name="stats", description="View your pronunciation practice stats and streak")
    async def stats(self, interaction: discord.Interaction):
        try:
            user_stats = get_user_stats(str(interaction.user.id))
            if user_stats is None:
                await interaction.response.send_message(
                    "No practice attempts yet! Use `/practice` or `/randompractice` to get started."
                )
                return

            streak_emoji = "\U0001f525" if user_stats.current_streak >= 3 else ""
            avg_pct = int(user_stats.average_score * 100)
            best_pct = int(user_stats.best_score * 100)

            embed = discord.Embed(
                title="Your Practice Stats",
                color=0x9B59B6,
            )
            embed.add_field(
                name="Total Attempts",
                value=str(user_stats.total_attempts),
                inline=True,
            )
            embed.add_field(
                name="Average Score",
                value=f"{avg_pct}%",
                inline=True,
            )
            embed.add_field(
                name="Best Score",
                value=f"{best_pct}%",
                inline=True,
            )
            embed.add_field(
                name="Current Streak",
                value=f"{user_stats.current_streak} day{'s' if user_stats.current_streak != 1 else ''} {streak_emoji}",
                inline=True,
            )
            embed.add_field(
                name="Longest Streak",
                value=f"{user_stats.longest_streak} day{'s' if user_stats.longest_streak != 1 else ''}",
                inline=True,
            )

            if user_stats.recent_scores:
                recent_lines = []
                for target, score_val, date_str in user_stats.recent_scores:
                    pct = int(score_val * 100)
                    if pct >= 90:
                        emoji = "\U0001f7e2"
                    elif pct >= 70:
                        emoji = "\U0001f7e1"
                    else:
                        emoji = "\U0001f534"
                    recent_lines.append(f"{emoji} {pct}% — {target} ({date_str})")
                embed.add_field(
                    name="Recent Attempts",
                    value="\n".join(recent_lines),
                    inline=False,
                )

            await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"ERROR in /stats: {e}")
            import traceback
            traceback.print_exc()
            if not interaction.response.is_done():
                await interaction.response.send_message("Something went wrong. Please try again.")
            else:
                await interaction.followup.send("Something went wrong. Please try again.")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        if not message.reference or not message.reference.message_id:
            return

        ref_id = message.reference.message_id
        if ref_id not in self._prompt_messages:
            return

        if not _is_voice_message(message):
            await message.reply("Please reply with a **voice message** so I can hear your pronunciation!")
            return

        audio_att = _find_audio_attachment(message)
        if audio_att is None:
            await message.reply("I couldn't find an audio attachment. Try sending a voice message.")
            return

        target_hanzi = self._prompt_messages[ref_id]

        await message.add_reaction("⏳")

        try:
            with tempfile.TemporaryDirectory() as tmp:
                ext = Path(audio_att.filename).suffix or ".ogg"
                audio_path = Path(tmp) / f"voice{ext}"
                await audio_att.save(audio_path)

                transcription = await asyncio.to_thread(transcribe, audio_path)
                score = await asyncio.to_thread(
                    score_pronunciation, target_hanzi, transcription.text,
                )

            log_score(
                user_id=str(message.author.id),
                target_hanzi=target_hanzi,
                heard_hanzi=transcription.text,
                score=score.overall,
                target_pinyin=score.target_pinyin,
                heard_pinyin=score.heard_pinyin,
                note=score.note,
            )

            embed = build_score_embed(score, target_hanzi, transcription.text)
            await message.remove_reaction("⏳", self.bot.user)
            await message.reply(embed=embed)

        except Exception as e:
            await message.remove_reaction("⏳", self.bot.user)
            await message.reply("Something went wrong while processing your audio. Please try again.")


async def setup(bot: commands.Bot):
    await bot.add_cog(PracticeCog(bot))
