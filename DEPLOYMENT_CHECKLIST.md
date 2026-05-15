# Quick Deployment Checklist

## Pre-Deployment ✓ (Complete These First)

- [ ] Create `.env` file from `.env.example`
- [ ] Update Django settings for production (✓ Done - see settings.py)
- [ ] Set up PostgreSQL database on Neon (https://neon.tech)
- [ ] Initialize Git repository
- [ ] Create GitHub repository and push code
- [ ] Update `.gitignore` (see below)

## Deployment Steps

1. **Create Vercel Account**
   - Go to https://vercel.com
   - Sign up with GitHub

2. **Deploy Project**
   - New Project → Import Git Repository
   - Select your repository
   - Click "Import"

3. **Set Environment Variables** (Critical!)
   - Go to Settings → Environment Variables
   - Add:
     - `DEBUG=false`
     - `SECRET_KEY=[generate new one]`
     - `ALLOWED_HOSTS=your-app.vercel.app`
     - `DATABASE_URL=postgresql://...` (from Neon)
   - Save and Redeploy

4. **Test Deployment**
   - Visit your-app.vercel.app
   - Check admin panel at /admin
   - Test database operations

## Important Files Created/Modified

| File | Purpose |
|------|---------|
| `requirements.txt` | Updated with PostgreSQL driver & production dependencies |
| `atemksam/settings.py` | Updated for production (env vars, whitenoise, PostgreSQL) |
| `vercel.json` | Updated Vercel configuration |
| `.env.example` | Template for environment variables |
| `build.sh` | Build script for Vercel |
| `DEPLOYMENT_GUIDE.md` | Full deployment documentation |

## Generate Secret Key

```bash
python manage.py shell
```

In Python shell:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Copy the output and paste as `SECRET_KEY` in Vercel environment variables.

## Free Services Used

- **Vercel**: Hosting (free tier: 1 project, 100GB bandwidth/month)
- **Neon**: PostgreSQL database (free tier: 3 projects, 10GB storage)
- **GitHub**: Code repository (free)

This setup is completely free and production-ready! 🚀
