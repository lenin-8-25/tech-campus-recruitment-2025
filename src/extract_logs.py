import sys
import os
import zipfile

def extract_logs(date, zip_file, output_dir="output"):
    """Extracts logs for a specific date from a zipped log file."""
    # Ensure output directory exists
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "output"))
    
    # Extract the .log file from the zip
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        log_file = None
        for file_name in zip_ref.namelist():
            if file_name.endswith(".log"):
                log_file = os.path.join(output_dir, file_name)
                zip_ref.extract(file_name, output_dir)
                break
        
    if not log_file:
        print("No .log file found in the zip archive.")
        return
    
    output_file = os.path.join(output_dir, f"output_{date}.txt")
    
    try:
        with open(log_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            for line in infile:
                if line.startswith(date):
                    outfile.write(line)
        print(f"Logs for {date} saved to {output_file}")
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)
    
    date = sys.argv[1]
    zip_file = r"C:\Users\LENIN SAI\Downloads\logs_2024.log.zip" # Update with the actual zip file path
    extract_logs(date, zip_file)
