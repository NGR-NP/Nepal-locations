import json

# Load the JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Access the first element of the list to get to the "features" field
features = data[0]['features']

# Iterate over each feature
for feature in features:
    # Remove the "geometry" field if it exists
    if 'geometry' in feature:
        del feature['geometry']
    # Remove the "style" field if it exists in the "properties" field
    if 'properties' in feature and 'style' in feature['properties']:
        del feature['properties']['style']

# Save the modified data
with open('modified_data.json', 'w') as file:
    json.dump(data, file, indent=2)
