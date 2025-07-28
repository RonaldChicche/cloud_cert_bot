import sqlite3
from datetime import datetime

DB_FILE = "storage/data.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS coupons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT,
        platform TEXT,
        title TEXT,
        description TEXT,
        url TEXT,
        expires_at TEXT,
        notified INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def save_coupons(coupons):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    for coupon in coupons:
        c.execute("""
        INSERT INTO coupons (source, platform, title, description, url, expires_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            coupon["source"],
            coupon["platform"],
            coupon["title"],
            coupon["description"],
            coupon["url"],
            coupon["expires_at"]
        ))
    conn.commit()
    conn.close()
