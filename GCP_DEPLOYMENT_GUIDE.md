# Google Cloud Run & Cloud SQL Deployment Guide

This guide walks you step-by-step through deploying **ShriramPortfolio** to **Google Cloud Run** connected to your existing **Google Cloud SQL (MySQL)** database using the Google Cloud Console and Cloud Shell.

---

## 📦 What Was Prepared Locally
All files required by Google Cloud have been configured in your project:
1. **`Dockerfile`**: Container definition using `python:3.11-slim`, `gunicorn`, and static assets pre-collection.
2. **`requirements.txt`**: Includes `Django`, `mysqlclient`, `pymysql`, `gunicorn`, `whitenoise`, and `cryptography`.
3. **`portfolio_project/settings.py`**:
   - `ALLOWED_HOSTS = ["*"]`
   - `CSRF_TRUSTED_ORIGINS = ["https://*.run.app"]`
   - `WhiteNoiseMiddleware` configured for static file serving.
   - Dual-mode database connection supporting both Cloud Run Unix Sockets (`/cloudsql/...`) and direct TCP IP (`34.100.184.249`).
4. **`ShriramPortfolio.zip`**: Pre-built 510 KB zip file ready for upload (located at `c:\ThiranexWebsite\PersonalPortfolio\ShriramPortfolio.zip`).

---

## 🚀 Step 1: Upload to Google Cloud via Cloud Shell

1. Open the [Google Cloud Console](https://console.cloud.google.com/).
2. Click the **Activate Cloud Shell** button (`>_`) in the top-right toolbar.
3. In the Cloud Shell window, click the **Three Dots (⋮)** menu in the top right of the terminal and select **Upload**.
4. Choose the file:
   `c:\ThiranexWebsite\PersonalPortfolio\ShriramPortfolio.zip`
5. Once uploaded, run the following commands in Cloud Shell:
   ```bash
   unzip ShriramPortfolio.zip -d django-app
   cd django-app
   ```

---

## 🔨 Step 2: Build the Container Image Using Cloud Build

In the Cloud Shell terminal, run:
```bash
PROJECT_ID=$(gcloud config get-value project)
gcloud builds submit --tag gcr.io/$PROJECT_ID/django-app:v1
```
> *This uploads the source code to Cloud Build, compiles the container, and stores it in your Google Container Registry.*

---

## 🌐 Step 3: Deploy the App in Cloud Run

1. In the Google Cloud Console top search bar, type **Cloud Run** and click on it.
2. Click **Deploy Container** (or **Create Service**).
3. Under **Container image URL**, click **Select** and choose:
   `gcr.io/<your-project-id>/django-app:v1`
4. Configure basic settings:
   - **Service Name**: `shriram-portfolio` (or `django-app`)
   - **Region**: Select the region matching your Cloud SQL database (e.g. `asia-south1`, `us-central1`, etc.)
   - **Authentication**: Select **Allow unauthenticated invocations** (makes the portfolio public).
5. Scroll down and expand **Container, Volumes, Networking, Security**:
   - **Cloud SQL connections**: Click **Add Connection** and select your MySQL database instance from the dropdown.
   - **Environment Variables**: Click **Add Variable** for each of the following:
     | Name | Value |
     |---|---|
     | `DB_NAME` | `Portfoliodb` |
     | `DB_USER` | `root` |
     | `DB_PASSWORD` | `AppEtite123!` |
     | `CLOUD_SQL_CONNECTION_NAME` | *Your instance connection name from SQL overview (e.g. `project:region:instance`)* |
     | `SECRET_KEY` | `django-insecure-shriram-portfolio-prod-key-xyz789` |
     | `DEBUG` | `False` |
6. Click **Create**.
7. After 1–2 minutes, Cloud Run will display your public live URL (e.g., `https://shriram-portfolio-xyz.a.run.app`).

---

## 🗄️ Step 4: Run Migrations on Cloud Run (Optional / Verification)
Since your Cloud SQL database is already migrated and seeded, the live website will display all data immediately!

If you ever need to apply new schema migrations directly from Cloud Shell in the future, run:
```bash
gcloud run jobs create django-migrate \
  --image gcr.io/$PROJECT_ID/django-app:v1 \
  --region <YOUR_REGION> \
  --add-cloudsql-instances <INSTANCE_CONNECTION_NAME> \
  --set-env-vars CLOUD_SQL_CONNECTION_NAME="<INSTANCE_CONNECTION_NAME>",DB_NAME="Portfoliodb",DB_USER="root",DB_PASSWORD="AppEtite123!" \
  --command python \
  --args manage.py,migrate

gcloud run jobs execute django-migrate --region <YOUR_REGION>
```

---

## 🎉 Done!
Your personal portfolio will be live 24/7 on Google Cloud Run with automatic HTTPS, autoscaling, and live connection to your Google Cloud SQL database.
