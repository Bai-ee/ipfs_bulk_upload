IPFS Bulk Upload Tool
Description
This repository contains a Python script designed for efficiently uploading images to the InterPlanetary File System (IPFS) and updating an associated JSON file with the resultant IPFS hashes (CIDs). Primarily, the script automates the removal of .DS_Store files (specific to macOS), facilitates the batch uploading of images from a specified directory to an IPFS node, and generates a text file containing links to these uploaded images. Additionally, it efficiently updates an existing metadata/JSON file with new IPFS links, making it a valuable tool for projects that necessitate bulk asset uploads to IPFS along with corresponding metadata updates.

Installation and Usage
Prerequisites
Ensure Python is installed on your system.
Set up an IPFS node either on your local machine or a server.
Installation
Install the IPFS HTTP Client Library:
Copy code
pip install ipfshttpclient
Preparing Your Data
Place the images intended for upload in a designated folder (e.g., 'images').
Prepare a JSON file (e.g., 'metadata.json') to be updated with IPFS links.
Configuration
In the script's main function, update the folder_path to your image folder's path.
Update the json_file path to your JSON file.
Execution
Run the script:
php
Copy code
python <script_name>.py
This script will efficiently upload your images to the configured IPFS node, create a file with the links, and update your JSON metadata file with the new IPFS links.