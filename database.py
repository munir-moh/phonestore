import sqlite3

DB_PATH = "phonestore.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS phones (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL,
            price       REAL NOT NULL,
            condition   TEXT NOT NULL,
            ram         TEXT,
            storage     TEXT,
            battery     TEXT,
            image       TEXT,
            notes       TEXT,
            sold        INTEGER DEFAULT 0,
            created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS settings (
            key   TEXT PRIMARY KEY,
            value TEXT
        );

        INSERT OR IGNORE INTO settings (key, value) VALUES ('store_name', 'PhoneStore');
        INSERT OR IGNORE INTO settings (key, value) VALUES ('whatsapp', '2348000000000');
        INSERT OR IGNORE INTO settings (key, value) VALUES ('password', 'admin123');
    """)
    conn.commit()
    conn.close()


def get_setting(key: str):
    conn = get_db()
    row = conn.execute("SELECT value FROM settings WHERE key = ?", (key,)).fetchone()
    conn.close()
    return row["value"] if row else None