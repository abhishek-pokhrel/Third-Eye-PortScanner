THIRD EYE - Professional Port Scanner
Overview
THIRD EYE is a professional port scanner designed to identify open ports on a target system. It leverages multi-threading to ensure fast and efficient scanning. The tool provides a clear and colorful output using ASCII art and color-coded logging to enhance usability.

Features
Multi-threaded Scanning: Scans multiple ports simultaneously to speed up the process.
Customizable Parameters: Allows users to specify the port range, number of threads, and verbosity.
Color-coded Output: Uses colorama for enhanced readability in terminal.
Interrupt Handling: Gracefully handles user interruptions and provides a summary of the scan.
Requirements
Python 3.6 or later
Dependencies listed in requirements.txt
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/third-eye.git
cd third-eye
Install Dependencies:

Make sure you have pip installed. Then, install the required packages:

bash
Copy code
pip install -r requirements.txt
Usage
To use THIRD EYE, run the scanner.py script from the command line with the desired arguments.

Command-Line Arguments
target: Target hostname or IP address (required).
-sp or --start-port: Starting port number (default: 1).
-ep or --end-port: Ending port number (default: 65535).
-nt or --num-threads: Number of threads to use (default: 100).
-v or --verbose: Enable verbose output for detailed logs.
Example
bash
Copy code
python scanner.py example.com -sp 20 -ep 80 -nt 50 -v
This command scans ports 20 to 80 on example.com using 50 threads and enables verbose logging.

Output
The tool will display the following:

ASCII Banner: A visually appealing banner with the tool’s name.
Scan Status: Updates on the target, port range, and start time.
Port Status: Indicates which ports are open or closed.
Summary: A detailed summary of the scan including target IP, scanned port range, and open ports.
Signal Handling
The scanner handles keyboard interrupts (Ctrl+C) gracefully and will stop scanning when interrupted, providing a summary of the scan up to that point.

Error Handling
The tool provides error messages for issues such as invalid hostnames, socket errors, and unexpected exceptions, helping users troubleshoot problems effectively.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or support, please contact [your email address] or open an issue on the GitHub repository.