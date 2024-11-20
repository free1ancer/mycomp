import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

def create_profile_form():
    with st.form("profile_submission", clear_on_submit=True):
        st.subheader("Add Your Compensation Data")
        
        col1, col2 = st.columns(2)
        with col1:
            company = st.text_input("Company Name")
            role = st.selectbox("Role", [
                "Software Engineer", "Data Scientist", 
                "Product Manager", "UX Designer"
            ])
            level = st.selectbox("Level", [
                "Junior", "Mid", "Senior", "Lead", "Principal"
            ])
            location = st.selectbox("Location", [
                "SF Bay Area", "New York", "London", "Remote"
            ])
        
        with col2:
            base = st.number_input("Base Salary", min_value=0, step=1000)
            bonus = st.number_input("Annual Bonus", min_value=0, step=1000)
            equity = st.number_input("Annual Equity (USD)", min_value=0, step=1000)
            date = st.date_input("Date", datetime.now())
        
        submitted = st.form_submit_button("Submit")
        if submitted and company and base > 0:
            return {
                "company": company,
                "role": role,
                "level": level,
                "base": base,
                "bonus": bonus,
                "equity": equity,
                "location": location,
                "date": date,
                "id": datetime.now().strftime("%Y%m%d_%H%M%S")
            }
    return None

def render_overview(profiles):
    st.header("Your Career Overview")
    if profiles:
        df = pd.DataFrame(profiles)
        
        # Total compensation over time
        fig1 = px.line(df, x='date', 
                      y=['base', 'bonus', 'equity'],
                      title="Your Compensation History",
                      labels={"value": "Amount ($)", "variable": "Component"})
        st.plotly_chart(fig1, use_container_width=True)
        
        # Latest compensation breakdown
        latest = df.iloc[-1]
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Base Salary", f"${latest['base']:,.0f}")
        with col2:
            st.metric("Bonus", f"${latest['bonus']:,.0f}")
        with col3:
            st.metric("Equity", f"${latest['equity']:,.0f}")

def render_profile_data(profiles):
    st.header("Your Profile Data")
    if profiles:
        df = pd.DataFrame(profiles)
        df['total'] = df['base'] + df['bonus'] + df['equity']
        st.dataframe(df, hide_index=True)
    else:
        st.info("No entries yet. Click '+ Add Entry' to get started!")

def render_entry_details(profile):
    st.header(f"Entry Details - {profile['company']}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Company:**", profile['company'])
        st.write("**Role:**", profile['role'])
        st.write("**Level:**", profile['level'])
        st.write("**Location:**", profile['location'])
    
    with col2:
        st.write("**Base Salary:**", f"${profile['base']:,}")
        st.write("**Bonus:**", f"${profile['bonus']:,}")
        st.write("**Equity:**", f"${profile['equity']:,}")
        st.write("**Total:**", 
                f"${profile['base'] + profile['bonus'] + profile['equity']:,}")

def render_you_tab():
    if 'profiles' not in st.session_state:
        st.session_state.profiles = []
    
    profile_tabs = ["Overview", "Profile Data", "+ Add Entry"] + \
                  [f"Entry {p['id']}" for p in st.session_state.profiles]
    
    current_tab = st.tabs(profile_tabs)
    
    with current_tab[0]:
        render_overview(st.session_state.profiles)
    
    with current_tab[1]:
        render_profile_data(st.session_state.profiles)
    
    with current_tab[2]:
        new_profile = create_profile_form()
        if new_profile:
            st.session_state.profiles.append(new_profile)
            st.success("Profile added successfully!")
            st.rerun()
    
    for i, profile in enumerate(st.session_state.profiles):
        with current_tab[i + 3]:
            render_entry_details(profile)
            if st.button("Delete Entry", key=f"delete_{profile['id']}"):
                st.session_state.profiles.remove(profile)
                st.rerun()