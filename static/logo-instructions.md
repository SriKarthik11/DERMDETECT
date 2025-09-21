# 🎨 Logo Setup Instructions

## Where to Add Your Logo

### 📁 File Location
Place your logo file in this `/static/` directory with one of these names:
- `logo.png` (recommended - supports transparency)
- `logo.jpg` 
- `logo.svg`

### 📏 Recommended Specifications
- **Size**: 300x80 pixels (or similar 4:1 aspect ratio)
- **Format**: PNG with transparent background preferred
- **File size**: Under 500KB for fast loading
- **Style**: Should work well on beige/cream background

### 🎯 How It Works
The website automatically detects your logo file:
1. If `logo.png` exists → Shows your logo
2. If logo not found → Shows "DermDetect" text as fallback

### 🖼️ Sample Medical Image
Also add a professional medical image as:
- `sample-medical.jpg` (doctor examining skin, dermatology consultation, etc.)
- **Size**: 400x400 pixels (square format)
- **Style**: Professional, medical context

### 📂 Current Structure
```
static/
├── logo.png              ← Add your logo here
├── sample-medical.jpg    ← Add medical sample image here
└── logo-instructions.md  ← This file
```

### 🎨 Logo Design Tips
- Use your brand colors that complement the beige theme
- Ensure text is readable on light backgrounds
- Consider a medical/healthcare aesthetic
- Test on both desktop and mobile sizes

### ✅ Testing Your Logo
1. Add your logo file to `/static/`
2. Run `python test_local.py` to verify
3. Start the app with `python app.py`
4. Check http://localhost:5000 to see your logo

Your logo will appear at the top of the DermDetect interface! 🎉