# Netlify Deployment Guide for ShriramPortfolio

This project is fully configured to run Django on **Netlify** using **Serverless WSGI Functions** and connects directly to your **Google Cloud SQL (MySQL)** database.

---

## Step 1: Whitelist Netlify in Google Cloud SQL (Crucial!)

Because Netlify serverless functions run on dynamic AWS IP addresses, Cloud SQL must allow connections from any IP:

1. Open **Google Cloud Console**: [https://console.cloud.google.com/sql/instances](https://console.cloud.google.com/sql/instances)
2. Select your MySQL instance (`Portfoliodb` / `34.100.184.249`).
3. In the left navigation, click **Connections** -> **Networking** tab.
4. Under **Authorized networks**, click **Add Network**:
   - **Name**: `Netlify`
   - **Network**: `0.0.0.0/0`
5. Click **Save**.

---

## Step 2: Push your Code to GitHub

Open PowerShell or Command Prompt in `c:\ThiranexWebsite\PersonalPortfolio` and run:

```bash
git add .
git commit -m "Configure Django for Netlify serverless deployment"
git push origin main
```

---

## Step 3: Deploy on Netlify

### Option A: Via Netlify Web Dashboard (Easiest)

1. Log in to [Netlify](https://app.netlify.com/).
2. Click **Add new site** -> **Import an existing project**.
3. Choose **GitHub** and authorize access.
4. Select your repository: **`StarShree/ThiranaxeWebsite`**.
5. Netlify will automatically detect the settings from `netlify.toml`:
   - **Base directory**: *(Leave blank)*
   - **Build command**: `python -m pip install --upgrade pip && pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Publish directory**: `public`
   - **Functions directory**: `netlify/functions`
6. Click **Deploy Site**.

### Option B: (Optional) Set Environment Variables in Netlify

Your `settings.py` already contains the fallback defaults, but you can explicitly set them in Netlify:
- Go to your site dashboard on Netlify -> **Site configuration** -> **Environment variables**.
- Add the following:
  - `DEBUG`: `False`
  - `SECRET_KEY`: `django-insecure-e%6-64q9(8&7=m&j5x7v1*l@a#8f0_y)c!z4g@2q_p-3+k_r1!`
  - `DB_NAME`: `Portfoliodb`
  - `DB_USER`: `root`
  - `DB_PASSWORD`: `AppEtite123!`
  - `DB_HOST`: `34.100.184.249`
  - `DB_PORT`: `3306`

---

## What We Configured For You

- [x] **`netlify/functions/api.py`**: AWS Lambda serverless WSGI handler with PyMySQL database patching.
- [x] **`netlify.toml`**: Automatic static file publishing to CDN, Python 3.11 build environment, and function routing.
- [x] **`runtime.txt`**: Pins Python to `3.11` on Netlify build runners.
- [x] **`requirements.txt`**: Added `serverless-wsgi>=3.1.0` and `werkzeug>=3.0.0`.
- [x] **`settings.py`**: Updated `CSRF_TRUSTED_ORIGINS` for `*.netlify.app` and configured `CONN_MAX_AGE=0` for serverless DB pooling.
