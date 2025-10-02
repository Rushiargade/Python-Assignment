import configparser
import json
import os
from flask import Flask, jsonify

# Read configuration file
config_file = 'config.ini'
config_data = {}

try:
    if not os.path.exists(config_file):
        raise FileNotFoundError("Configuration file not found.")
    
    config = configparser.ConfigParser()
    config.read(config_file)

    # Extract sections into a dictionary
    for section in config.sections():
        config_data[section] = dict(config.items(section))
except Exception as e:
    print(f"Error: {e}")

# Save extracted data as JSON
json_file = 'config_data.json'
try:
    with open(json_file, 'w') as f:
        json.dump(config_data, f, indent=4)
except Exception as e:
    print(f"Error saving JSON data: {e}")

# Simple Flask app for GET request
app = Flask(__name__)

@app.route('/config', methods=['GET'])
def get_config():
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
