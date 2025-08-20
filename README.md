# Fitbit-Location-History-Map

This project allows you to visualize your Fitbit location history on a map. It consists of two Python scripts:

## `csv_merger.py`

**Purpose:**  
Merges multiple CSV files containing location data into a single CSV file. It can also reduce file size by keeping only every Nth row (recommended: 240) to prevent excessively large files.

**How it works:**  
1. Prompts the user for the folder containing CSV files.  
2. Prompts the user for a target directory and file name for the merged CSV.  
3. Optionally reduces the number of rows by a specified factor.  
4. Outputs a merged CSV file containing latitude and longitude data.

## `location_history.py`

**Purpose:**  
Visualizes location data from a CSV file on an interactive map using Plotly.

**How it works:**  
1. Asks the user if they have a single CSV file:  
   - **Yes:** Prompts for the CSV file path.  
   - **No:** Runs `csv_merger.py` to merge multiple CSV files interactively.  
2. Reads the CSV and extracts `latitude` and `longitude` columns.  
3. Plots the location data as a scatter map.  
4. Displays the map in a browser window.

**Requirements**
- Plotly (pip install plotly)
