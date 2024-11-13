import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Set page config
st.set_page_config(
    page_title="Two-Tab Demo",
    layout="wide"
)

# Main title
st.title("Streamlit Multi-Tab Demo")

# Create tabs
tab1, tab2 = st.tabs(["Data Analysis", "Data Visualization"])

# Generate sample data
def generate_sample_data():
    np.random.seed(42)
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    data = {
        'Date': dates,
        'Sales': np.random.normal(100, 15, len(dates)),
        'Traffic': np.random.normal(500, 50, len(dates))
    }
    return pd.DataFrame(data)

df = generate_sample_data()

# Tab 1: Data Analysis
with tab1:
    st.header("Data Analysis")
    
    # Add some filters
    date_range = st.date_input(
        "Select Date Range",
        value=(df['Date'].min(), df['Date'].max()),
        min_value=df['Date'].min(),
        max_value=df['Date'].max()
    )
    
    # Filter data based on date range
    mask = (df['Date'] >= pd.Timestamp(date_range[0])) & (df['Date'] <= pd.Timestamp(date_range[1]))
    filtered_df = df[mask]
    
    # Display statistics
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Summary Statistics")
        st.dataframe(filtered_df.describe())
    
    with col2:
        st.subheader("Raw Data")
        st.dataframe(filtered_df)

# Tab 2: Data Visualization
with tab2:
    st.header("Data Visualization")
    
    # Metric selector
    metric = st.selectbox("Select Metric to Visualize", ["Sales", "Traffic"])
    
    # Create line plot
    fig = px.line(
        filtered_df,
        x='Date',
        y=metric,
        title=f'{metric} Over Time'
    )
    
    # Display plot
    st.plotly_chart(fig, use_container_width=True)
    
    # Add some summary metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label=f"Average {metric}",
            value=f"{filtered_df[metric].mean():.2f}"
        )
    
    with col2:
        st.metric(
            label=f"Maximum {metric}",
            value=f"{filtered_df[metric].max():.2f}"
        )
    
    with col3:
        st.metric(
            label=f"Minimum {metric}",
            value=f"{filtered_df[metric].min():.2f}"
        )