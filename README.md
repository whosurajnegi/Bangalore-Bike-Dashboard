# Bangalore Bikes Dashboard
https://bangalore-bikeriders-community.streamlit.app/
## Overview

The **Bangalore Bikes Dashboard** is a Streamlit application that provides insights into bike models and their riders in Bangalore. Users can select a bike model from a sidebar and view the corresponding riders, along with an overview of the bike data in a tabular format. The application also features a pie chart that visualizes the distribution of riders across different bike models.

## Features

- **Interactive Selection**: Choose a bike model from the sidebar to see the list of riders associated with that model.
- **Data Overview**: Access a comprehensive table that shows all bike data.

## Technologies Used

- Python
- Streamlit
- Pandas
- Altair (for data visualization)
- Excel (for data storage)

## Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/bangalore-bikes-dashboard.git
   cd bangalore-bikes-dashboard
2. python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the packages:
   pip install streamlit pandas altair openpyxl
4. Run application: streamlit run bike_dashboard.py  
