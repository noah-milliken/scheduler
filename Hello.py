import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Quarterpath Rec Center",
    page_icon="👋",
)

from st_supabase_connection import SupabaseConnection

# Initialize connection.
conn = st.connection("supabase", type=SupabaseConnection)

# Perform query.
rows = conn.query("*", table="mytable", ttl="10m").execute()

# Print results.
for row in rows.data:
    st.write(f"{row['name']} has a :{row['pet']}:")
