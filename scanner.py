import pyfiglet
import socket
from datetime import datetime
from colorama import Fore, Style, init
import os
import argparse
import concurrent.futures
import logging
import sys
import signal

init()

# Global flag to stop threads
stop_flag = False

# Define a signal handler to handle keyboard interrupts
def signal_handler(sig, frame):
    global stop_flag
    stop_flag = True
    logging.error("Scan interrupted by user")

signal.signal(signal.SIGINT, signal_handler)

# clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# print the ASCII banner
def print_banner():
    ascii_banner = pyfiglet.figlet_format("THIRD EYE", font="starwars")
    print(Fore.CYAN + ascii_banner + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + "A Professional Port Scanner" + Style.RESET_ALL + "\n")

# Function to resolve the target hostname to an IP address
def resolve_hostname(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        logging.error("Invalid hostname or IP address")
        sys.exit()

# Function to scan a specific port
def scan_port(target, port):
    if stop_flag:
        return None
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            socket.setdefaulttimeout(0.5)  # Adjusted timeout for faster scanning
            result = s.connect_ex((target, port))
            if result == 0:
                logging.info(Fore.GREEN + f"Port {port} is open" + Style.RESET_ALL)
                return port
            elif verbose:
                logging.debug(Fore.RED + f"Port {port} is closed" + Style.RESET_ALL)
            return None
    except socket.error as e:
        logging.error(Fore.RED + f"Socket error on port {port}: {e}" + Style.RESET_ALL)
    except Exception as e:
        logging.error(Fore.RED + f"Unexpected error on port {port}: {e}" + Style.RESET_ALL)

# strat scanning ports
def start_scanning(target, start_port, end_port, num_threads=100):
    open_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_port = {executor.submit(scan_port, target, port): port for port in range(start_port, end_port + 1)}

        for future in concurrent.futures.as_completed(future_to_port):
            if stop_flag:
                break
            port = future_to_port[future]
            try:
                result = future.result()
                if result is not None:
                    open_ports.append(result)
            except Exception as e:
                logging.error(Fore.RED + f"Exception occurred: {e}" + Style.RESET_ALL)

    return open_ports

# main function
def main():
    clear_screen()
    print_banner()

    parser = argparse.ArgumentParser(description="A simple port scanner")
    parser.add_argument("target", help="Target hostname or IP address")
    parser.add_argument("-sp", "--start-port", type=int, default=1, help="Starting port number (default: 1)")
    parser.add_argument("-ep", "--end-port", type=int, default=65535, help="Ending port number (default: 65535)")
    parser.add_argument("-nt", "--num-threads", type=int, default=100, help="Number of threads to use (default: 100)")
    parser.add_argument("-v", "--verbose", action='store_true', help="Enable verbose output")

    args = parser.parse_args()

    # Configure logging based on verbose mode
    global verbose
    verbose = args.verbose
    logging_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=logging_level, format='%(asctime)s - %(levelname)s - %(message)s')

    target = resolve_hostname(args.target)
    start_port = args.start_port
    end_port = args.end_port
    num_threads = args.num_threads

    logging.info(Fore.CYAN + f"Scanning Target: {target}" + Style.RESET_ALL)
    logging.info(Fore.CYAN + f"Scanning Port Range: {start_port} to {end_port}" + Style.RESET_ALL)
    logging.info(Fore.CYAN + f"Scanning started at: {datetime.now()}" + Style.RESET_ALL)

    try:
        open_ports = start_scanning(target, start_port, end_port, num_threads)
    except KeyboardInterrupt:
        logging.error(Fore.RED + "Scan interrupted by user" + Style.RESET_ALL)
    except Exception as e:
        logging.error(Fore.RED + f"An unexpected error occurred: {e}" + Style.RESET_ALL)
    finally:
        logging.info(Fore.YELLOW + "-" * 50 + Style.RESET_ALL)
        logging.info(Fore.YELLOW + "Scan Summary" + Style.RESET_ALL)
        logging.info(Fore.YELLOW + "-" * 50 + Style.RESET_ALL)
        logging.info(Fore.CYAN + f"Target IP Address: {target}" + Style.RESET_ALL)
        logging.info(Fore.CYAN + f"Port Range Scanned: {start_port}-{end_port}" + Style.RESET_ALL)
        logging.info(Fore.CYAN + f"Open Ports: {', '.join(map(str, open_ports)) if open_ports else 'None'}" + Style.RESET_ALL)
        logging.info(Fore.YELLOW + "-" * 50 + Style.RESET_ALL)
        logging.info(Fore.YELLOW + f"Scanning completed at: {datetime.now()}" + Style.RESET_ALL)
        logging.info(Fore.YELLOW + "-" * 50 + Style.RESET_ALL)

if __name__ == "__main__":
    main()
