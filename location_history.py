import plotly.express as px
import csv
import subprocess
import os
import sys

user_rsp = input("Do you have a single CSV file? (y/n)\n")

if user_rsp == 'y':
    path = input("Enter path to CSV file:\n")
    path = path.strip("'")

else:
   # Run the merger script and let the user interact with it
    subprocess.run([sys.executable, "csv_merger.py"])  # user provides inputs in terminal

    # After merger finishes, ask user to enter the path to the merged CSV
    path = input("Enter the path to the merged CSV file produced by the merger:\n")
    path = path.strip("'\"")
    print(f"Using merged file: {path}")

data = []

with open(path, "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for line in reader:
        data.append({
            "latitude": float(line["latitude"]),
            "longitude": float(line["longitude"])
        })

# print(data)


fig = px.scatter_map(
    data, # list of dictionaries
    lat="latitude",        
    lon="longitude",       
    zoom=3,
    height=600,
    width=800,
    title="Location History"
)

fig.show()
