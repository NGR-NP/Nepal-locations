import json
import os
def safe_load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Failed to load {file_path}: {str(e)}")
        return None

# Usage:
# Replace './' with the path to your JSON files
for filename in os.listdir('./'):
    if filename.endswith('.json'):
        data = safe_load_json(filename)
        if data is not None:
            # Process the data...
            pass
