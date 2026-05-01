"""
Tests for pronunciation.db — SQLite score storage.
"""

import sqlite3
from pathlib import Path
from unittest.mock import patch

import pytest

from pronunciation.db import DB_PATH, get_user_stats, log_score, _calc_streak, _calc_longest_streak


@pytest.fixture(autouse=True)
def use_temp_db(tmp_path):
    test_db = tmp_path / "test_scores.db"
    with patch("pronunciation.db.DB_PATH", test_db):
        yield test_db


class TestLogScore:
    def test_inserts_row(self, use_temp_db):
        log_score("user1", "你好", "你好", 1.0, "ni3 hao3", "ni3 hao3", "Perfect")
        conn = sqlite3.connect(str(use_temp_db))
        count = conn.execute("SELECT COUNT(*) FROM scores").fetchone()[0]
        conn.close()
        assert count == 1

    def test_multiple_inserts(self, use_temp_db):
        log_score("user1", "你好", "你好", 1.0, "ni3 hao3", "ni3 hao3", "Perfect")
        log_score("user1", "谢谢", "谢谢", 0.9, "xie4 xie4", "xie4 xie4", "Close")
        log_score("user2", "你好", "你好", 0.8, "ni3 hao3", "ni3 hao3", "Good")
        conn = sqlite3.connect(str(use_temp_db))
        count = conn.execute("SELECT COUNT(*) FROM scores").fetchone()[0]
        conn.close()
        assert count == 3

    def test_stores_correct_data(self, use_temp_db):
        log_score("user1", "你好", "尼好", 0.8, "ni3 hao3", "ni2 hao3", "Tone off")
        conn = sqlite3.connect(str(use_temp_db))
        row = conn.execute("SELECT user_id, target_hanzi, heard_hanzi, score, note FROM scores").fetchone()
        conn.close()
        assert row == ("user1", "你好", "尼好", 0.8, "Tone off")


class TestGetUserStats:
    def test_no_data_returns_none(self):
        result = get_user_stats("nonexistent_user")
        assert result is None

    def test_basic_stats(self):
        log_score("user1", "你好", "你好", 1.0, "ni3 hao3", "ni3 hao3", "Perfect")
        log_score("user1", "谢谢", "谢谢", 0.8, "xie4 xie4", "xie4 xie4", "Good")
        stats = get_user_stats("user1")
        assert stats is not None
        assert stats.total_attempts == 2
        assert stats.average_score == pytest.approx(0.9)
        assert stats.best_score == 1.0

    def test_recent_scores_limited(self):
        for i in range(15):
            log_score("user1", f"phrase{i}", f"phrase{i}", 0.5 + i * 0.03, "p", "p", "note")
        stats = get_user_stats("user1")
        assert len(stats.recent_scores) == 10

    def test_separate_users(self):
        log_score("user1", "你好", "你好", 1.0, "p", "p", "n")
        log_score("user2", "你好", "你好", 0.5, "p", "p", "n")
        stats1 = get_user_stats("user1")
        stats2 = get_user_stats("user2")
        assert stats1.total_attempts == 1
        assert stats2.total_attempts == 1
        assert stats1.average_score == 1.0
        assert stats2.average_score == 0.5


class TestStreakCalculation:
    def test_empty(self):
        assert _calc_streak([]) == 0

    def test_single_today(self):
        from datetime import date
        today = date.today().isoformat()
        assert _calc_streak([today]) == 1

    def test_consecutive_days(self):
        from datetime import date, timedelta
        today = date.today()
        dates = [(today - timedelta(days=i)).isoformat() for i in range(5)]
        assert _calc_streak(dates) == 5

    def test_gap_breaks_streak(self):
        from datetime import date, timedelta
        today = date.today()
        dates = [
            today.isoformat(),
            (today - timedelta(days=1)).isoformat(),
            (today - timedelta(days=3)).isoformat(),
        ]
        assert _calc_streak(dates) == 2

    def test_no_recent_activity(self):
        from datetime import date, timedelta
        old = (date.today() - timedelta(days=5)).isoformat()
        assert _calc_streak([old]) == 0


class TestLongestStreak:
    def test_empty(self):
        assert _calc_longest_streak([]) == 0

    def test_single_day(self):
        assert _calc_longest_streak(["2026-01-01"]) == 1

    def test_finds_longest(self):
        dates = [
            "2026-01-01", "2026-01-02",
            "2026-01-10", "2026-01-11", "2026-01-12", "2026-01-13",
        ]
        assert _calc_longest_streak(dates) == 4

    def test_all_consecutive(self):
        dates = ["2026-01-01", "2026-01-02", "2026-01-03"]
        assert _calc_longest_streak(dates) == 3
