import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "finance.db")

CATEGORIES = ["餐饮", "交通", "购物", "娱乐", "居住", "其他"]


def get_conn():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            note TEXT
        )
    """)
    conn.commit()
    conn.close()


def add_record(amount, category, date, note):
    conn = get_conn()
    conn.execute(
        "INSERT INTO records (amount, category, date, note) VALUES (?, ?, ?, ?)",
        (amount, category, date, note),
    )
    conn.commit()
    conn.close()


def get_records(month=None, categories=None):
    conn = get_conn()
    sql = "SELECT id, amount, category, date, note FROM records WHERE 1=1"
    params = []
    if month:
        sql += " AND date LIKE ?"
        params.append(month + "%")
    if categories:
        placeholders = ",".join("?" for _ in categories)
        sql += f" AND category IN ({placeholders})"
        params.extend(categories)
    sql += " ORDER BY date DESC, id DESC"
    rows = conn.execute(sql, params).fetchall()
    conn.close()
    return rows


def update_record(record_id, amount, category, date, note):
    conn = get_conn()
    cur = conn.execute(
        "UPDATE records SET amount=?, category=?, date=?, note=? WHERE id=?",
        (amount, category, date, note, record_id),
    )
    conn.commit()
    updated = cur.rowcount > 0
    conn.close()
    return updated


def get_record(record_id):
    conn = get_conn()
    row = conn.execute(
        "SELECT id, amount, category, date, note FROM records WHERE id=?", (record_id,)
    ).fetchone()
    conn.close()
    return row


def delete_record(record_id):
    conn = get_conn()
    cur = conn.execute("DELETE FROM records WHERE id = ?", (record_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    conn.close()
    return deleted


def get_stats(month=None):
    conn = get_conn()
    sql = """
        SELECT category, SUM(amount), COUNT(*)
        FROM records
        WHERE 1=1
    """
    params = []
    if month:
        sql += " AND date LIKE ?"
        params.append(month + "%")
    sql += " GROUP BY category ORDER BY SUM(amount) DESC"
    rows = conn.execute(sql, params).fetchall()
    conn.close()
    return rows
