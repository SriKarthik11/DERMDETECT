import os
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import timm
import numpy as np
from flask import Flask, request, jsonify, render_template
import base64
from io import BytesIO
from supabase_config import SupabaseDB
import uuid

app = Flask(__name__)

# Configuration
MODEL_PATH = "final_tinyvit_safe.pth"
IMG_SIZE = 224
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Class names mapping (17 classes from your actual training data)
CLASS_NAMES = [
    "Acne And Rosacea Photos",
    "Actinic Keratosis Basal Cell Carcinoma And Other Malignant Lesions",
    "Atopic Dermatitis Photos", 
    "Benign",
    "Cellulitis Impetigo And Other Bacterial Infections",
    "Eczema Photos",
    "Fu Ringworm",
    "Hair Loss Photos Alopecia And Other Hair Diseases",
    "Heathy",
    "Lupus And Other Connective Tissue Diseases",
    "Malignant",
    "Melanoma Skin Cancer Nevi And Moles",
    "Psoriasis Pictures Lichen Planus And Related Diseases",
    "Rashes",
    "Seborrheic Keratoses And Other Benign Tumors",
    "Urticaria Hives",
    "Vascular Tumors"
]

# Load model
def load_model():
    model = timm.create_model("tiny_vit_21m_224", pretrained=False, num_classes=len(CLASS_NAMES))
    state_dict = torch.load(MODEL_PATH, map_location=DEVICE, weights_only=True)
    model.load_state_dict(state_dict)
    model.to(DEVICE)
    model.eval()
    return model

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])

# Initialize model and Supabase
model = load_model()
print("✅ Model loaded successfully")

# Initialize Supabase (optional - will work without Supabase too)
try:
    supabase_db = SupabaseDB()
    print("✅ Supabase initialized")
except Exception as e:
    print(f"⚠️ Supabase not available: {e}")
    supabase_db = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get image from request
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No image selected'}), 400
        
        # Process image
        image = Image.open(file.stream).convert('RGB')
        input_tensor = transform(image).unsqueeze(0).to(DEVICE)
        
        # Make prediction
        with torch.no_grad():
            outputs = model(input_tensor)
            probabilities = nn.Softmax(dim=1)(outputs)
            confidence, predicted = torch.max(probabilities, 1)
            
        # Get top 3 predictions
        probs = probabilities.cpu().numpy()[0]
        top_indices = np.argsort(probs)[::-1][:3]
        
        results = []
        for i, idx in enumerate(top_indices):
            results.append({
                'class': CLASS_NAMES[idx],
                'confidence': float(probs[idx]) * 100
            })
        
        # Save to Supabase if available
        if supabase_db and supabase_db.supabase:
            try:
                image_id = str(uuid.uuid4())
                user_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
                supabase_db.save_analysis(image_id, results, user_ip)
            except Exception as e:
                print(f"Supabase save error: {e}")
        
        return jsonify({
            'success': True,
            'predictions': results
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/stats')
def get_stats():
    """Get analysis statistics"""
    if supabase_db and supabase_db.supabase:
        stats = supabase_db.get_analysis_stats()
        return jsonify(stats)
    return jsonify({'error': 'Supabase not available'})

@app.route('/recent')
def get_recent():
    """Get recent analyses"""
    if supabase_db and supabase_db.supabase:
        recent = supabase_db.get_recent_analyses()
        return jsonify(recent)
    return jsonify({'error': 'Supabase not available'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)