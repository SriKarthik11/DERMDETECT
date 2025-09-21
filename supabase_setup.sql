-- Supabase Database Setup for DermDetect
-- Run this SQL in your Supabase SQL Editor

-- Create analyses table
CREATE TABLE IF NOT EXISTS analyses (
    id BIGSERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    image_name TEXT,
    predictions JSONB,
    user_ip INET,
    top_prediction_class TEXT,
    top_prediction_confidence DECIMAL(5,2)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_analyses_created_at ON analyses(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_analyses_top_prediction ON analyses(top_prediction_class);
CREATE INDEX IF NOT EXISTS idx_analyses_user_ip ON analyses(user_ip);

-- Enable Row Level Security (RLS)
ALTER TABLE analyses ENABLE ROW LEVEL SECURITY;

-- Create policy to allow inserts from anyone (for the app)
CREATE POLICY "Allow public inserts" ON analyses
    FOR INSERT WITH CHECK (true);

-- Create policy to allow reads from anyone (for stats)
CREATE POLICY "Allow public reads" ON analyses
    FOR SELECT USING (true);

-- Create a view for public statistics (optional)
CREATE OR REPLACE VIEW public_stats AS
SELECT 
    COUNT(*) as total_analyses,
    COUNT(DISTINCT user_ip) as unique_users,
    top_prediction_class,
    COUNT(*) as condition_count,
    AVG(top_prediction_confidence) as avg_confidence
FROM analyses 
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY top_prediction_class
ORDER BY condition_count DESC;