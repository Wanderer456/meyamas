# Quick Start: Deploy to Vercel Now (No GitHub)

## You're Ready! Here's What to Do Next:

### 1. **Install Vercel CLI**
Open PowerShell and run:
```bash
npm install -g vercel
```

### 2. **Login to Vercel**
```bash
vercel login
```

### 3. **Deploy Your Project**
```bash
cd c:\Users\famwa\Meta-Web
vercel
```

During the wizard:
- Answer `y` to "Set up and deploy?"
- Choose your account
- Answer `n` to "Link to existing project?"
- Name your project (e.g., `meta-web`)
- Answer `n` to "Want to modify these settings?"

**That's it! Your app is deployed!** 🎉

---

## 4. **Get Your Free Database (Neon)**

1. Go to https://neon.tech and sign up (free)
2. Create a new PostgreSQL project
3. Copy your connection string (starts with `postgresql://`)

---

## 5. **Add Environment Variables**

1. Go to https://vercel.com/dashboard
2. Click your project
3. Go to **Settings** → **Environment Variables**
4. Add:
   - `DJANGO_DEBUG` = `False`
   - `SECRET_KEY` = `&-nkk-+5v*r3_^ky^)+e59euei%mr#)3jaa4!c!zys$n1*z%u-`
   - `ALLOWED_HOSTS` = `your-project-name.vercel.app`
   - `DATABASE_URL` = [Your Neon connection string]
5. Save and **Redeploy** from Deployments tab

---

## 6. **Test Your Live Site**

Visit: `https://your-project-name.vercel.app` ✅

Admin: `https://your-project-name.vercel.app/admin`
- Username: `admin`
- Password: `admin123`

---

## Future Updates

After making changes locally, just run:
```bash
vercel --prod
```

That's all! No GitHub needed ever. 🚀
