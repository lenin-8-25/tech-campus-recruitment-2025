Discussion.md

# Solutions Considered
1. Reading the Entire File into Memory
     Pros: Simple implementation.
     Cons: Not feasible for large files (1TB) due to high memory usage.

2. Streaming Line by Line Processing
     Pros: Efficient memory usage, suitable for large files.
     Cons: Slower if searching across unsorted logs.

3. Using Memory Mapped Files (mmap)
     Pros: Faster access to large files.
     Cons: Complexity and potential compatibility issues.

4. Indexing Logs by Date for Faster Lookup
     Pros: Quick retrieval once indexed.
     Cons: Requires pre processing and storage overhead.

5. Extracting and Processing Logs from a Zip File
     Pros: Saves storage space, avoids extracting the whole zip manually.
     Cons: Slightly slower due to extraction overhead.

### Final Solution Summary
The chosen solution efficiently extracts logs by:
  Unzipping the `.log` file directly from the zip.
  Streaming line by line to filter logs matching the given date.
  Writing the filtered logs to an output file.

This approach balances memory efficiency and processing speed while handling large log files.

### Steps to Run
1. Ensure Prerequisites:
     Python 3 installed
     The log file zip (`logs_2024.log.zip`) present at `"C:\Users\LENIN SAI\Downloads\logs_2024.log.zip"`
   
2. Run the Script:
      python extract_logs.py YYYY MM DD
   
   Example:
      python extract_logs.py 2024 12 01
   

3. Check the Output:
     The filtered logs will be saved outside the `src` directory in the `../output/` folder as `output_YYYY MM DD.txt`.
     Example: `../output/output_2024 12 01.txt`.

4. Handle Errors:
     Ensure the zip file path is correct.
     Check for read/write permissions in the output directory.

