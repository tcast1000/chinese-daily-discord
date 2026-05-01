"""
SQLite storage for practice scores.

Stores one row per practice attempt, keyed by user + timestamp.
Provides queries for streaks, averages, and recent history.
"""

import sqlite3
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Optional

DB_PATH = Path(__file__).parent.parent / "practice_scores.db"


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            target_hanzi TEXT NOT NULL,
            heard_hanzi TEXT NOT NULL,
            score REAL NOT NULL,
            target_pinyin TEXT NOT NULL,
            heard_pinyin TEXT NOT NULL,
            note TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        )
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_scores_user_date
        ON scores (user_id, created_at)
    """)
    conn.commit()
    return conn


def log_score(
    user_id: str,
    target_hanzi: str,
    heard_hanzi: str,
    score: float,
    target_pinyin: str,
    heard_pinyin: str,
    note: str,
) -> None:
    conn = _connect()
    try:
        conn.execute(
            "INSERT INTO scores (user_id, target_hanzi, heard_hanzi, score, target_pinyin, heard_pinyin, note) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (user_id, target_hanzi, heard_hanzi, score, target_pinyin, heard_pinyin, note),
        )
        conn.commit()
    finally:
        conn.close()


@dataclass
class UserStats:
    total_attempts: int
    average_score: float
    best_score: float
    current_streak: int
    longest_streak: int
    recent_scores: list[tuple[str, float, str]]  # (target, score, date)


def get_user_stats(user_id: str) -> Optional[UserStats]:
    conn = _connect()
    try:
        row = conn.execute(
            "SELECT COUNT(*), AVG(score), MAX(score) FROM scores WHERE user_id = ?",
            (user_id,),
        ).fetchone()

        total = row[0]
        if total == 0:
            return None

        avg_score = row[1]
        best_score = row[2]

        practice_dates = [
            r[0] for r in conn.execute(
                "SELECT DISTINCT date(created_at) FROM scores WHERE user_id = ? ORDER BY date(created_at) DESC",
                (user_id,),
            ).fetchall()
        ]

        current_streak = _calc_streak(practice_dates)
        longest_streak = _calc_longest_streak(practice_dates)

        recent = conn.execute(
            "SELECT target_hanzi, score, date(created_at) FROM scores "
            "WHERE user_id = ? ORDER BY created_at DESC LIMIT 10",
            (user_id,),
        ).fetchall()

        return UserStats(
            total_attempts=total,
            average_score=avg_score,
            best_score=best_score,
            current_streak=current_streak,
            longest_streak=longest_streak,
            recent_scores=recent,
        )
    finally:
        conn.close()


def _calc_streak(dates: list[str]) -> int:
    if not dates:
        return 0
    today = date.today().isoformat()
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    if dates[0] != today and dates[0] != yesterday:
        return 0
    streak = 1
    for i in range(1, len(dates)):
        prev = date.fromisoformat(dates[i - 1])
        curr = date.fromisoformat(dates[i])
        if (prev - curr).days == 1:
            streak += 1
        else:
            break
    return streak


def _calc_longest_streak(dates: list[str]) -> int:
    if not dates:
        return 0
    sorted_dates = sorted(set(dates))
    longest = 1
    current = 1
    for i in range(1, len(sorted_dates)):
        prev = date.fromisoformat(sorted_dates[i - 1])
        curr = date.fromisoformat(sorted_dates[i])
        if (curr - prev).days == 1:
            current += 1
            longest = max(longest, current)
        else:
            current = 1
    return longest
