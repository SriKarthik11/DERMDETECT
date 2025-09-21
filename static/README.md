# Static Assets for DermDetect

## How to Add Your Images

### 1. Logo Image
- **File name**: `logo.png` (or `logo.jpg`, `logo.svg`)
- **Location**: Place in this `/static/` folder
- **Recommended size**: 300x80px or similar aspect ratio
- **Format**: PNG with transparent background preferred

### 2. Sample Medical Image
- **File name**: `sample-medical.jpg` (or `.png`)
- **Location**: Place in this `/static/` folder  
- **Recommended**: Professional photo of doctor examining skin or dermatology consultation
- **Size**: 400x400px or square aspect ratio
- **Format**: JPG or PNG

## Current Structure
```
static/
├── README.md (this file)
├── logo.png (add your logo here)
└── sample-medical.jpg (add your medical sample image here)
```

## Fallback Behavior
- If logo.png is not found, the text "DermDetect" will be displayed
- If sample-medical.jpg is not found, a simple SVG illustration will be shown

## Tips
- Use high-quality images for better professional appearance
- Ensure medical images are appropriate and professional
- Logo should work well on the beige background color scheme