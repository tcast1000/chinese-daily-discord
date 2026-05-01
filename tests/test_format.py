"""
Tests for pronunciation.format — embed builder.
"""

import discord

from pronunciation.format import build_score_embed
from pronunciation.score import score_pronunciation


class TestBuildScoreEmbed:
    def test_returns_embed(self):
        result = score_pronunciation("你好", "你好")
        embed = build_score_embed(result, "你好", "你好")
        assert isinstance(embed, discord.Embed)

    def test_title_contains_percentage(self):
        result = score_pronunciation("你好", "你好")
        embed = build_score_embed(result, "你好", "你���")
        assert "100%" in embed.title

    def test_title_contains_score_for_partial(self):
        result = score_pronunciation("你好吗", "你好")
        embed = build_score_embed(result, "你好���", "你好")
        assert "%" in embed.title

    def test_has_target_field(self):
        result = score_pronunciation("你好", "你好")
        embed = build_score_embed(result, "你好", "你好")
        field_names = [f.name for f in embed.fields]
        assert "Target" in field_names

    def test_has_heard_field(self):
        result = score_pronunciation("你好", "你��")
        embed = build_score_embed(result, "你好", "你好")
        field_names = [f.name for f in embed.fields]
        assert "Heard" in field_names

    def test_has_breakdown_field(self):
        result = score_pronunciation("你好", "你好")
        embed = build_score_embed(result, "你好", "你好")
        field_names = [f.name for f in embed.fields]
        assert "Breakdown" in field_names

    def test_has_note_field(self):
        result = score_pronunciation("你好", "你好")
        embed = build_score_embed(result, "你好", "你好")
        field_names = [f.name for f in embed.fields]
        assert "Note" in field_names

    def test_green_color_for_high_score(self):
        result = score_pronunciation("你好", "你好")
        embed = build_score_embed(result, "你好", "你好")
        assert embed.color.value == 0x2ECC71

    def test_red_color_for_low_score(self):
        result = score_pronunciation("你好吗", "谢谢")
        embed = build_score_embed(result, "你���吗", "谢谢")
        assert embed.color.value == 0xE74C3C

    def test_empty_heard(self):
        result = score_pronunciation("你好", "")
        embed = build_score_embed(result, "你好", "")
        assert "0%" in embed.title

    def test_breakdown_contains_characters(self):
        result = score_pronunciation("你好", "你好")
        embed = build_score_embed(result, "你好", "你好")
        breakdown = next(f for f in embed.fields if f.name == "Breakdown")
        assert "你" in breakdown.value
        assert "好" in breakdown.value
