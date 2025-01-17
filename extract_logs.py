import os
import sys
from concurrent.futures import ThreadPoolExecutor

def process_chunk(chunk_lines, target_date, output_file):
    """
    Processes a chunk of lines and writes matching logs to the output file.
    """
    matching_lines = [line for line in chunk_lines if line.startswith(target_date)]
    with open(output_file, "a") as f:  # Append to avoid overwriting
        f.writelines(matching_lines)

def extract_logs_multithreaded(file_path, target_date, output_dir="output", num_threads=4, chunk_size=10**6):
    """
    Efficiently extracts logs for the given date from a large file using multithreading.
    """
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Output file path
    output_file_path = os.path.join(output_dir, f"output_{target_date}.txt")

    try:
        # Open the input file in read mode
        with open(file_path, 'r') as file:
            with ThreadPoolExecutor(max_workers=num_threads) as executor:
                chunk_lines = []
                futures = []

                for i, line in enumerate(file):
                    chunk_lines.append(line)
                    
                    # Process in chunks
                    if len(chunk_lines) >= chunk_size:
                        # Submit a thread to process this chunk
                        futures.append(executor.submit(process_chunk, chunk_lines, target_date, output_file_path))
                        chunk_lines = []

                # Process the remaining lines
                if chunk_lines:
                    futures.append(executor.submit(process_chunk, chunk_lines, target_date, output_file_path))

                # Wait for all threads to complete
                for future in futures:
                    future.result()

        print(f"Logs for {target_date} have been extracted to {output_file_path}.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to handle command-line arguments
if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    date_to_extract = sys.argv[1]
    # Default log file path in the src folder
    log_file_path = os.path.join("src", "test_logs.log")

    if not os.path.exists(log_file_path):
        print(f"Error: The file {log_file_path} does not exist.")
        sys.exit(1)

    extract_logs_multithreaded(log_file_path, date_to_extract)
