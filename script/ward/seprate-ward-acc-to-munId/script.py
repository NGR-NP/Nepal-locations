import os
import json

# Load the JSON data
with open('koshi-wards.json', 'r') as file:
    data = json.load(file)

# Dictionary to store the extracted data grouped by mun_Name
extracted_data_by_munName = {}

# Iterate over each record in the data
for record in data:
    mun_name = record.get('mun_Name')
    #mun_id = record.get('munId')
    provinceId = record.get("provinceId")
    # Append to the dictionary based on mun_Name
    if mun_name is not None:
        if mun_name not in extracted_data_by_munName:
            extracted_data_by_munName[mun_name] = []
        extracted_data_by_munName[mun_name].append(record)

# Create a new folder if it doesn't exist
folder_name = str(provinceId)
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Save the extracted data to separate files based on mun_Name inside the new folder
for mun_name, data_list in extracted_data_by_munName.items():
    filename = os.path.join(folder_name, f'{mun_name}.json')
    with open(filename, 'w') as file:
        json.dump(data_list, file, indent=2)

