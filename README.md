PhoneStore API

A lightweight REST API for managing a personal phone store. Built with **FastAPI** and **SQLite** — no heavy setup, just Python.

Project Structure

phonestore/
├── main.py          
├── database.py      
├── models.py        
├── requirements.txt
├── phonestore.db    
└── README.md

1. Create and activate a virtual environment

python -m venv venv

 Windows
venv\Scripts\activate

Mac/Linux
source venv/bin/activate
```

2. Install dependencies

pip install -r requirements.txt

3. Start the server

uvicorn main:app --reload

Server runs at: **http://localhost:8000**


Testing with Postman

1. Open Postman
2. Click **Import**
3. Select `PhoneStore.postman_collection.json`
4. All requests will be loaded and ready to send


API Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/login` | Verify admin password |
| POST | `/auth/change-password` | Change admin password |
| GET | `/phones` | Get all phones (supports filtering) |
| GET | `/phones/{id}` | Get a single phone |
| POST | `/phones` | Add a new phone |
| PUT | `/phones/{id}` | Update a phone |
| DELETE | `/phones/{id}` | Delete a phone |
| GET | `/settings` | Get store settings |
| PUT | `/settings` | Update store settings |
