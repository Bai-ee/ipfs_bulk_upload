import os
import json
import ipfshttpclient

def remove_ds_store(folder_path):
    ds_store_path = os.path.join(folder_path, '.DS_Store')
    if os.path.exists(ds_store_path):
        os.remove(ds_store_path)

def upload_files(folder_path, client):
    uploaded_files = {}
    remove_ds_store(folder_path)  # Remove .DS_Store file if present

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            res = client.add(os.path.join(folder_path, filename))
            uploaded_files[filename] = res['Hash']

    return uploaded_files

def create_links_file(uploaded_files, links_file_name='links.txt'):
    links_data = []
    with open(links_file_name, 'w') as file:
        for filename, ipfs_hash in uploaded_files.items():
            link_info = {'filename': filename.rsplit('.', 1)[0], 'ipfs_link': f'ipfs://{ipfs_hash}'}
            links_data.append(link_info)
            file.write(f'{filename}: ipfs://{ipfs_hash}\n')
    return links_data

def update_json_metadata(json_file, links_data):
    with open(json_file, 'r') as file:
        data = json.load(file)

    for item in data['collection_items']:
        for link in links_data:
            if item['name'].strip() == link['filename'].strip():
                item['external_url'] = link['ipfs_link']

    with open(json_file.replace('.json', '_FINAL.json'), 'w') as file:
        json.dump(data, file, indent=4)

def main():
    folder_path = 'images'  # Update with your folder path
    json_file = 'metadata.json'  # Update with your JSON file path

    client = ipfshttpclient.connect('/dns/localhost/tcp/5001/http')
    uploaded_files = upload_files(folder_path, client)
    links_data = create_links_file(uploaded_files)
    update_json_metadata(json_file, links_data)

if __name__ == "__main__":
    main()
