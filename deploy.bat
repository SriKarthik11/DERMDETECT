@echo off
echo 🚀 DermDetect Deployment Helper
echo.
echo ⚠️  IMPORTANT: Netlify won't work for DermDetect!
echo    Netlify only hosts static sites, but DermDetect needs Python backend
echo.
echo ✅ Use Render.com instead (perfect for ML apps)
echo.

echo Checking if git is initialized...
if not exist ".git" (
    echo Initializing git repository...
    git init
    git add .
    git commit -m "Deploy DermDetect to Render"
    echo.
    echo ✅ Git repository created
    echo.
    echo 📋 Next steps:
    echo 1. Create a repository on GitHub
    echo 2. Run: git remote add origin YOUR_GITHUB_REPO_URL  
    echo 3. Run: git push -u origin main
    echo 4. Deploy on Render.com (see render-deploy.md)
    echo.
) else (
    echo Git already initialized. Updating...
    git add .
    git commit -m "Update DermDetect for Render deployment"
    git push
    echo ✅ Code updated and pushed
)

echo.
echo 🗄️ Your Supabase is Ready:
echo ✅ URL: https://kmlpgfpkjwbijbynfrox.supabase.co
echo ✅ Key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
echo.

echo 🌐 Best Free Hosting for ML Apps:
echo 1. ⭐ Render.com - Perfect for DermDetect (750 hours/month)
echo 2. Railway.app - Easy deployment ($5 credit/month)  
echo 3. Fly.io - Global edge deployment (3 free VMs)
echo.
echo ❌ Netlify - Only for static sites (won't work with your AI model)
echo.

echo 🚀 Quick Render Deployment:
echo 1. Push code to GitHub
echo 2. Go to render.com and connect GitHub
echo 3. Add environment variables (Supabase URL and key)
echo 4. Deploy! Your app will be live in 5 minutes
echo.

echo 📖 Read render-deploy.md for step-by-step instructions
echo.

pause