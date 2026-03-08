# Employee Management System

A comprehensive, production-ready Employee Management System built with Django, featuring cloud database integration (Neon DB) and external media storage (Cloudinary).

![Project Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.13-success)
![Django](https://img.shields.io/badge/Django-5.2.7-success)
![Render](https://img.shields.io/badge/Deployed_on-Render-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🔗 Live Application
**Live Demo:** [https://employee-management-system-m4dk.onrender.com](https://employee-management-system-m4dk.onrender.com)

---

## ✨ Features
* **Employee Directory:** comprehensive management of employee profiles.
* **Attendance Tracking:** Keep secure records of employee check-ins/outs.
* **Leave Management:** Employees can request leaves with admin approvals.
* **Department Sorting:** Classify and filter employees by department.
* **Salary Tracking:** Secure management and viewing of payroll information.
* **Profile Pictures (Cloud Media):** Employee avatars are reliably hosted remotely via Cloudinary integration.
* **Secure Honeypot Admin:** Custom fake admin login page to trap unauthorized access attempts.

---

## 🛠️ Tech Stack
* **Backend:** Python + Django
* **Database:** PostgreSQL (Hosted on Neon DB) / SQLite3 (Local)
* **Storage:** Cloudinary (Media), WhiteNoise (Static Assets)
* **Deployment:** Render + Gunicorn

---

## 🚀 Local Deployment Setup

To clone and run this project locally, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/Hi-There-shuvo/Employee-management-system.git
cd Employee-management-system
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file
Create a new file named `.env` in the root directory:
```env
ENVIRONMENT=development
SECRET_KEY=your-local-secret-key-xyz123
DATABASE_URL=postgres://neondb_owner:... # Get this from Neon
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```
*(Note: As `ENVIRONMENT` is set to `development`, the project will temporarily ignore PostgreSQL limits and Cloudinary storage to boost your local development speed).*

### 5. Run Migrations & Start Server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open `http://localhost:8000` to view the application.

---

## 👨‍💻 Developer Information

Built and maintained by **[Mia Shuvo](https://github.com/Hi-There-shuvo)**. 

If you find this project helpful or insightful, please consider leaving a ⭐ on the repository!
