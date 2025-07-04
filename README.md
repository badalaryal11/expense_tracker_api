# Django Expense Tracker API

A REST API for tracking personal expenses and income, built with Django and Django REST Framework. This project includes user authentication, CRUD operations for financial records, and automatic tax calculations.

## Core Features

- **User Authentication**: Secure user registration and login using JWT (JSON Web Tokens).
- **Access Control**:
  - Regular users can only manage their own records.
  - Superusers can manage all records across the system.
- **CRUD Operations**: Full Create, Read, Update, and Delete functionality for expense/income records.
- **Automatic Tax Calculation**: Supports both flat and percentage-based tax calculations on records.
- **Pagination**: API responses for lists are paginated for efficient data handling.

## Technical Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: djangorestframework-simplejwt
- **Database**: SQLite (for development)
- **Python**: 3.8+

---

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

### 1. Prerequisites

- Python 3.8 or newer
- `pip` package manager

### 2. Clone the Repository (if you haven't already)

```bash
git clone <your-repository-url>
cd expense_tracker_api
```

### 3. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### 4. Install Dependencies

Install all the required packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

This command creates the necessary database tables, including the user and `ExpenseIncome` models.

```bash
python manage.py migrate
```

### 6. Create a Superuser

A superuser is required to access the Django admin panel and test superuser-specific API permissions.

```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### 7. Run the Development Server

You're all set! Start the Django development server.

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`. You can now use a tool like Postman or `curl` to interact with the API endpoints.

---

## Next Steps

1.  **Register a new user**: `POST /api/auth/register/`
2.  **Log in**: `POST /api/auth/login/` to get your JWT access token.
3.  **Access protected endpoints**: Include the access token in the `Authorization` header as `Bearer <your_token>`.