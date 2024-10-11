import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Bangalore Bikes Dashboard", page_icon="🏍️", layout="wide")

# Create two columns for the image and title
col1, col2 = st.columns([1, 3])  # Adjust the ratio as needed

# Display a smaller image in the first column
image_path = 'https://github.com/whosurajnegi/Bangalore-Bike-Dashboard/blob/main/bike.JPG'  # Replace with the path to your image
col1.image(image_path, width=100)  # Set a specific width for the image

# Display the title in the second column
col2.title("Bangalore Bikes Dashboard")  # Title of the app

# Load the bike data from the specified path
file_path = 'Bangalore_Bike_Data.xlsx'
bike_data = pd.read_excel(file_path, header=None)

# Set the first row as the header (bike models)
bike_data.columns = bike_data.iloc[0]  # Set the first row as header
bike_data = bike_data[1:]  # Remove the header row

# Replace None values with empty strings
bike_data.fillna('', inplace=True)

# Sidebar for bike model selection
st.sidebar.header("Filter")
bike_models = bike_data.columns.tolist()
selected_bike = st.sidebar.selectbox("Select a Bike Model", bike_models)

# Get the riders for the selected bike model
riders_for_selected_bike = bike_data[selected_bike].dropna().tolist()

# Display the riders' names
st.markdown(f"### Riders for {selected_bike}:")
for rider in riders_for_selected_bike:
    st.write(rider)

# Display overall data in a table
st.markdown('### Bike Data Overview')
st.dataframe(bike_data, use_container_width=True)
