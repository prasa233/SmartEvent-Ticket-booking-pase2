from fastapi import FastAPI

from .database import Base, engine

from .routers import (
    auth,
    events,
    admin
)

Base.metadata.create_all(bind=engine)



app = FastAPI(
    title="SmartEvent API",
    description="SmartEvent Event Discovery & Ticket Booking Platform",
    version="3.0.0"
)


app.include_router(
    auth.router
)

app.include_router(
    events.router
)

app.include_router(
    admin.router
)


@app.get("/")
def root():

    return {
        "message": "SmartEvent API is running",
        "version": "Phase 2"
    }