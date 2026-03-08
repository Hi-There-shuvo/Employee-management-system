# 🏢 Employee Management System (EMS)

A full-stack web application built with **Django** for managing employees, departments, attendance, leaves, and salaries within an organization. Features role-based access control for Admin and Employee users.

---

## ✨ Features

### Admin Panel
- 📊 **Dashboard** — Summary stats, department bar chart, attendance doughnut chart, pending leave requests
- 👥 **Employee Management** — Create, view, edit, delete employees with profile pictures
- 🏗️ **Department Management** — Create, edit, delete departments with employee counts
- 📅 **Attendance Tracking** — View all records, filter by employee name, status, and date
- 📝 **Leave Management** — View all leave requests, approve/reject with remarks
- 💰 **Salary Management** — Add salary records for employees

### Employee Portal
- 👤 **My Profile** — View and update personal profile information
- ⏰ **Attendance** — Check in/out with automatic late detection (after 9:00 AM)
- 🗓️ **Leave Application** — Apply for sick, casual, annual, or other leave types
- 💵 **My Salary** — View personal salary history

### Security & Access
- 🔐 Role-based access control with custom decorators (`@admin_required`, `@login_required`)
- 🔑 Password change functionality for all users
- 🪤 Honeypot fake admin panel at `/admin/` for security

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0 (Python) |
| Database | SQLite |
| Frontend | HTML, CSS, Bootstrap 5 |
| Icons | Bootstrap Icons |
| Charts | Chart.js |
| Typography | Inter (Google Fonts) |

---

## 📁 Project Structure

```
Managementwebapp/
├── accounts/          # Login, logout, password change, decorators
├── employees/         # Employee CRUD, profiles, salary management
├── departments/       # Department CRUD
├── attendance/        # Check-in/out, admin attendance overview
├── leaves/            # Leave application & admin approval workflow
├── dashboard/         # Admin dashboard with stats & charts
├── ems_project/       # Django project settings & root URLs
├── templates/         # All HTML templates
├── static/            # CSS & JavaScript files
├── media/             # Uploaded profile pictures
└── manage.py
```

---

## 🚀 Setup & Installation

### Prerequisites
- Python 3.10+
- pip

### Steps

1. **Clone the repository**
   ```bash
   https://github.com/Hi-There-shuvo/Employee-management-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install django pillow
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open in browser**
   - Application: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin Panel: [http://127.0.0.1:8000/matha/](http://127.0.0.1:8000/matha/)

---

## 📸 Screenshots

<!-- Add your screenshots here -->
<!-- ![Dashboard](screenshots/dashboard.png) -->
<!-- ![Employee List](screenshots/employees.png) -->
<!-- ![Attendance](screenshots/attendance.png) -->

---

## 👥 User Roles

| Feature | Admin | Employee |
|---|---|---|
| Dashboard | ✅ | ❌ |
| Manage Employees | ✅ Full CRUD | View/edit own profile |
| Manage Departments | ✅ Full CRUD | ❌ |
| Attendance | ✅ View all | Check in/out, view own |
| Leaves | ✅ Approve/reject | Apply, view own |
| Salary | ✅ Add records | View own |
| Change Password | ✅ | ✅ |

---

## 📄 License

This project is developed as part of the CSE-3100 course.
