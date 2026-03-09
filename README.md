# MCO Inventory System

The **MCO (Maintenance Control Officer) Inventory System** is a backend REST API for managing military weapon component inventory. It tracks the full lifecycle of weapons and their parts using a four-level hierarchical model:

```
Gun → Major Assembly → Sub Assembly → Component
```

**Example:**
```
Gun: AK-47
 └── Major Assembly: Barrel Assembly
        └── Sub Assembly: Gas System
               └── Component: Gas Piston
```

## Key Features

- **Hierarchical inventory management** — track weapons down to individual replaceable parts
- **Lifecycle tracking** — monitor the status and history of each component
- **Audit logging** — record all inventory actions for accountability
- **Role-based access control** — restrict operations by user role
- **QR code support** — generate and scan QR codes for components
- **Reporting** — generate inventory summaries and status reports
- **Auto-generated API docs** — interactive Swagger UI and ReDoc at `/docs` and `/redoc`

## Tech Stack

| Layer | Technology |
| --- | --- |
| Backend Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | PostgreSQL (Supabase) |
| Migration Tool | Alembic |
| API Server | Uvicorn |
| Environment Config | python-dotenv |

---

# Backend Setup

This repository contains the backend for the **MCO Inventory Management System**, built with **FastAPI, PostgreSQL, SQLAlchemy, and Alembic**.

---

## Prerequisites

Make sure you have the following installed:

* Python 3.10+
* Git
* pip
* Virtual environment support

---

## 1. Clone the Repository

```bash
git clone https://github.com/<your-org>/mco-inventory-system.git
cd mco-inventory-system/backend
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create Environment File

Copy the example environment file:

### Windows

```bash
copy .env.example .env
```

### Linux / Mac

```bash
cp .env.example .env
```

Now open `.env` and fill in the required values.

Example:

```
DATABASE_URL=postgresql://username:password@host:port/database
```

The actual database credentials will be shared separately.

---

## 5. Run Database Migrations

Apply the latest database schema:

```bash
alembic upgrade head
```

This will create the required tables in the database.

---

## 6. Start the Backend Server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Project Structure

```
backend
│
├── app
│   ├── api
│   ├── core
│   ├── database
│   ├── models
│   └── services
│
├── alembic
│   └── versions
│
├── alembic.ini
├── requirements.txt
└── .env.example
```

---

## Important Notes

* Do **not commit `.env` files** to the repository.
* All database schema changes must be done through **Alembic migrations**.
* Always run migrations before starting the server.

---

## Development Workflow

1. Pull latest changes
2. Run migrations
3. Start the server
4. Implement features in a new branch
5. Submit a pull request
