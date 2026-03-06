from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import get_db, init_db, get_setting
from models import (
    PhoneIn, SettingsIn, SettingsOut,
    LoginIn, PasswordChangeIn, SuccessResponse
)

app = FastAPI(
    title="PhoneStore API",
    description="Backend API for managing a personal phone store",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()


@app.post("/auth/login", response_model=SuccessResponse, tags=["Auth"])
def login(body: LoginIn):
    """Verify the admin password."""
    if body.password != get_setting("password"):
        raise HTTPException(status_code=401, detail="Wrong password")
    return {"success": True, "message": "Login successful"}


@app.post("/auth/change-password", response_model=SuccessResponse, tags=["Auth"])
def change_password(body: PasswordChangeIn):
    """Change the admin password."""
    if body.old_password != get_setting("password"):
        raise HTTPException(status_code=401, detail="Current password is incorrect")
    conn = get_db()
    conn.execute("UPDATE settings SET value = ? WHERE key = 'password'", (body.new_password,))
    conn.commit()
    conn.close()
    return {"success": True, "message": "Password updated successfully"}

@app.get("/phones", tags=["Phones"])
def get_phones(search: str = "", condition: str = "", sort: str = "newest"):
    """
    Get all phone listings with optional filters.

    - **search** — filter by phone name
    - **condition** — filter by New | Used | Refurbished
    - **sort** — newest | low | high
    """
    conn = get_db()
    query = "SELECT * FROM phones WHERE 1=1"
    params = []

    if search:
        query += " AND name LIKE ?"
        params.append(f"%{search}%")
    if condition:
        query += " AND condition = ?"
        params.append(condition)

    if sort == "low":
        query += " ORDER BY price ASC"
    elif sort == "high":
        query += " ORDER BY price DESC"
    else:
        query += " ORDER BY created_at DESC"

    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [dict(r) for r in rows]


@app.get("/phones/{phone_id}", tags=["Phones"])
def get_phone(phone_id: int):
    """Get a single phone by its ID."""
    conn = get_db()
    row = conn.execute("SELECT * FROM phones WHERE id = ?", (phone_id,)).fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Phone not found")
    return dict(row)


@app.post("/phones", tags=["Phones"], status_code=201)
def add_phone(phone: PhoneIn):
    """Add a new phone listing."""
    conn = get_db()
    cur = conn.execute(
        """INSERT INTO phones (name, price, condition, ram, storage, battery, image, notes, sold)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (phone.name, phone.price, phone.condition, phone.ram,
         phone.storage, phone.battery, phone.image, phone.notes, phone.sold)
    )
    conn.commit()
    row = conn.execute("SELECT * FROM phones WHERE id = ?", (cur.lastrowid,)).fetchone()
    conn.close()
    return dict(row)


@app.put("/phones/{phone_id}", tags=["Phones"])
def update_phone(phone_id: int, phone: PhoneIn):
    """Update an existing phone listing."""
    conn = get_db()
    exists = conn.execute("SELECT id FROM phones WHERE id = ?", (phone_id,)).fetchone()
    if not exists:
        conn.close()
        raise HTTPException(status_code=404, detail="Phone not found")
    conn.execute(
        """UPDATE phones SET name=?, price=?, condition=?, ram=?, storage=?,
           battery=?, image=?, notes=?, sold=? WHERE id=?""",
        (phone.name, phone.price, phone.condition, phone.ram,
         phone.storage, phone.battery, phone.image, phone.notes, phone.sold, phone_id)
    )
    conn.commit()
    row = conn.execute("SELECT * FROM phones WHERE id = ?", (phone_id,)).fetchone()
    conn.close()
    return dict(row)


@app.delete("/phones/{phone_id}", response_model=SuccessResponse, tags=["Phones"])
def delete_phone(phone_id: int):
    """Delete a phone listing by ID."""
    conn = get_db()
    exists = conn.execute("SELECT id FROM phones WHERE id = ?", (phone_id,)).fetchone()
    if not exists:
        conn.close()
        raise HTTPException(status_code=404, detail="Phone not found")
    conn.execute("DELETE FROM phones WHERE id = ?", (phone_id,))
    conn.commit()
    conn.close()
    return {"success": True, "message": f"Phone {phone_id} deleted successfully"}

@app.get("/settings", response_model=SettingsOut, tags=["Settings"])
def get_settings():
    """Get current store settings."""
    return {
        "store_name": get_setting("store_name"),
        "whatsapp": get_setting("whatsapp"),
    }

@app.put("/settings", response_model=SuccessResponse, tags=["Settings"])
def update_settings(body: SettingsIn):
    """Update store name and WhatsApp number."""
    conn = get_db()
    conn.execute("UPDATE settings SET value = ? WHERE key = 'store_name'", (body.store_name,))
    conn.execute("UPDATE settings SET value = ? WHERE key = 'whatsapp'", (body.whatsapp,))
    conn.commit()
    conn.close()
    return {"success": True, "message": "Settings updated successfully"}