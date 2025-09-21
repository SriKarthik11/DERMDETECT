# DermDetect - AI Skin Analysis

A web application for dermatology analysis using your trained TinyViT model.

## Setup Instructions

1. **Copy your model file**:
   ```bash
   copy "E:\SkinCancerDetection\final_tinyvit_safe.pth" "skin-cancer-web-app\final_tinyvit_safe.pth"
   ```

2. **Install dependencies**:
   ```bash
   cd skin-cancer-web-app
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and go to: `http://localhost:5000`

## Features

- **Drag & Drop Interface**: Easy image upload
- **Real-time Predictions**: Instant AI analysis
- **Top 3 Results**: Shows confidence scores for top predictions
- **Responsive Design**: Works on desktop and mobile
- **Professional UI**: Clean, medical-grade interface

## Model Classes

The model can detect 35 different skin conditions:
- Acne and Rosacea
- Malignant lesions
- Benign conditions
- Various skin diseases
- And more...

## Usage

1. Upload a skin image (JPG, PNG, JPEG)
2. Click "Analyze Image"
3. View the AI predictions with confidence scores
4. Get top 3 most likely conditions

## Disclaimer

This tool is for educational purposes only. Always consult a healthcare professional for medical advice.