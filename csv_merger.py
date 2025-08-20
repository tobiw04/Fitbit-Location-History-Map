import csv
import glob

path_pattern = input("Enter the full path to the directory with the CSV files you want to merge:\n")
path_pattern = path_pattern.strip("'") # removes quotation marks
path_pattern = path_pattern+"/*.csv"

# print(path_pattern)

new_file_path = input("Target directory for the merged CSV file:\n")
new_file_path = new_file_path.strip("'")

new_file_name = input("New file name:\n")
new_file_name = new_file_name.strip("'")
if not new_file_name.endswith('.csv'):
    new_file_name = new_file_name+".csv"

if not new_file_path.endswith('/'):
    new_file_path = new_file_path+"/"

new_file_path = new_file_path+new_file_name

# print(new_file_path)

th_row = input("Factor for reducing file size (Recommended: 240):\n")
th_row = int(th_row)
'''
Fitbit saves location every second. Since we don't want out CSV file to get too large,
we'll only keep every 240th row.
'''

rows = []
first_file = True
row_count = 0

for path in glob.glob(path_pattern):
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        if first_file:

            header = next(reader, None)
            if header:
                rows.append(header)
            first_file = False
        
        for idx, row in enumerate(reader, start=1):
            if idx % th_row == 0: # adding only every 240th row
                rows.append(row)
                row_count += 1


with open(new_file_path, mode='w', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)

print(f"Merge was successful. New file saved to: \n")
print(new_file_path)