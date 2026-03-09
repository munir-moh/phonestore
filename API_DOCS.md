PhoneStore API Docs
Base URL: `http://localhost:8000`

Auth

POST `/auth/login`
**Payload**
{
  "password": "admin123"
}
```
**Response**
{
  "success": true,
  "message": "Login successful"
}
```

POST `/auth/change-password`
**Payload**
{
  "old_password": "admin123",
  "new_password": "mynewpassword"
}
```
**Response**
{
  "success": true,
  "message": "Password updated successfully"
}
```

Phones
GET `/phones`
**Response**
[
  {
    "id": 1,
    "name": "iPhone 13 Pro",
    "price": 450000,
    "condition": "Used",
    "ram": "6GB",
    "storage": "256GB",
    "battery": "3095mAh",
    "image": "",
    "notes": "No scratches",
    "sold": 0,
    "created_at": "2025-03-06 10:00:00"
  }
]
```

GET `/phones/{id}`
**Response**
```json
{
  "id": 1,
  "name": "iPhone 13 Pro",
  "price": 450000,
  "condition": "Used",
  "ram": "6GB",
  "storage": "256GB",
  "battery": "3095mAh",
  "image": "",
  "notes": "No scratches",
  "sold": 0,
  "created_at": "2025-03-06 10:00:00"
}
```


POST `/phones`
**Payload**
{
  "name": "Samsung Galaxy A54",
  "price": 280000,
  "condition": "New",
  "ram": "8GB",
  "storage": "256GB",
  "battery": "5000mAh",
  "image": "",
  "notes": "Sealed box",
  "sold": 0
}

**Response**
{
  "id": 2,
  "name": "Samsung Galaxy A54",
  "price": 280000,
  "condition": "New",
  "ram": "8GB",
  "storage": "256GB",
  "battery": "5000mAh",
  "image": "",
  "notes": "Sealed box",
  "sold": 0,
  "created_at": "2025-03-06 11:00:00"
}


PUT `/phones/{id}`
**Payload**
{
  "name": "Samsung Galaxy A54",
  "price": 260000,
  "condition": "New",
  "ram": "8GB",
  "storage": "256GB",
  "battery": "5000mAh",
  "image": "",
  "notes": "Price reduced",
  "sold": 0
}
```
**Response**
{
  "id": 2,
  "name": "Samsung Galaxy A54",
  "price": 260000,
  "condition": "New",
  "ram": "8GB",
  "storage": "256GB",
  "battery": "5000mAh",
  "image": "",
  "notes": "Price reduced",
  "sold": 0,
  "created_at": "2025-03-06 11:00:00"
}


DELETE `/phones/{id}`
**Response**
{
  "success": true,
  "message": "Phone 2 deleted successfully"
}
```

Settings
GET `/settings`
**Response**
{
  "store_name": "PhoneStore",
  "whatsapp": "2348000000000"
}


PUT `/settings`
**Payload**
{
  "store_name": "Chidi Phones",
  "whatsapp": "2348012345678"
}
```
**Response**
{
  "success": true,
  "message": "Settings updated successfully"
}
