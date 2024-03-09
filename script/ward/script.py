import json

# Load the JSON data
with open('koshi-ward-data.json', 'r') as file:
    data = json.load(file)

# Access the first element of the list to get to the "features" field
features = data[0]['features']

# List to store the extracted data
extracted_data = []

# Iterate over each feature
for feature in features:
    # Extract "munid" and "LU_Name" fields from "properties"
    properties = feature.get('properties', {})
    id = properties.get('id')
    ward_number = properties.get('new_ward_n')
    mun_id = properties.get('munid')
    mun_name = properties.get('GaPa_NaP_1')
    dis_id = properties.get('districtid')
    province_id = int(properties.get('state',11))
    # Append to the list if both fields are present
    if id is not None and ward_number is not None:
        extracted_data.append({'id': id,  'ward_Num': ward_number,'mun_Name': mun_name, 'munId': mun_id, 'disId': dis_id, 'provinceId': province_id})

# Save the extracted data
with open('koshi-ward.json', 'w') as file:
    json.dump(extracted_data, file, indent=2)
