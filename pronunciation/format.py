"""
Discord embed formatter for pronunciation scores.

Takes a ScoreResult and builds a rich embed with per-syllable color-coded feedback.
"""

from __future__ import annotations

import discord
from pypinyin import Style, lazy_pinyin

from pronunciation.score import ScoreResult


def _score_emoji(score: float) -> str:
    if score >= 0.9:
        return "\U0001f7e2"  # green
    if score >= 0.7:
        return "\U0001f7e1"  # yellow
    return "\U0001f534"  # red


def _overall_emoji(score: float) -> str:
    if score >= 0.9:
        return "\U0001f7e2"
    if score >= 0.7:
        return "\U0001f7e1"
    return "\U0001f534"


def _syllable_breakdown(result: ScoreResult, target_hanzi: str) -> str:
    chars = list(target_hanzi)
    lines = []
    for i, s in enumerate(result.per_syllable):
        char = chars[i] if i < len(chars) else "?"
        emoji = _score_emoji(s.score)

        if s.heard is None:
            detail = "missed"
        elif s.score >= 1.0:
            detail = ""
        else:
            issues = []
            if not s.initial_match:
                issues.append("initial")
            if not s.final_match:
                issues.append("vowel")
            if not s.tone_match:
                issues.append("tone")
            detail = ", ".join(issues) if issues else ""

        if detail:
            lines.append(f"{char} {emoji} ({detail})")
        else:
            lines.append(f"{char} {emoji}")

    return "  ".join(lines)


def _pinyin_with_diacritics(hanzi: str) -> str:
    return " ".join(lazy_pinyin(hanzi, style=Style.TONE))


def build_score_embed(
    result: ScoreResult,
    target_hanzi: str,
    heard_hanzi: str,
) -> discord.Embed:
    pct = int(result.overall * 100)
    emoji = _overall_emoji(result.overall)

    if pct >= 90:
        color = 0x2ECC71  # green
    elif pct >= 70:
        color = 0xF1C40F  # yellow
    else:
        color = 0xE74C3C  # red

    embed = discord.Embed(
        title=f"Pronunciation Score: {pct}% {emoji}",
        color=color,
    )

    embed.add_field(
        name="Target",
        value=_pinyin_with_diacritics(target_hanzi),
        inline=True,
    )
    embed.add_field(
        name="Heard",
        value=_pinyin_with_diacritics(heard_hanzi) if heard_hanzi else "(nothing)",
        inline=True,
    )
    embed.add_field(
        name="Breakdown",
        value=_syllable_breakdown(result, target_hanzi),
        inline=False,
    )
    embed.add_field(
        name="Note",
        value=result.note,
        inline=False,
    )

    return embed
