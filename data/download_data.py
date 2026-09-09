# data/download_data.py
import os  # deal with file paths and directories
import pandas as pd  # for handling tabular data

# Permanent OpenML source for French Motor Insurance Claims dataset (freMTPL2freq) 
DATA_URL = "https://www.openml.org/data/get_csv/20649148/freMTPL2freq.csv" # the data website
OUTPUT_PATH = os.path.join("data", "raw_business_data.csv")     # Where you want to save the downloaded data

def fetch_raw_data():  #define a function (name is fetch_raw_data) to fetch and save raw data #When Python encounters `def`, it simply "remembers how the function works" without actually executing the code inside it.
    print(f"[*] Extracting raw data from:\n    {DATA_URL}")
    try:
        df = pd.read_csv(DATA_URL) #This line actually reads the CSV data from the URL into a DataFrame
        os.makedirs("data", exist_ok=True)  # create the "data" directory if it doesn't already exist
        df.to_csv(OUTPUT_PATH, index=False)  # save the DataFrame to a CSV file
        print(f"[+] Saved locally to: {OUTPUT_PATH}") # print a confirmation message that the data has been saved locally
        print(f"[+] Record Count: {len(df)} rows x {len(df.columns)} columns") # print the number of rows and columns in the downloaded data
    except Exception as e:  # catch any exceptions that may occur during data fetching and saving
        raise Exception(f"[-] Download failed: {e}")

if __name__ == "__main__":  # this block ensures that the function is only called when the script is run directly, not when it's imported as a module

    fetch_raw_data()  # call the function to fetch and save the raw data