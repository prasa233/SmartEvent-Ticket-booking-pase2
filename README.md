
# SmartEvent – Phase 2

## Project Overview

SmartEvent is a full-stack Event Discovery and Ticket Booking Platform developed using FastAPI, SQLAlchemy, SQLite, React, and Vite. Phase 2 introduces role-based access control, organizer event management, and admin analytics.

## Technology Stack

* **Backend:** Python, FastAPI, SQLAlchemy, SQLite
* **Frontend:** React, Vite, Tailwind CSS
* **Authentication:** JWT
* **Validation:** Pydantic

## Key Features

### 1. Role-Based Access Control (RBAC)

* **USER:** Browse events, book tickets, view bookings and tickets.
* **ORGANIZER:** Create, update, cancel, and manage owned events.
* **ADMIN:** Manage users, events, bookings, and analytics.

### 2. Organizer Event Management

* Create, edit, and cancel events.
* View organizer-owned events.
* View event bookings.
* Validate event ownership.

### 3. Organizer Analytics

* Total tickets sold.
* Remaining tickets.
* Booking statistics.
* Revenue summaries.

### 4. Event Lifecycle

* Track event status: `UPCOMING`, `ONGOING`, `COMPLETED`, `CANCELLED`.
* Notify users about event updates and cancellations.

### 5. Admin Dashboard

* View all users, events, and bookings.
* Display total users, events, bookings, and revenue.
* Analyze daily ticket sales and monthly booking trends.
* Identify popular events and top revenue-generating events.

## Main API Endpoints

| Method    | Endpoint                       | Purpose                  |
| --------- | ------------------------------ | ------------------------ |
| POST      | `/api/auth/register`           | Register user            |
| POST      | `/api/auth/login`              | Login                    |
| GET       | `/api/auth/me`                 | Current user             |
| GET       | `/api/events`                  | Browse events            |
| POST      | `/api/events`                  | Create event (Organizer) |
| PUT/PATCH | `/api/events/{event_id}`       | Update event             |
| DELETE    | `/api/events/{event_id}`       | Cancel event             |
| GET       | `/api/organizer/insights`      | Organizer analytics      |
| GET       | `/api/admin/users`             | View users               |
| GET       | `/api/admin/events`            | View all events          |
| GET       | `/api/admin/bookings`          | View all bookings        |
| GET       | `/api/admin/analytics?days=30` | Admin analytics          |

## Database Updates

* **Users:** Add `role`.
* **Events:** Add `organizer_id` and `event_status`.
* **Existing tables:** Users, Events, Bookings, Tickets, Notifications.

## Installation and Setup

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python -m uvicorn app.main:app --reload
```

Backend:  http://127.0.0.1:8000

Swagger documentation:  http://127.0.0.1:8000/docs

### Frontend

Open a second terminal:

```bash
cd frontend
npm install
npm run dev
```


## Security

* JWT authentication for protected endpoints.
* Validate user roles against the current database role.
* Restrict organizer actions to owned events.
* Allow analytics access only to administrators.
* Validate input using Pydantic.
* Store secrets securely in `.env`.

## Expected Workflow

1. Organizer logs in and creates an event.
2. Organizer manages events and views ticket sales.
3. Users browse events and book tickets.
4. Users receive notifications about event updates.
5. Admin views users, events, bookings, and analytics.

## Project Objective

To build a secure, multi-role event platform with event management, ticket booking, notifications, and administrative analytics.
