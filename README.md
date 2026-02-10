# FastAPI Backend Boilerplate

[English](./README.md) - [Russian](./translations/README.ru-RU.md) - [Ukrainian](./translations/README.ua-UA.md)

## 📌 About the Project

**FastAPI Backend Boilerplate** is a base template for a backend application built with FastAPI, designed to quickly bootstrap API service development with clean architecture and full database control.

The project helps you:

- Quickly launch a production-ready backend
- Build APIs with clear separation of concerns
- Work with PostgreSQL using SQLAlchemy Core without ORM
- Use an existing database (tables, functions, views)
- Build scalable backend systems with transparent business logic
- Centralize configuration and security (JWT, secrets, ENV)

---

## 🧰 Tech Stack

The project uses a modern asynchronous stack:

- **FastAPI** — web framework for building APIs  
- **Uvicorn** — ASGI server  
- **Pydantic** — data validation and DTOs  
- **SQLAlchemy Core (async)** — database access without ORM  
- **asyncpg** — asynchronous PostgreSQL driver  
- **PostgreSQL** — primary database  
- **python-jose** — JWT authentication  
- **python-dotenv** — environment variable management  

---

## 🏗 Architecture

The project follows a **Layered Architecture**:

### 1. API Layer (Presentation)

- FastAPI Routers  
- Controllers  
- Input validation using Pydantic  
- HTTP response formatting  
- Authentication and authorization  

### 2. Service Layer (Business Logic)

- Core business logic  
- Operation orchestration  
- Transaction management  
- Repository interaction  
- Domain error handling  

### 3. Repository Layer (Data Access)

- Pure database access  
- Uses **SQLAlchemy Core (without ORM)**  
- Maximum SQL control  
- Works with database functions, views, and raw SQL  
- Asynchronous queries  

---

## 📦 Database Approach

Key architectural principles:

- Tables are **created directly in the database**
- Migrations are executed outside the backend
- Business logic may partially reside in PostgreSQL functions
- Backend **does not manage the database schema**
- SQLAlchemy is used **only to reflect the existing structure**
- ORM is intentionally avoided for full SQL control

This makes the backend:

- Deterministic  
- Predictable  
- Suitable for enterprise / DB-driven architectures  
- Independent from migration tools  

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repo_url>
cd project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # Linux / Mac
.venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create an environment file using `.env.example` as a template.

```dotenv
# FastAPI Configuration
FASTAPI_SECRET="your_fastapi_secret"

# JWT configuration
JWT_SECRET="your_jwt_secret"
JWT_ALGORITHM="HS256"
JWT_EXPIRATION_MINUTES="120"

# Database configuration
DB_HOST="localhost"
DB_PORT="5432"
DB_USER="your_user"
DB_PASSWORD="your_password"
DB_NAME="your_db_name"
```

---

## 🔧 Configuration (config.py)

Configuration is centralized and loaded from `.env.dev`.

Main settings include:

- **Database** — PostgreSQL connection  
- **SQLAlchemy** — connection pool and reflection schemas  
- **PythonJose** — JWT configuration  
- **FastAPI** — API metadata  
- **dotenv** — environment loading  

---

## ▶️ Running the Application

Run the server using Uvicorn:

```bash
uvicorn main:app --reload
```

The server will be available at:

```
http://127.0.0.1:8000
```

---

## 📘 OpenAPI Documentation

- Swagger UI → http://127.0.0.1:8000/docs  
- ReDoc → http://127.0.0.1:8000/redoc  
