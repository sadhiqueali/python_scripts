import time

def watch_log_file(file_path, keywords=["ERROR", "CRITICAL"]):
    """
    Watches a log file for specific error keywords.

    :param file_path: Path to the log file.
    :param keywords: List of keywords to watch for (e.g., "ERROR", "CRITICAL").
    """
    print(f"Watching {file_path} for errors...\n")
    try:
        with open(file_path, 'r') as log_file:
            # Move the file pointer to the end of the file
            log_file.seek(0, 2)
            
            while True:
                line = log_file.readline()
                if line:
                    # Check if the line contains any of the keywords
                    if any(keyword in line for keyword in keywords):
                        print(f"[{time.ctime()}] Error Detected: {line.strip()}")
                else:
                    time.sleep(1)  # Wait before checking for new lines
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except KeyboardInterrupt:
        print("\nStopped watching the log file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Replace with your server log file path
    log_file_path = "/var/log/server.log"
    
    # Call the function
    watch_log_file(log_file_path)
