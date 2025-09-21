"""
Quick local test script for DermDetect with Supabase
Run this to test your app locally before deployment
"""
import os
import sys

def test_supabase_connection():
    """Test Supabase connection"""
    print("🧪 Testing Supabase Connection...")
    
    # Check if environment variables are set
    supabase_url = os.environ.get('SUPABASE_URL')
    supabase_key = os.environ.get('SUPABASE_ANON_KEY')
    
    if not supabase_url or not supabase_key:
        print("❌ Supabase credentials not found!")
        print("📋 To test with Supabase:")
        print("1. Create .env file with your credentials")
        print("2. Or set environment variables:")
        print("   set SUPABASE_URL=https://your-project-id.supabase.co")
        print("   set SUPABASE_ANON_KEY=your-anon-key")
        print("\n✅ App will still work without Supabase (no database logging)")
        return False
    
    try:
        from supabase_config import SupabaseDB
        db = SupabaseDB()
        if db.supabase:
            print("✅ Supabase connection successful!")
            
            # Test database write
            test_data = [{'class': 'Test Condition', 'confidence': 95.5}]
            result = db.save_analysis('test-image', test_data, '127.0.0.1')
            if result:
                print("✅ Database write test successful!")
            
            # Test database read
            stats = db.get_analysis_stats()
            print(f"📊 Current database stats: {stats}")
            
            return True
        else:
            print("❌ Supabase connection failed")
            return False
            
    except Exception as e:
        print(f"❌ Supabase test failed: {e}")
        return False

def check_model_file():
    """Check if model file exists"""
    print("\n🤖 Checking Model File...")
    if os.path.exists('final_tinyvit_safe.pth'):
        size_mb = os.path.getsize('final_tinyvit_safe.pth') / (1024 * 1024)
        print(f"✅ Model file found ({size_mb:.1f} MB)")
        return True
    else:
        print("❌ Model file 'final_tinyvit_safe.pth' not found!")
        print("📋 Please copy your model file to this directory")
        return False

def check_static_files():
    """Check static files (logo, sample image)"""
    print("\n🖼️ Checking Static Files...")
    
    if not os.path.exists('static'):
        os.makedirs('static')
        print("📁 Created static directory")
    
    logo_exists = os.path.exists('static/logo.png') or os.path.exists('static/logo.jpg')
    sample_exists = os.path.exists('static/sample-medical.jpg') or os.path.exists('static/sample-medical.png')
    
    if logo_exists:
        print("✅ Logo file found in static/")
    else:
        print("⚠️ Logo not found - add your logo as 'static/logo.png'")
    
    if sample_exists:
        print("✅ Sample medical image found in static/")
    else:
        print("⚠️ Sample image not found - add as 'static/sample-medical.jpg'")
    
    return logo_exists, sample_exists

def main():
    print("🚀 DermDetect Local Test")
    print("=" * 50)
    
    # Check model
    model_ok = check_model_file()
    
    # Check static files
    logo_ok, sample_ok = check_static_files()
    
    # Test Supabase
    supabase_ok = test_supabase_connection()
    
    print("\n" + "=" * 50)
    print("📋 Test Summary:")
    print(f"🤖 Model file: {'✅' if model_ok else '❌'}")
    print(f"🖼️ Logo file: {'✅' if logo_ok else '⚠️'}")
    print(f"📸 Sample image: {'✅' if sample_ok else '⚠️'}")
    print(f"🗄️ Supabase: {'✅' if supabase_ok else '⚠️'}")
    
    if model_ok:
        print("\n🎉 Ready to start local server!")
        print("Run: python app.py")
        print("Then open: http://localhost:5000")
    else:
        print("\n❌ Please fix the issues above before starting")

if __name__ == "__main__":
    main()