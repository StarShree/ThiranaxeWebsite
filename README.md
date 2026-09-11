# Full-Stack Personal Portfolio Website

A production-grade, highly aesthetic personal portfolio website built with **Django 6.1** and directly integrated with **Google Cloud SQL (MySQL 8.0)**.

![Google Cloud SQL](https://img.shields.io/badge/Database-Google%20Cloud%20SQL%20MySQL-4285F4?logo=google-cloud&logoColor=white)
![Django](https://img.shields.io/badge/Backend-Django%206.1-092E20?logo=django&logoColor=white)
![HTML5/CSS3/JS](https://img.shields.io/badge/Frontend-Vanilla%20CSS%20%2B%20ES6%20JS-E34F26?logo=html5&logoColor=white)

---

## 🌟 Key Features

- **Dynamic Backend**: Built with Django and connected to Google Cloud SQL (MySQL 8.0) using `PyMySQL` and `cryptography`.
- **Live Cloud SQL Telemetry**: Real-time connectivity monitor in the navigation bar and footer displaying live database status.
- **Modern Glassmorphic Dark UI**: Custom-built CSS styling with vibrant cyan/indigo/violet gradients, ambient background orbs, smooth micro-interactions, and responsive layouts.
- **Projects Showcase**: Filterable by domain (*Full Stack*, *Cloud & DevOps*, *Backend & APIs*, *Frontend UI*) with interactive modal previews.
- **Interactive Contact Inquiries**: AJAX-powered contact form that stores submissions directly into the `portfolio_contactmessage` MySQL table with instant toast feedback.
- **Django Admin Suite**: Pre-configured admin dashboard to manage projects, skills, profile details, and inquiries at `/admin/`.
- **Standalone SQL Scripts**: Includes complete DDL (`sql/schema.sql`) and DML (`sql/seed_data.sql`) scripts for direct database management.

---

## 🗄️ Database Credentials (Google Cloud SQL)

| Setting | Value |
|---|---|
| **Host** | `34.100.184.249` |
| **Port** | `3306` |
| **Database** | `Portfoliodb` |
| **Username** | `root` |
| **Password** | `AppEtite123!` |
| **Engine** | MySQL 8.0 |

---

## 🚀 Getting Started

### 1. Environment Setup
Activate the virtual environment:
```powershell
# Windows
.\.venv\Scripts\Activate.ps1
```

Or initialize fresh:
```bash
py -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
```

### 2. Configuration (`.env`)
The database connection is defined in `.env`:
```env
SECRET_KEY=your-secure-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,*

DB_NAME=Portfoliodb
DB_USER=root
DB_PASSWORD=AppEtite123!
DB_HOST=34.100.184.249
DB_PORT=3306
```

### 3. Database Migration & Seeding
Apply migrations to Google Cloud SQL:
```bash
python manage.py migrate
```

Populate initial portfolio data:
```bash
python manage.py seed_portfolio
```

### 4. Admin Access
A default superuser is available:
- **URL**: `http://127.0.0.1:8000/admin/`
- **Username**: `admin`
- **Password**: `AdminPass123!`

### 5. Running the Application
Start the Django development server:
```bash
python manage.py runserver 127.0.0.1:8000
```
Open your browser at: `http://127.0.0.1:8000/`

---

## 📄 Standalone SQL Scripts
If you prefer managing the database directly via MySQL Workbench, DBeaver, or MySQL CLI:
- **`sql/schema.sql`**: Full table definitions, primary keys, foreign keys, and indexes.
- **`sql/seed_data.sql`**: Complete data population inserts matching the Django models.

To run via MySQL client:
```bash
mysql -h 34.100.184.249 -P 3306 -u root -p Portfoliodb < sql/schema.sql
mysql -h 34.100.184.249 -P 3306 -u root -p Portfoliodb < sql/seed_data.sql
```

---

## 🧪 Running Automated Tests
Run Django's test suite:
```bash
python manage.py test portfolio
```
Tests will verify database connectivity, index views, contact submission, and JSON APIs.
