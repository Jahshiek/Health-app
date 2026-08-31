import os

from dotenv import load_dotenv
from supabase import create_client

# Load environment variables from the .env file.
load_dotenv()


# Read our Supabase connection values.
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")


# Create one Supabase client that can be imported
# by other parts of the backend.
supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)