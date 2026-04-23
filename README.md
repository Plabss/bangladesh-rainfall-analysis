# 🌧️ Bangladesh Historical Rainfall Analytics (1948–2014)

## 📌 Project Overview
This project provides an interactive spatiotemporal analysis of historical rainfall patterns in Bangladesh. Leveraging 66 years of daily data from 35 meteorological stations, the dashboard allows researchers and engineers to visualize monsoon trends, annual variability, and extreme precipitation events.

As a Water Resources Engineer, I developed this tool to bridge the gap between raw hydrological data and actionable visual insights, facilitating better understanding of regional climate shifts.

## 🚀 Live Demo
Access the Interactive Dashboard here: [Streamlit App](https://)

## 🛠️ Tech Stack
- **Language**: Python

- **Dashboard**: Streamlit

- **Data Manipulation**: Pandas (Reshaping from wide to long format), NumPy

- **Visualization**: Plotly (Interactive), Matplotlib, Seaborn

- **Deployment**: Streamlit Community Cloud

## 📊 Key Features & Engineering Insights

* **Data Reshaping (Tidy Data Architecture)**
    * Engineered a pipeline to transform raw meteorological data from a wide format (31 daily columns) into a time-series optimized **long format**. 
    * This transformation reduces data redundancy and enables efficient grouping by `Station`, `Month`, and `Year`.

* **Statistical Variability Analysis**
    * Implemented **Box Plots** for station-specific analysis. This allows for the immediate visualization of:
        * **Seasonal Interquartile Ranges (IQR):** Identifying the "typical" rainfall levels for each month.
        * **Extreme Value Detection:** Highlighting potential flood events (outliers) that deviate significantly from the monthly median.

* **Context-Aware UI (Conditional Rendering)**
    * The dashboard intelligently adapts its layout based on user input:
        * **Regional View:** Displays a "Top 10 Comparison" bar chart to identify the wettest zones in Bangladesh.
        * **Station View:** Automatically switches to a distribution-focused box plot when a specific station is selected, ensuring the visualization remains statistically meaningful.

* **Performance Optimization**
    * Integrated Streamlit's `@st.cache_data` decorator to ensure that the 600,000+ row dataset is loaded and processed only once.
    * Provides a seamless, low-latency user experience even when manipulating large time-series datasets.

## 📁 Project Structure
```
├── data/               # Raw and processed datasets
├── src/                # Streamlit source code (app.py)
├── notebooks/          # Exploratory Data Analysis (EDA)
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

## 📖 Data Citation & Source
The dataset used in this project is sourced from Kaggle, covering 35 rainfall stations in Bangladesh.

Basak, S. K. (2025). [Bangladesh Historical Rainfall Dataset](https://www.kaggle.com/datasets/shuvokumarbasak2030/bangladesh-historical-rainfall-dataset-1948-2014) (1948-2014). Kaggle. https://doi.org/10.34740/KAGGLE/DSV/10773426

### Developed with ❤️ by Plabon Chowdhury WRE Graduate | Data Scientist | Full Stack Developer