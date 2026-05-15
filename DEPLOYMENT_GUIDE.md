# Vercel Deployment Guide for Django

## Overview
Your Django project is now configured for production deployment on Vercel with a PostgreSQL database. Follow these steps to deploy:

## Step 1: Set Up a PostgreSQL Database (Free)

### Option A: Neon (Recommended - Free PostgreSQL)
1. Go to https://neon.tech/ and sign up (free account)
2. Create a new project
3. Copy your connection string (looks like: `postgresql://user:password@host:port/dbname`)

### Option B: Vercel PostgreSQL Add-on (Paid, but easier integration)
1. In your Vercel project settings, add a PostgreSQL database

## Step 2: Prepare Your GitHub Repository

1. Initialize git in your project (if not already done):
   ```bash
   cd c:\Users\famwa\Meta-Web
   git init
   git add .
   git commit -m "Initial commit: Django project ready for Vercel deployment"
   ```

2. Create a `.env` file locally (for development):
   ```bash
   cp .env.example .env
   ```
   
3. Edit `.env` and add your local database URL (for local development)

4. Add `.env` to `.gitignore` (don't commit secrets):
   ```bash
   echo ".env" >> .gitignore
   echo "*.sqlite3" >> .gitignore
   echo "staticfiles/" >> .gitignore
   echo "__pycache__/" >> .gitignore
   echo ".DS_Store" >> .gitignore
   ```

5. Push to GitHub:
   - Create a new repository on GitHub (https://github.com/new)
   - Name it something like "meta-web" (or your preference)
   - Add the remote and push:
     ```bash
     git remote add origin https://github.com/YOUR_USERNAME/meta-web.git
     git branch -M main
     git push -u origin main
     ```

## Step 3: Deploy to Vercel

1. Go to https://vercel.com and sign up (free)
2. Click "New Project"
3. Select "Import Git Repository"
4. Choose your GitHub repository
5. Click "Import"

## Step 4: Configure Environment Variables in Vercel

1. In the Vercel project, go to **Settings → Environment Variables**
2. Add the following variables:

   | Variable | Value | Notes |
   |----------|-------|-------|
   | `DEBUG` | false | Never set to true in production |
   | `SECRET_KEY` | [Generate a new one](#generate-secret-key) | Generate a secure key |
   | `ALLOWED_HOSTS` | your-project.vercel.app | Replace with your actual domain |
   | `DATABASE_URL` | postgresql://... | Your Neon connection string |

3. Click "Save"

## Step 5: Deploy

1. After setting environment variables, click "Deploy"
2. Wait for the deployment to complete (2-5 minutes)
3. Your app will be live at: `https://your-project-name.vercel.app`

## Troubleshooting

### Check Deployment Logs
1. In Vercel dashboard, click your project
2. Go to **Deployments** tab
3. Click the latest deployment
4. View **Function Logs** to debug issues

### Common Issues

**Database Connection Error:**
- Verify DATABASE_URL is correctly set in Environment Variables
- Check Neon credentials are correct
- Ensure your IP is whitelisted (if required by your DB provider)

**Static Files Not Loading:**
- Run manually: `python manage.py collectstatic --noinput`
- Check STATIC_URL and STATIC_ROOT in settings.py

**502 Error (Application Error):**
- Check the Function Logs
- Verify all dependencies in requirements.txt
- Ensure migrations have run successfully

### Test Your Deployment

1. Visit: `https://your-project.vercel.app`
2. Check admin panel: `https://your-project.vercel.app/admin`
3. Try submitting data to verify database connection

## Advanced: Custom Domain

1. In Vercel dashboard, go to **Settings → Domains**
2. Add your custom domain
3. Follow Vercel's instructions to update DNS records
4. Update `ALLOWED_HOSTS` in Vercel environment variables

## Next Steps

- Set up a custom domain (optional)
- Configure email for password resets (add email backend)
- Set up monitoring and alerting
- Consider adding a CDN for faster static file delivery
- Set up GitHub Actions for automated deployments

## Generate Secret Key

For a new SECRET_KEY, use Django's utility:

```bash
python manage.py shell
```

Then in the shell:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Copy the output and use it as your SECRET_KEY in Vercel environment variables.

## Useful Commands for Troubleshooting

```bash
# Test locally with production settings
DEBUG=False python manage.py runserver

# Check migrations
python manage.py showmigrations

# Run specific migration
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
```

---
**Last Updated**: May 2026
