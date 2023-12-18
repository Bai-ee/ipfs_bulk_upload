# IPFS Bulk Upload Tool

## Description
This repository hosts a Python script for bulk uploading images to IPFS and updating an associated JSON file with the IPFS hashes (CIDs). It's designed to remove `.DS_Store` files, upload images from a specified directory to an IPFS node, and generate a text file with links to the uploaded images. Additionally, it updates an existing metadata/JSON file with new IPFS links. This tool is invaluable for projects requiring batch uploading of assets to IPFS and automated metadata updates.

## Installation and Usage

### Prerequisites
- Python installation
- An IPFS node set up locally or on a server

### Installation
1. Install IPFS HTTP Client Library: pip install ipfshttpclient

### Data Preparation
- Place images in a folder (e.g., 'images').
- Prepare a JSON file (e.g., 'metadata.json') for updating with IPFS links.

### Configuration
- Update `folder_path` in the script's `main` function to the path of your images folder.
- Update `json_file` to the path of your JSON file.

### Execution
- Run the script: python <script_name>.py

The script uploads images to IPFS, creates a links file, and updates the JSON file with new IPFS links.
