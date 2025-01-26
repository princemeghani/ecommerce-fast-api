# eCommerce API

A **FastAPI-based** backend for an **eCommerce system** that manages **products** and **orders**, ensuring data validation, stock management, and order processing.

## Features

✅ **Product Management** – Add and retrieve products.  
✅ **Order Management** – Create orders with validation for stock and pricing.  
✅ **Validation & Error Handling** – Ensures data integrity for product pricing, quantity, and stock availability.  
✅ **Database Management** – Uses **SQLAlchemy** with SQLite/PostgreSQL.  
✅ **Health Check API** – Provides a `/health` endpoint for API monitoring.  
✅ **Automated Testing** – Includes unit and integration tests with **pytest**.

## Technologies Used

- **FastAPI** – Web framework
- **SQLAlchemy** – ORM for database interactions
- **SQLite/PostgreSQL** – Database
- **Pytest** – Testing framework
- **Pydantic** – Data validation
- **Docker** – Containerization

---

## Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/princemeghani/ecommerce-fast-api.git
cd ecommerce-fast-api
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file and add database credentials:

```
DATABASE_URL=sqlite:///./test.db
```

For PostgreSQL:

```
DATABASE_URL=postgresql://user:password@localhost/ecommerce_db
```

---

## Running the API

### 🚀 Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

### 🌍 Access the API

- **Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

### 🛍️ Product Endpoints

| Method | Endpoint    | Description           |
| ------ | ----------- | --------------------- |
| `POST` | `/products` | Add a new product     |
| `GET`  | `/products` | Retrieve all products |

### 📦 Order Endpoints

| Method | Endpoint  | Description     |
| ------ | --------- | --------------- |
| `POST` | `/orders` | Create an order |

### 🛠️ Utility Endpoints

| Method | Endpoint  | Description      |
| ------ | --------- | ---------------- |
| `GET`  | `/`       | API Home         |
| `GET`  | `/health` | API Health Check |

---

## Running Tests

To run tests with **pytest**, execute:

```bash
pytest
```

## Database Migrations (Using Alembic)

1️⃣ **Initialize Alembic**

```bash
alembic init alembic
```

2️⃣ **Generate a migration**

```bash
alembic revision --autogenerate -m "Initial migration"
```

3️⃣ **Apply migrations**

```bash
alembic upgrade head
```

---

## Docker Setup

### 🛠️ Build and Run with Docker

#### 1️⃣ Build the Docker image

```bash
docker build -t ecommerce-api .
```

#### 2️⃣ Run the container

```bash
docker run -p 8000:8000 --env-file .env ecommerce-api
```

#### 3️⃣ Run container in detached mode

```bash
docker run -d -p 8000:8000 --env-file .env --name ecommerce-container ecommerce-api
```

#### 4️⃣ Stop the container

```bash
docker stop ecommerce-container
```

#### 5️⃣ Remove the container

```bash
docker rm ecommerce-container
```

#### 6️⃣ View running containers

```bash
docker ps
```

#### 7️⃣ View all containers (including stopped ones)

```bash
docker ps -a
```

#### 8️⃣ View logs from a running container

```bash
docker logs ecommerce-container
```

---

## License

This project is licensed under the **MIT License**.

---

This README is now structured, clear, and includes **Docker commands** for easy setup. Let me know if you need further modifications! 🚀
