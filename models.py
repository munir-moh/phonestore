from pydantic import BaseModel, Field
from typing import Optional


class PhoneIn(BaseModel):
    name: str = Field(..., example="iPhone 13 Pro")
    price: float = Field(..., example=450000)
    condition: str = Field(..., example="Used")  # New | Used | Refurbished
    ram: Optional[str] = Field("", example="6GB")
    storage: Optional[str] = Field("", example="256GB")
    battery: Optional[str] = Field("", example="3095mAh")
    image: Optional[str] = Field("", example="https://example.com/image.jpg")
    notes: Optional[str] = Field("", example="Bought 6 months ago, no scratches")
    sold: Optional[int] = Field(0, example=0)


class PhoneOut(BaseModel):
    id: int
    name: str
    price: float
    condition: str
    ram: Optional[str]
    storage: Optional[str]
    battery: Optional[str]
    image: Optional[str]
    notes: Optional[str]
    sold: int
    created_at: str


class SettingsIn(BaseModel):
    store_name: str = Field(..., example="Chidi Phones")
    whatsapp: str = Field(..., example="2348012345678")


class SettingsOut(BaseModel):
    store_name: str
    whatsapp: str


class LoginIn(BaseModel):
    password: str = Field(..., example="admin123")


class PasswordChangeIn(BaseModel):
    old_password: str = Field(..., example="admin123")
    new_password: str = Field(..., example="mynewpassword")


class SuccessResponse(BaseModel):
    success: bool
    message: str