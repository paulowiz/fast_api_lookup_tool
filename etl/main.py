import sys, logging

sys.path.append("../..")
from datetime import datetime
from utils import download_and_extract_zip, remove_large_files, list_files_in_folder
import pandas as pd
import concurrent.futures
import os
from database import sync_engine

DATASET_URL = os.environ.get('DATASET_URL')
OUTPUT_FOLDER = os.environ.get('OUTPUT_FOLDER')
LOCAL_RUN =  os.environ.get('LOCAL_RUN')

# Logging configuration
formatter = logging.Formatter('[%(asctime)s] %(levelname)s @ line %(lineno)d: %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# current time variable to be used for logging purpose
dt_string = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

logger.info("Starting Extraction.....")
logger.info("Downloading and extracting zip file")

download_and_extract_zip(url=DATASET_URL, destination_folder=OUTPUT_FOLDER)

if LOCAL_RUN:
    logger.info("Removing big files just for the assigment...")
    remove_large_files(folder_path=OUTPUT_FOLDER, size_limit_gb=0.02)

logger.info("Starting Transform process.")

file_paths = list_files_in_folder(OUTPUT_FOLDER)


def read_file(file_path):
    df = pd.read_json(file_path, lines=True,
                      compression='gzip')
    return df


# Initialize an empty DataFrame
combined_df = pd.DataFrame()

max_cores = min(len(file_paths), os.cpu_count())  # Adjust this if needed
logger.info("Combining Datasets into one dataframe...")
# Use multithreading to read files concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=max_cores) as executor:
    future_to_path = {executor.submit(read_file, path): path for path in file_paths}
    for future in concurrent.futures.as_completed(future_to_path):
        file_path = future_to_path[future]
        try:
            df = future.result()
            combined_df = pd.concat([combined_df, df], ignore_index=True)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

logger.info("Cleaning Dataframe...")
df_properties = pd.DataFrame.from_records(combined_df['properties'])
df_properties = df_properties.drop_duplicates(subset=['hash'], keep='last')
df_properties = df_properties[df_properties['hash'] != 'e70d2a522603d9f0']
df_geometry = pd.DataFrame.from_records(combined_df['geometry'])

df_joined = pd.merge(df_properties, df_geometry, left_index=True, right_index=True)

logger.info("Loading Dataframe to Database.")
df_joined.to_sql('address', sync_engine, if_exists='replace', index=False)
