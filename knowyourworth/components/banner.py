import streamlit as st

def render_banner():
    st.markdown("""
        <div class="banner">
            <h1>KnowYourWorth</h1>
            <p>Empowering careers through crowd-sourced compensation data. Join our community to understand your market value and make informed career decisions.</p>
        </div>
    """, unsafe_allow_html=True)