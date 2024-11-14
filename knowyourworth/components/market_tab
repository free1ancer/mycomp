import streamlit as st
import plotly.express as px
from data.data_generator import generate_sample_data

def render_market_tab():
    st.header("Market Trends and Insights")
    
    df = generate_sample_data()
    
    # Market overview metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Market Average",
            f"${df['Total_Compensation'].mean():,.0f}",
            f"{df['Total_Compensation'].pct_change().mean():+.1%}"
        )
    with col2:
        st.metric(
            "Highest Paying Role",
            df.groupby('Role')['Total_Compensation'].mean().idxmax()
        )
    with col3:
        st.metric(
            "Highest Paying Location",
            df.groupby('Location')['Total_Compensation'].mean().idxmax()
        )
    
    # Market insights
    st.subheader("Market Insights")
    
    tab1, tab2, tab3 = st.tabs([
        "Role Analysis", "Location Analysis", "Experience Impact"
    ])
    
    with tab1:
        fig1 = px.violin(df,
                        x="Role",
                        y="Total_Compensation",
                        color="Level",
                        box=True,
                        title="Compensation Distribution by Role")
        st.plotly_chart(fig1, use_container_width=True)
    
    with tab2:
        avg_by_location = df.groupby(
            ['Location', 'Role']
        )['Total_Compensation'].mean().reset_index()
        
        fig2 = px.bar(avg_by_location,
                     x="Location",
                     y="Total_Compensation",
                     color="Role",
                     title="Average Compensation by Location")
        st.plotly_chart(fig2, use_container_width=True)