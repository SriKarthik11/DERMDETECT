import os
from supabase import create_client, Client
from datetime import datetime
import json

class SupabaseDB:
    def __init__(self):
        # Supabase credentials - set these as environment variables
        supabase_url = os.environ.get('SUPABASE_URL', 'your-supabase-url')
        supabase_key = os.environ.get('SUPABASE_ANON_KEY', 'your-supabase-anon-key')
        
        if supabase_url == 'your-supabase-url' or supabase_key == 'your-supabase-anon-key':
            print("⚠️ Supabase credentials not set. Running without database.")
            self.supabase = None
        else:
            try:
                self.supabase: Client = create_client(supabase_url, supabase_key)
                print("✅ Supabase connected successfully")
            except Exception as e:
                print(f"⚠️ Supabase connection failed: {e}")
                self.supabase = None
    
    def save_analysis(self, image_name, predictions, user_ip=None):
        """Save analysis results to Supabase"""
        if not self.supabase:
            return None
            
        try:
            analysis_data = {
                'created_at': datetime.now().isoformat(),
                'image_name': image_name,
                'predictions': json.dumps(predictions),
                'user_ip': user_ip,
                'top_prediction_class': predictions[0]['class'] if predictions else None,
                'top_prediction_confidence': predictions[0]['confidence'] if predictions else None
            }
            
            result = self.supabase.table('analyses').insert(analysis_data).execute()
            return result.data[0]['id'] if result.data else None
            
        except Exception as e:
            print(f"Error saving to Supabase: {e}")
            return None
    
    def get_analysis_stats(self):
        """Get basic statistics from Supabase"""
        if not self.supabase:
            return {'total_analyses': 0, 'condition_distribution': {}}
            
        try:
            # Get total count
            total_result = self.supabase.table('analyses').select('id', count='exact').execute()
            total_count = total_result.count if hasattr(total_result, 'count') else 0
            
            # Get condition distribution
            conditions_result = self.supabase.table('analyses').select('top_prediction_class').execute()
            
            condition_counts = {}
            for record in conditions_result.data:
                condition = record.get('top_prediction_class', 'Unknown')
                if condition:
                    condition_counts[condition] = condition_counts.get(condition, 0) + 1
            
            return {
                'total_analyses': total_count,
                'condition_distribution': condition_counts
            }
            
        except Exception as e:
            print(f"Error getting stats from Supabase: {e}")
            return {'total_analyses': 0, 'condition_distribution': {}}
    
    def get_recent_analyses(self, limit=10):
        """Get recent analyses"""
        if not self.supabase:
            return []
            
        try:
            result = self.supabase.table('analyses')\
                .select('*')\
                .order('created_at', desc=True)\
                .limit(limit)\
                .execute()
            
            return result.data
            
        except Exception as e:
            print(f"Error getting recent analyses: {e}")
            return []