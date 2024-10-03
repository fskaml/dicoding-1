import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Dashboard title
st.title("Bike Sharing Data Analysis")

# Load data
data = pd.read_csv('dashboard/main_data.csv')

# Display data
if st.checkbox("Show Data"):
    st.write(data)

# Calculate total rentals
total_rentals = data['cnt_x'].sum()  # Total rentals
st.subheader(f'Total Bike Rentals: {total_rentals}')

# Select analysis type
analysis_type = st.selectbox("Select Analysis Type", ["Weekdays vs Weekends", "Total Rentals per Day", "Total Rentals by Weather", "Temperature vs Total Rentals"])

# Analysis based on selection
if analysis_type == "Weekdays vs Weekends":
    st.subheader("Bike Rentals on Weekdays vs Weekends/Holidays")
    # Create a new column to classify weekdays and weekends
    data['day_type'] = data['weekday_x'].apply(lambda x: 'Weekend' if x in [5, 6] else 'Weekday')  # Assuming 0-6 where 0=Monday, 6=Sunday

    # Create boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x='day_type', y='cnt_x')
    plt.title('Bike Rentals on Weekdays vs Weekends/Holidays')
    plt.xlabel('Day Type')
    plt.ylabel('Number of Rentals')
    st.pyplot(plt)

elif analysis_type == "Total Rentals per Day":
    st.subheader("Total Bike Rentals per Day")
    total_per_day = data.groupby('dteday')['cnt_x'].sum().reset_index()  # Group by date
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=total_per_day, x='dteday', y='cnt_x')
    plt.xticks(rotation=45)
    plt.title('Total Bike Rentals per Day')
    plt.xlabel('Date')
    plt.ylabel('Total Rentals')
    st.pyplot(plt)

elif analysis_type == "Total Rentals by Weather":
    st.subheader("Total Rentals by Weather")
    weather_rentals = data.groupby('weathersit_x')['cnt_x'].sum().reset_index()  # Group by weather
    plt.figure(figsize=(8, 5))
    sns.barplot(data=weather_rentals, x='weathersit_x', y='cnt_x')
    plt.title('Total Bike Rentals by Weather')
    plt.xlabel('Weather Condition')
    plt.ylabel('Total Rentals')
    st.pyplot(plt)

elif analysis_type == "Temperature vs Total Rentals":
    st.subheader("Temperature vs Total Rentals")
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=data, x='temp_x', y='cnt_x')  # Scatter plot
    plt.title('Temperature vs Total Rentals')
    plt.xlabel('Temperature')
    plt.ylabel('Total Rentals')
    st.pyplot(plt)

# Show descriptive statistics
if st.checkbox("Show Descriptive Statistics"):
    st.write(data.describe())

# Additional information
st.sidebar.title("Additional Information")
st.sidebar.info("This dashboard is used to analyze bike rental data based on various factors such as weather, temperature, and day of the week.")
