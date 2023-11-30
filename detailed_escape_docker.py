# File: detailed_escape_docker.py

import os
import subprocess
import logging
from datetime import datetime

def setup_logging():
    log_filename = f'escape_docker_{datetime.now().strftime("%Y%m%d%H%M%S")}.log'
    logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s [%(levelname)s]: %(message)s')

def check_privilege_escalation():
    try:
        # Check for sudo privileges
        subprocess.run(['sudo', '-l'], check=True)
        logging.info("Privilege escalation check successful. User has sudo privileges.")
    except subprocess.CalledProcessError:
        logging.warning("Privilege escalation check failed. User may not have sudo privileges.")

def verify_security_context():
    try:
        # Check for AppArmor or SELinux
        apparmor_status = subprocess.run(['apparmor_status'], check=True, stdout=subprocess.PIPE, text=True).stdout
        selinux_status = subprocess.run(['sestatus'], check=True, stdout=subprocess.PIPE, text=True).stdout

        logging.info(f"AppArmor Status:\n{apparmor_status}")
        logging.info(f"SELinux Status:\n{selinux_status}")

    except subprocess.CalledProcessError:
        logging.warning("Error while checking security context.")

def configure_nsenter():
    try:
        # Configure nsenter options
        subprocess.run(['echo', 'kernel.unprivileged_userns_clone=1', '|', 'sudo', 'tee', '-a', '/etc/sysctl.conf'], check=True)
        subprocess.run(['sudo', 'sysctl', '-p'], check=True)
        logging.info("nsenter options configured successfully.")
    except subprocess.CalledProcessError:
        logging.warning("Error while configuring nsenter options.")

def enhanced_logging():
    # Improve logging with timestamps
    logging.info("Enhanced logging with timestamps...")

def post_escape_analysis():
    # Provide information about the host system post-escape
    # Example: Display kernel version, running processes, network configuration, etc.
    logging.info("Performing post-escape analysis...")

def main():
    setup_logging()
    logging.info("Welcome to the Enhanced Docker Escape Room!")
    logging.info("In this exercise, you'll attempt to escape from a Docker container to the underlying host system.")

    # Check for privilege escalation opportunities
    check_privilege_escalation()

    # Verify the security context within the container and on the host
    verify_security_context()

    # Allow configuration of nsenter options
    configure_nsenter()

    # Enhance logging with timestamps
    enhanced_logging()

    # Get the ID of the current Docker container
    container_id = get_container_id()

    if container_id:
        logging.info(f"Your current Docker container ID is: {container_id}")
        logging.info("Attempting to escape from the container...")

        # Use nsenter to enter the host namespace
        success = escape_from_container(container_id)

        if success:
            logging.info("Congratulations! You've successfully escaped from the Docker container.")
            
            # Perform post-escape analysis
            post_escape_analysis()

        else:
            logging.error("Oops! Something went wrong. Unable to escape from the Docker container.")
    else:
        logging.error("Unable to retrieve the Docker container ID. Are you sure this script is running inside a Docker container?")

if __name__ == "__main__":
    main()
