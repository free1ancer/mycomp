import streamlit as st
import plotly.express as px
from data.data_generator import generate_sample_data

def render_companies_tab():
    st.header("Company Compensation Analysis")
    
    df = generate_sample_data()
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_company = st.selectbox(
            "Company Type", 
            ["All"] + sorted(df['Company_Type'].unique().tolist())
        )
    with col2:
        selected_role = st.selectbox(
            "Role",
            ["All"] + sorted(df['Role'].unique().tolist())
        )
    with col3:
        selected_level = st.selectbox(
            "Level",
            ["All"] + sorted(df['Level'].unique().tolist())
        )
    
    # Filter data
    filtered_df = df.copy()
    if selected_company != "All":
        filtered_df = filtered_df[filtered_df['Company_Type'] == selected_company]
    if selected_role != "All":
        filtered_df = filtered_df[filtered_df['Role'] == selected_role]
    if selected_level != "All":
        filtered_df = filtered_df[filtered_df['Level'] == selected_level]
    
    # Visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = px.box(filtered_df, 
                     x="Company_Type", 
                     y="Total_Compensation",
                     color="Level",
                     title="Compensation Distribution by Company Type")
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        avg_by_company = filtered_df.groupby(
            ['Company_Type', 'Level']
        )['Total_Compensation'].mean().reset_index()
        
        fig2 = px.bar(avg_by_company,
                     x="Company_Type",
                     y="Total_Compensation",
                     color="Level",
                     title="Average Compensation by Company Type and Level")
        st.plotly_chart(fig2, use_container_width=True)
    
    # Detailed stats
    st.subheader("Compensation Statistics")
    stats_df = filtered_df.groupby('Company_Type').agg({
        'Total_Compensation': ['mean', 'median', 'std', 'count']
    }).round(2)
    stats_df.columns = ['Mean', 'Median', 'Std Dev', 'Count']
    st.dataframe(stats_df)