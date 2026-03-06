import os
from supabase import create_client

def get_supabase_client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SECRET_KEY")

    if not url or not key:
        raise Exception("SUPABASE_URL or SUPABASE_SECRET_KEY not set")
    
    return create_client(url, key)