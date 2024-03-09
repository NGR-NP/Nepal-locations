import json
import os

# Function to merge JSON files
def merge_json_files(directory, output_file):
    combined_data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename)) as f:
                data = json.load(f)
                combined_data.extend(data)
    
    # Save the combined data to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(combined_data, f, indent=4)

# Example usage:
# Call the function with the directory containing your JSON files and the name of the output file
merge_json_files('./', 'combined_data.json')
