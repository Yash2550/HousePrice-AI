# 🚀 Deployment Guide - Render

This guide will help you deploy your HousePrice-AI application to Render for free!

## Prerequisites

- GitHub account (already done ✅)
- Render account (free) - Sign up at https://render.com

## Step-by-Step Deployment Instructions

### 1. Create Render Account

1. Go to https://render.com
2. Click **"Get Started for Free"**
3. Sign up using your **GitHub account** (recommended)

### 2. Connect GitHub Repository

1. After logging in, click **"New +"** button in the top right
2. Select **"Web Service"**
3. Click **"Connect account"** to connect your GitHub
4. Grant Render access to your repositories
5. Find and select **"HousePrice-AI"** repository

### 3. Configure the Web Service

Render will auto-detect your settings from `render.yaml`, but verify these settings:

- **Name**: `houseprice-ai` (or any name you prefer)
- **Environment**: `Python`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Plan**: `Free`

### 4. Deploy!

1. Click **"Create Web Service"**
2. Render will start building and deploying your app
3. Wait 3-5 minutes for the first deployment
4. You'll see a live URL like: `https://houseprice-ai.onrender.com`

### 5. Access Your Live Application

Once deployed, you'll get a URL like:
```
https://houseprice-ai-xxxx.onrender.com
```

Share this URL with anyone - your app is now live! 🎉

## Important Notes

⚠️ **Free Tier Limitations**:
- App may sleep after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds to wake up
- 750 hours/month of free usage

💡 **Tips**:
- The ML model (`house_price_model.pkl`) will be loaded on startup
- All frontend pages will be accessible at the root URL
- API endpoint `/predict` is available for price predictions

## Troubleshooting

### Build Failed?
- Check that all files are pushed to GitHub
- Verify `requirements.txt` has all dependencies
- Check Render logs for specific errors

### App not loading?
- Wait for initial deployment to complete (check Render dashboard)
- Clear browser cache and try again
- Check if the service is "Live" in Render dashboard

### Prediction not working?
- Ensure `models/house_price_model.pkl` exists in the repository
- If missing, run `python src/train.py` locally first
- Commit and push the generated model file

## Updating Your Deployment

To update your live app:

1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your update message"
   git push origin main
   ```
3. Render will automatically detect changes and redeploy!

## Environment Variables (Optional)

If needed, you can add environment variables in Render:
- Go to your service dashboard
- Click "Environment"
- Add variables (e.g., API keys, database URLs)

---

## Need Help?

- Render Documentation: https://render.com/docs
- Render Support: https://render.com/support

**Your app is now accessible worldwide! 🌍**
