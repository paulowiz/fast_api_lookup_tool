import os
import requests
import zipfile
from typing import List


def remove_large_files(folder_path: str, size_limit_gb: float) -> None:
    """
    Remove large files with more than a size limit in Gigabits.

    :param folder_path: folder with files
    :param size_limit_gb: size in Gigabits
    :return: None
    """
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                file_size_gb = os.path.getsize(file_path) / (1024 ** 3)
                if file_size_gb > size_limit_gb:
                    os.remove(file_path)
                    print(f"Removed: {file_path} (Size: {file_size_gb:.2f} GB)")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")


def download_and_extract_zip(url: str, destination_folder: str) -> None:
    """

    :param url: URL with zip file
    :param destination_folder: download destination and extraction
    :return: None
    """
    os.makedirs(destination_folder, exist_ok=True)
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to download the ZIP file.")
        return

    zip_file_path = os.path.join(destination_folder, "downloaded_file.zip")
    with open(zip_file_path, 'wb') as f:
        f.write(response.content)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)

    os.remove(zip_file_path)


def list_files_in_folder(folder_path: str) -> List[str]:
    """

    :param folder_path: Folder with files
    :return: List(str) string list with filepaths
    """
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_paths.append(file_path)
    return file_paths
