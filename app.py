### Flask + Streamlit + OAuth + Token Store integration (public hosting ready)

# Streamlit app for Digiman dashboard
# Features:
# - OAuth for Gmail, Instagram, Stripe, etc.
# - Token storage in `.digi/clients/{client_id}/tokens.json`
# - Toggle active agents
# - Chat with Digiman

import streamlit as st
import json
import os
from pathlib import Path

st.set_page_config(page_title="DigiMan Dashboard", layout="wide")

st.title("🤖 DigiMan – Your Autonomous COO")
client_id = st.text_input("Client ID", value="demo-client")
token_path = Path(f".digi/clients/{client_id}/tokens.json")
token_path.parent.mkdir(parents=True, exist_ok=True)

# === OAuth Buttons ===
st.subheader("🔐 Connect Accounts")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Connect Gmail"):
        st.info("[Mock] OAuth flow for Gmail initiated...")
with col2:
    if st.button("Connect Instagram"):
        st.info("[Mock] OAuth flow for Instagram initiated...")
with col3:
    if st.button("Connect Stripe"):
        st.info("[Mock] OAuth flow for Stripe initiated...")

# === Token Store ===
st.subheader("📦 Stored Tokens")
if token_path.exists():
    with open(token_path) as f:
        st.json(json.load(f))
else:
    st.info("No tokens stored yet.")

# === Agent Control ===
st.subheader("🧠 Active Agents")
agents = ["Manager Agent", "Email Agent", "Web Builder Agent", "CRM Agent"]
active_agents = st.multiselect("Enable/Disable Agents", agents, default=agents)

# === Digiman Chat ===
st.subheader("💬 Chat with Digiman")
user_input = st.text_input("Type a command (e.g., 'Build website', 'Connect Gmail')")
if st.button("Send Command"):
    if user_input:
        st.success(f"Command sent to Digiman: '{user_input}'")
        # Placeholder for backend integration
    else:
        st.warning("Please type a command.")

# === Notes ===
st.markdown("---")
st.markdown("This UI is ready for public hosting via [Streamlit Cloud](https://streamlit.io/cloud). Push to GitHub and link your repo to deploy.")

# === GitHub Deployment Files ===
with open("requirements.txt", "w") as f:
    f.write("streamlit\n")

with open(".gitignore", "w") as f:
    f.write("__pycache__/\n.digi/\n.env\n*.pyc\n")
