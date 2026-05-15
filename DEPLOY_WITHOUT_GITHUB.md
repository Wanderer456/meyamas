# Deploy to Vercel Without GitHub

## Overview
This guide shows how to deploy your Django app directly to Vercel using the Vercel CLI without requiring GitHub.

## Prerequisites
1. Vercel account (https://vercel.com - free signup)
2. Vercel CLI installed on your machine
3. A free PostgreSQL database (Neon or Vercel)

---

## Step 1: Install Vercel CLI

Open PowerShell and run:
```bash
npm install -g vercel
```

Or if you have npm/Node.js installed:
```bash
npm install --global vercel
```

---

## Step 2: Set Up Free PostgreSQL Database

### Option A: Neon (Recommended)
1. Go to https://neon.tech
2. Sign up (free account)
3. Create a new project
4. Copy your connection string: `postgresql://user:password@host:port/dbname`

### Option B: Vercel PostgreSQL (if in US region)
1. Later in the deployment process, Vercel will offer to add a database

---

## Step 3: Update .env.example for Production

Make sure your `.env.example` has deployment-ready variables:

```
DJANGO_DEBUG=False
SECRET_KEY=&-nkk-+5v*r3_^ky^)+e59euei%mr#)3jaa4!c!zys$n1*z%u-
ALLOWED_HOSTS=your-app.vercel.app
DATABASE_URL=postgresql://user:password@host:port/dbname
```

---

## Step 4: Login to Vercel

```bash
vercel login
```

You'll be prompted to login with your Vercel account. Choose your login method (GitHub, GitLab, Bitbucket, or email).

---

## Step 5: Deploy Your Project

Navigate to your project directory and run:

```bash
cd c:\Users\famwa\Meta-Web
vercel
```

### During the deploy wizard, answer:
- **Set up and deploy?** → `y` (yes)
- **Which scope?** → Select your personal account
- **Link to existing project?** → `n` (no, this is a new project)
- **What's your project's name?** → Give it a name (e.g., `meta-web`)
- **In which directory is your code?** → `.` (current directory)
- **Want to modify these settings?** → `n` (no, we already configured vercel.json)

Vercel will then:
1. Upload your entire project (no GitHub needed!)
2. Install dependencies
3. Build your app
4. Deploy it

---

## Step 6: Add Environment Variables in Vercel Dashboard

After deployment completes:

1. Go to https://vercel.com/dashboard
2. Click your project
3. Go to **Settings** → **Environment Variables**
4. Add these variables:

| Key | Value |
|-----|-------|
| `DJANGO_DEBUG` | `False` |
| `SECRET_KEY` | `&-nkk-+5v*r3_^ky^)+e59euei%mr#)3jaa4!c!zys$n1*z%u-` |
| `ALLOWED_HOSTS` | `your-app-name.vercel.app` |
| `DATABASE_URL` | `postgresql://user:pass@host/db` (from Neon) |

5. Click "Save"
6. Go to **Deployments** and click **Redeploy** on the latest build

---

## Step 7: Test Your Deployment

1. Visit: `https://your-app-name.vercel.app`
2. Test your home page
3. Try admin: `https://your-app-name.vercel.app/admin`
   - Login with: admin / admin123 (or your credentials)

---

## Step 8: Redeploy After Changes (No GitHub!)

Whenever you make changes locally:

```bash
cd c:\Users\famwa\Meta-Web
vercel --prod
```

This will push your latest code directly to production!

---

## Database Configuration

### For PostgreSQL Neon:
1. Sign up at https://neon.tech (free tier includes 10GB)
2. Create a database
3. Copy connection string and add to Environment Variables as `DATABASE_URL`

### For Local Development:
- Uses SQLite (`db.sqlite3`) automatically
- Your current `.env` file sets `DJANGO_DEBUG=True` for local dev

---

## Troubleshooting

### Function Logs Show Errors
```bash
vercel logs --tail
```

### Redeploy After Environment Variable Changes
Vercel doesn't auto-redeploy when you add env vars. Go to Deployments and click **Redeploy**.

### Database Connection Error
- Check DATABASE_URL is correct
- Verify IP whitelist in your database provider (if required)
- Run migrations: Check Function Logs for migration status

### Static Files Not Loading
- Already configured with WhiteNoise in settings.py
- If issues persist, run locally: `python manage.py collectstatic`

### Force Full Redeploy
```bash
vercel deploy --prod --force
```

---

## Summary

| Step | What | Command |
|------|------|---------|
| 1 | Install Vercel CLI | `npm install -g vercel` |
| 2 | Set up PostgreSQL | Go to https://neon.tech |
| 3 | Login to Vercel | `vercel login` |
| 4 | Deploy | `vercel` then `vercel --prod` |
| 5 | Add Env Vars | Dashboard → Settings → Environment Variables |
| 6 | Redeploy | Go to Deployments, click Redeploy |
| 7 | Future deploys | `vercel --prod` in your project folder |

---

## Commands Reference

```bash
# Initial setup
npm install -g vercel
vercel login

# Deploy
cd c:\Users\famwa\Meta-Web
vercel                          # Deploy to staging/preview
vercel --prod                   # Deploy to production

# Check status
vercel status
vercel logs --tail              # Live logs
vercel whoami                   # Check logged-in account

# For future updates (after making changes locally)
vercel --prod                   # Quick redeploy to production
```

---

**That's it!** Your Django app will be live on Vercel without ever touching GitHub. 🚀
