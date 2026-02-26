User Management API
This project is a RESTful User Management API built using FastAPI and PostgreSQL. It supports
complete CRUD operations with proper validation, password hashing, and clean project
architecture following backend best practices.
Tech Stack
• FastAPI - Web framework
• PostgreSQL - Database
• SQLAlchemy - ORM
• Pydantic - Data validation
• Passlib (bcrypt) - Password hashing
• Uvicorn - ASGI server
Features
• Create User
• Get All Users
• Get Single User by ID
• Update User
• Delete User
• Email uniqueness validation
• Password hashing before storage
• Automatic Swagger documentation
Setup Instructions
1. Clone the repository. 2. Create a virtual environment and activate it. 3. Install dependencies
using pip install -r requirements.txt. 4. Create a PostgreSQL database. 5. Update DATABASE_URL
inside database.py. 6. Run the server using: uvicorn app.main:app --reload. 7. Open
http://127.0.0.1:8000/docs to access Swagger UI.
Database Schema (users table)
• id - Integer (Primary Key)
• name - String
• email - String (Unique)
• password - String (Hashed)
• is_active - Boolean (Default True)
• created_at - Timestamp
Project Architecture
The project follows a clean modular structure: - main.py handles app initialization. - database.py
manages database connection. - models.py defines database tables. - schemas.py validates
request/response data. - crud.py contains database operations. - routers/user.py defines API
endpoints. This separation ensures maintainability and scalability.
This project demonstrates backend development skills including API design, database integration,
password security, error handling, and proper project structuring using FastAPI and PostgreSQL.
