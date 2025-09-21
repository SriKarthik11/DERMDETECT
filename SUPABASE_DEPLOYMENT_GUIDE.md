# 🚀 DermDetect Deployment with Supabase

## 🎯 Best Free Hosting Options for ML Apps

### 1. **Render.com** (Recommended)
- ✅ **Free Tier**: 750 hours/month
- ✅ **ML Support**: Handles large model files (82MB)
- ✅ **Auto-deploy**: From GitHub
- ✅ **Environment variables**: Easy setup

### 2. **Railway.app**
- ✅ **Free Tier**: $5 credit monthly
- ✅ **Simple deployment**: One-click from GitHub
- ✅ **Good performance**: Fast cold starts

### 3. **Fly.io**
- ✅ **Free Tier**: 3 shared-cpu VMs
- ✅ **Global deployment**: Edge locations
- ✅ **Docker support**: Custom configurations

## 🗄️ Supabase Setup (5 minutes)

### Step 1: Create Supabase Project
1. Go to [supabase.com](https://supabase.com)
2. Click "Start your project"
3. Create new project (choose free tier)
4. Wait for setup to complete (~2 minutes)

### Step 2: Setup Database
1. Go to **SQL Editor** in Supabase dashboard
2. Copy and paste the contents of `supabase_setup.sql`
3. Click "Run" to create tables and policies

### Step 3: Get API Keys
1. Go to **Settings** → **API**
2. Copy your **Project URL** and **anon public key**
3. Save these for deployment

## 🌐 Deployment Steps

### Option A: Deploy to Render (Recommended)

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Deploy DermDetect with Supabase"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Deploy on Render**:
   - Go to [render.com](https://render.com)
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Environment**: Python 3

3. **Add Environment Variables**:
   ```
   SUPABASE_URL=https://your-project-id.supabase.co
   SUPABASE_ANON_KEY=your-anon-key-here
   ```

### Option B: Deploy to Railway

1. **Push to GitHub** (same as above)

2. **Deploy on Railway**:
   - Go to [railway.app](https://railway.app)
   - Click "Deploy from GitHub repo"
   - Select your repository
   - Add environment variables in settings

### Option C: Deploy to Fly.io

1. **Install Fly CLI**:
   ```bash
   # Windows
   iwr https://fly.io/install.ps1 -useb | iex
   ```

2. **Deploy**:
   ```bash
   fly launch
   fly secrets set SUPABASE_URL=your-url SUPABASE_ANON_KEY=your-key
   fly deploy
   ```

## 📊 Supabase Features

### Database Tables Created:
- **analyses**: Stores all predictions with metadata
- **public_stats**: View for analytics dashboard

### API Endpoints Added:
- `/stats` - Get usage statistics
- `/recent` - Get recent analyses

### Data Collected:
- Prediction results and confidence scores
- User IP addresses (for analytics)
- Timestamps for usage tracking
- Image metadata

## 🔧 Local Development

1. **Setup environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your Supabase credentials
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally**:
   ```bash
   python app.py
   ```

## 📈 Monitoring & Analytics

### Supabase Dashboard:
- **Table Editor**: View all analyses
- **SQL Editor**: Run custom queries
- **API Logs**: Monitor usage
- **Auth**: User management (if needed later)

### Custom Analytics Queries:
```sql
-- Most common conditions
SELECT top_prediction_class, COUNT(*) as count
FROM analyses 
GROUP BY top_prediction_class 
ORDER BY count DESC;

-- Daily usage
SELECT DATE(created_at) as date, COUNT(*) as analyses
FROM analyses 
GROUP BY DATE(created_at) 
ORDER BY date DESC;

-- Average confidence by condition
SELECT top_prediction_class, AVG(top_prediction_confidence) as avg_confidence
FROM analyses 
GROUP BY top_prediction_class;
```

## 🎯 Production Checklist

- [ ] Supabase project created and configured
- [ ] Database tables created with SQL script
- [ ] Environment variables set in hosting platform
- [ ] GitHub repository created and code pushed
- [ ] Hosting platform connected to GitHub
- [ ] Logo and sample images added to `/static/`
- [ ] Test deployment with sample image
- [ ] Monitor Supabase logs for errors

## 💡 Pro Tips

1. **Model Size**: Your 82MB model works best on Render/Railway
2. **Cold Starts**: First request may be slow, subsequent ones are fast
3. **Monitoring**: Check Supabase logs for database issues
4. **Scaling**: Supabase free tier handles 50,000 requests/month
5. **Backup**: Supabase automatically backs up your data

## 🆘 Troubleshooting

### Common Issues:
- **"Supabase not available"**: Check environment variables
- **Model loading errors**: Ensure model file is in repository
- **Database connection failed**: Verify Supabase URL and key
- **Deployment timeout**: Model file might be too large for some platforms

### Solutions:
- Use Render.com for large model files
- Check Supabase project status
- Verify environment variables are set correctly
- Monitor application logs in hosting platform

Your DermDetect app will be live with professional database tracking! 🎉