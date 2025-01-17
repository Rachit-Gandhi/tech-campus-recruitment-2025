import sys
import os

def extract_logs(file_path, target_date, output_dir="output"):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Output file path
    output_file_path = os.path.join(output_dir, f"output_{target_date}.txt")
    
    try:
        # Open the input file in read mode
        with open(file_path, 'r') as file:
            # Open the output file in write mode
            with open(output_file_path, 'w') as output_file:
                # Process file line by line
                for line in file:
                    # Check if the line starts with the target date
                    if line.startswith(target_date):
                        output_file.write(line)
        
        print(f"Logs for {target_date} have been extracted to {output_file_path}.")
    
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to handle command-line arguments
if __name__ == "__main__":
    
    log_file_path = sys.argv[1]
    date_to_extract = sys.argv[2]
    
    extract_logs(log_file_path, date_to_extract)
