# FastAPI CRUD Examples

This repository contains **multiple FastAPI backend example projects**, created for learning and practice purposes.  
Each project demonstrates a different approach to data handling, from simple JSON-based storage to PostgreSQL and external public API integration.

The goal of this repository is to show the **progressive evolution of a backend application**, starting with basic concepts and moving toward more realistic, production-oriented architectures.

---

## 🚀 Projects Included

### 📁 1. FastAPI CRUD with JSON

A beginner-friendly CRUD API using a **JSON file as a mock database**.

**Key concepts:**

- FastAPI fundamentals
- CRUD operations
- File-based persistence

---

### 📁 2. FastAPI CRUD with PostgreSQL

A CRUD API using **PostgreSQL** as a relational database.

**Key concepts:**

- Database connections
- Data modeling
- Pydantic schemas
- SQL-based persistence

---

### 📁 3. FastAPI + Public API Integration (Agify)

A FastAPI project that **consumes a public API** and stores the retrieved data in **PostgreSQL**.

Public API used:

```
https://api.agify.io/?name={name}
```

**Key concepts:**

- Consuming external REST APIs
- Handling third-party API responses
- Persisting external data into PostgreSQL
- Real-world backend integration patterns

## 🛠️ Technologies Used

- Python
- FastAPI
- Uvicorn
- JSON (mock database)
- PostgreSQL
- psycopg / SQL tools (depending on implementation)

---

## ▶️ How to Run the Project

#### 1. Clone the repository:

```
git clone https://github.com/Kevin-Mart/FastAPI-CRUD-Example-with-JSON-Database.git
```

#### 2. Move into the backend directory:

```
cd backend
```

#### 3. Create and activate a virtual environment (optional but recommended)

#### 4. Install dependencies:

```
pip install fastapi uvicorn
```

#### 5. Run the application:

```
uvicorn app.main:app --reload
```

#### 6. Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

to access the interactive Swagger UI.

### ⚠️ Disclaimer

This project is not intended for production use.
Using a JSON file as a database is only suitable for testing and learning scenarios.
