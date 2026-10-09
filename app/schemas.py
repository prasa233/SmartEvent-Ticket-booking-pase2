from datetime import datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, Field


# =========================
# AUTH
# =========================

class RegisterRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=100
    )


class LoginRequest(BaseModel):
    email: EmailStr

    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    role: str


# =========================
# EVENTS
# =========================

class EventCreate(BaseModel):

    title: str = Field(
        min_length=3,
        max_length=200
    )

    description: str | None = None

    location: str = Field(
        min_length=2,
        max_length=300
    )

    event_date: datetime

    price: float = Field(
        ge=0
    )

    total_tickets: int = Field(
        gt=0
    )


class EventUpdate(BaseModel):

    title: str | None = None

    description: str | None = None

    location: str | None = None

    event_date: datetime | None = None

    price: float | None = Field(
        default=None,
        ge=0
    )

    total_tickets: int | None = Field(
        default=None,
        gt=0
    )


class EventResponse(BaseModel):

    id: int

    title: str

    description: str | None

    location: str

    event_date: datetime

    price: float

    total_tickets: int

    organizer_id: int

    event_status: str

    class Config:
        from_attributes = True


# =========================
# BOOKING
# =========================

class BookingResponse(BaseModel):

    id: int

    user_id: int

    event_id: int

    quantity: int

    total_amount: float

    status: str

    class Config:
        from_attributes = True