import json

# Load the JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Access the first element of the list to get to the "features" field
features = data[0]['features']

# List to store the extracted data
extracted_data = []

# Iterate over each feature
for feature in features:
    # Extract "munid" and "LU_Name" fields from "properties"
    properties = feature.get('properties', {})
    name = properties.get('Name')
    id = properties.get('districtiD')
    # Append to the list if both fields are present
    if id is not None and name is not None:
        extracted_data.append({'disid': id, 'dis_Name': name})

# Save the extracted data
with open('extracted_data.json', 'w') as file:
    json.dump(extracted_data, file, indent=2)
