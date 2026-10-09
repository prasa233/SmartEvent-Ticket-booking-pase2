from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Float
)

from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(String(255), nullable=False)

    role = Column(
        String(20),
        default="USER",
        nullable=False
    )

    events = relationship(
        "Event",
        back_populates="organizer"
    )

    bookings = relationship(
        "Booking",
        back_populates="user"
    )


class Event(Base):
    __tablename__ = "events"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(200),
        nullable=False
    )

    description = Column(
        String(1000),
        nullable=True
    )

    location = Column(
        String(300),
        nullable=False
    )

    event_date = Column(
        DateTime,
        nullable=False
    )

    price = Column(
        Float,
        nullable=False
    )

    total_tickets = Column(
        Integer,
        nullable=False
    )

    organizer_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    event_status = Column(
        String(20),
        default="UPCOMING",
        nullable=False
    )

    organizer = relationship(
        "User",
        back_populates="events"
    )

    bookings = relationship(
        "Booking",
        back_populates="event"
    )


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    event_id = Column(
        Integer,
        ForeignKey("events.id"),
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    total_amount = Column(
        Float,
        nullable=False
    )

    status = Column(
        String(20),
        default="CONFIRMED",
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="bookings"
    )

    event = relationship(
        "Event",
        back_populates="bookings"
    )