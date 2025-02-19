# ✅ Task Management System 

## 📌 Overview
The **Task Management System** is a web application built with Flask and SQLAlchemy. It allows users to manage tasks, track progress, and maintain an organized workflow. The system supports user authentication, task completion tracking, and role-based access control. that allows users to create, assign, and track tasks efficiently. It features user authentication, role-based access control, and task status updates, making it ideal for team collaboration.

## 🚀 Features
- ✅ **User Authentication** (JWT-based login & registration)
- ✅ **Task Management** (Create, Read, Update, Delete tasks)
- ✅ **Role-Based Access Control** (Admin & User roles)
- ✅ **Task Status Updates** (Pending, In Progress, Completed)
- ✅ **Search & Filtering** for efficient task retrieval
- ✅ **Deployed on Vercel** for live testing

## 🛠️ Tech Stack
- **Backend:** Flask, SQLAlchemy
- **User Authentication:** Flask-Login
- **Database:** PostgreSQL / SQLite
- **Migrations:** Flask-Migrate
- **Database:** SQLite / PostgreSQL
- **Authentication:** JWT (JSON Web Tokens)
- **Deployment:** Vercel

## 📂 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Imperialemmy/todolist_with-user-auth.git
cd todolist_with-user-auth
```

### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add:
```
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///tasks.db  # Use PostgreSQL for production
```

### 5️⃣ Initialize the Database
```bash
python
>>> from app import db
>>> db.create_all()
```

### 6️⃣ Start the Development Server
```bash
flask run
```

## 🌍 Deployment
The application is **live on Vercel** and can be accessed at:
🔗 [Live API URL](#) *(Replace with actual link)*

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repository, open issues, and submit pull requests.

## 📜 License
This project is licensed under the **MIT License**.

---

### 📧 Contact
For any questions or collaborations, reach out via GitHub: [Imperialemmy](https://github.com/Imperialemmy)

---

This README provides all the necessary details for users and developers to get started with your API. Let me know if you need any modifications! 🚀

