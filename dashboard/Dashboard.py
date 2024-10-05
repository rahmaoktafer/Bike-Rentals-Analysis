import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.dates as mdates
from IPython.display import display

# Load the dataset
df = pd.read_csv('dashboard/final_data.csv')
#final_data.csv is the cleaned version of day.csv, generated after performing data cleaning

# Ensure 'dteday' is in datetime format
df['dteday'] = pd.to_datetime(df['dteday'])

# Set 'dteday' as the index for time series plotting
df.set_index('dteday', inplace=True)

# Streamlit app header
st.title('Bike Rental Analysis')

# Section 1: Casual vs Registered User Rentals Over Time
st.header('Casual vs Registered User Rentals Over Time')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot casual users over time
ax.plot(df.index, df['casual'], label='Casual Users', color='blue')

# Plot registered users over time
ax.plot(df.index, df['registered'], label='Registered Users', color='green')

# Add titles and labels
ax.set_title('Casual vs Registered User Rentals Over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Rentals')

# Add a legend
ax.legend()

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust x-axis ticks to show fewer dates while keeping date format
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Display the plot in Streamlit
st.pyplot(fig)

# Section 2: Number of Casual and Registered User Rentals by Weather Condition
st.header('Number of Casual and Registered User Rentals by Weather Condition')

# Group by 'weathersit' and sum the rentals
weather_data = df.groupby('weathersit').agg({
    'casual': 'sum',
    'registered': 'sum'
}).reset_index()

# Set the figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot casual users
ax.bar(weather_data['weathersit'] - 0.2, weather_data['casual'], width=0.4, label='Casual Users', color='blue')

# Plot registered users
ax.bar(weather_data['weathersit'] + 0.2, weather_data['registered'], width=0.4, label='Registered Users', color='green')

# Add titles and labels
ax.set_title('Number of Casual and Registered User Rentals by Weather Condition')
ax.set_xlabel('Weather Condition (1-4)')
ax.set_ylabel('Number of Rentals')

# Add a legend
ax.legend()

# Display the plot
ax.set_xticks(weather_data['weathersit'])
st.pyplot(fig)

# Section 3: Number of Rentals by Weather Condition (Boxplot)
st.header('Number of Rentals by Weather Condition')

# Create a box plot
fig, ax = plt.subplots(figsize=(8,6))
sns.boxplot(x='weathersit', y='cnt', data=df, ax=ax)

# Add labels and title
ax.set_xlabel('Weather Condition')
ax.set_ylabel('Number of Rentals')
ax.set_title('Number of Rentals by Weather Condition')

# Display the plot in Streamlit
st.pyplot(fig)

# Section 4: Correlation between Temperature and Number of Rentals
st.header('Correlation between Temperature and Number of Rentals')

# Set the figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Create scatter plot with regression line
sns.regplot(x='temp_celsius', y='cnt', data=df, scatter_kws={'color':'blue'}, line_kws={'color':'red'}, ax=ax)

# Add labels and title
ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('Number of Rentals')
ax.set_title('Correlation between Temperature and Number of Rentals')

# Show the plot in Streamlit
st.pyplot(fig)

# Section 5: Number of Rentals by Holiday (Boxplot)
st.header('Number of Rentals by Holiday')

# Create a box plot
fig, ax = plt.subplots(figsize=(8,6))
sns.boxplot(x='holiday', y='cnt', data=df, ax=ax)

# Add labels and title
ax.set_xlabel('Holiday')
ax.set_ylabel('Number of Rentals')

# Display the plot in Streamlit
st.pyplot(fig)

# Section 6: Number of Rentals by Working Days (Boxplot)
st.header('Number of Rentals by Working Days')

# Create a box plot
fig, ax = plt.subplots(figsize=(8,6))
sns.boxplot(x='workingday', y='cnt', data=df, ax=ax)

# Add labels and title
ax.set_xlabel('Working Days')
ax.set_ylabel('Number of Rentals')

# Display the plot in Streamlit
st.pyplot(fig)
