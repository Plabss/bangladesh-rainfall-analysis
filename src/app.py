import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(page_title="Bangladesh Rainfall Analytics", layout="wide")

# --- LOAD DATA ---
@st.cache_data # This caches the data so it doesn't reload on every click
def load_data():
    df = pd.read_csv("data/rainfall.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Options")

# Station Selection
all_stations = sorted(df['Station'].unique())
selected_station = st.sidebar.selectbox("Select Station", ["All Stations"] + all_stations)

# Year Range Selection
min_year, max_year = int(df['Year'].min()), int(df['Year'].max())
selected_years = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))

# Filter the dataframe based on selection
filtered_df = df[(df['Year'] >= selected_years[0]) & (df['Year'] <= selected_years[1])]

if selected_station != "All Stations":
    filtered_df = filtered_df[filtered_df['Station'] == selected_station]

# --- MAIN DASHBOARD ---
st.title("🌧️ Bangladesh Rainfall Analysis Dashboard")
st.markdown(f"Visualizing historical rainfall data from **{selected_years[0]} to {selected_years[1]}**")

# --- TOP METRICS ---
col1, col2, col3 = st.columns(3)
with col1:
    avg_rain = filtered_df['Rainfall'].mean()
    st.metric("Avg Daily Rainfall", f"{avg_rain:.2f} mm")
with col2:
    max_rain = filtered_df['Rainfall'].max()
    st.metric("Highest Recorded Day", f"{max_rain:.1f} mm")
with col3:
    total_stations = filtered_df['Station'].nunique()
    st.metric("Stations Analyzed", total_stations)

st.divider()

# --- VISUALIZATIONS ---

# Row 1: Time Series Trend
st.subheader(f"Rainfall Trend: {selected_station}")
# Aggregating to monthly for a smoother line chart
monthly_trend = filtered_df.groupby([pd.Grouper(key='Date', freq='ME')])['Rainfall'].sum().reset_index()
fig_line = px.line(monthly_trend, x='Date', y='Rainfall', 
                  title="Total Monthly Rainfall Over Time",
                  labels={'Rainfall': 'Rainfall (mm)'},
                  template="plotly_white")
st.plotly_chart(fig_line, use_container_width=True)

# Row 2: Seasonality and Distribution
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Monthly Seasonality")
    monthly_avg = filtered_df.groupby('Month')['Rainfall'].mean().reset_index()
    # Map month numbers to names
    month_map = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 
                 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
    monthly_avg['Month Name'] = monthly_avg['Month'].map(month_map)
    
    fig_bar = px.bar(monthly_avg, x='Month Name', y='Rainfall', 
                     color='Rainfall', color_continuous_scale='Blues',
                     title="Average Rainfall by Month")
    st.plotly_chart(fig_bar, use_container_width=True)

with col_right:
    if selected_station == "All Stations":
        st.subheader("Top 10 Wettest Stations")
        # Global comparison
        station_comp = filtered_df.groupby('Station')['Rainfall'].mean().sort_values(ascending=False).head(10).reset_index()
        fig = px.bar(station_comp, x='Rainfall', y='Station', orientation='h', color='Rainfall', color_continuous_scale='Blues')
    else:
        st.subheader(f"Rainfall Variability: {selected_station}")
        # Show a Box Plot for the specific station to see outliers and seasonality
        fig = px.box(filtered_df, x='Month', y='Rainfall', 
                     points="outliers", # Shows extreme weather events
                     color='Month',
                     labels={'Month': 'Month (1-12)', 'Rainfall': 'Daily Rainfall (mm)'},
                     title="Monthly Distribution & Outliers")
        # Improve X-axis labels to show Jan, Feb, etc.
        fig.update_layout(showlegend=False)

    st.plotly_chart(fig, use_container_width=True)

# Row 3: Data Table
with st.expander("View Raw Filtered Data"):
    st.dataframe(filtered_df.head(100), use_container_width=True)