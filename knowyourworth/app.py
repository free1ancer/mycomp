import streamlit as st
from config.styles import CUSTOM_CSS
from components.banner import render_banner
from components.you_tab import render_you_tab
from components.companies_tab import render_companies_tab
from components.market_tab import render_market_tab

# Page configuration
st.set_page_config(
    page_title="KnowYourWorth",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom styling
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Render banner
render_banner()

# Main tabs
tab1, tab2, tab3 = st.tabs(["You", "Companies", "The Market"])

# Render content for each tab
with tab1:
    render_you_tab()

with tab2:
    render_companies_tab()

with tab3:
    render_market_tab()

# Add requirements.txt content
"""
streamlit==1.31.0
pandas==2.1.3
plotly==5.18.0
numpy==1.24.3
"""