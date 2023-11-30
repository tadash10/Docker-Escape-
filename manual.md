CLI Manual
Installation
Prerequisites

    Python 3.x
    Docker environment

Steps

    Clone the repository:

    bash

git clone https://github.com/yourusername/docker-escape-attempt.git

Navigate to the script directory:

bash

cd docker-escape-attempt

Install dependencies:

bash

    pip install -r requirements.txt

Usage

Run the script using the following command:

bash

python escape_attempt.py

The script will display a menu with the following options:

    Perform Privilege Escalation Checks
    Verify Security Context
    Configure nsenter Options
    Exploit Vulnerabilities
    Enhance Logging
    Perform Post-Escape Analysis
    Generate Report
    Exit

Enter a number corresponding to the desired action and follow the on-screen instructions.
Options Overview
1. Perform Privilege Escalation Checks

This option checks for various privilege escalation vectors. If successful, it logs that the user has sudo privileges.
2. Verify Security Context

This option checks the security context within the container and on the host. It displays information about AppArmor and SELinux status.
3. Configure nsenter Options

This option configures nsenter options, allowing you to enter a new user namespace. It modifies the /etc/sysctl.conf file and applies the changes.
4. Exploit Vulnerabilities

This option is a placeholder for exploiting potential vulnerabilities in the host system. Additional exploitation steps can be added as needed.
5. Enhance Logging

This option enhances logging with timestamps and detailed context. Additional logging enhancements can be added.
6. Perform Post-Escape Analysis

This option is a placeholder for performing post-escape analysis. Additional post-escape analysis steps can be added.
7. Generate Report

This option generates a detailed report in the script directory. The report includes information on privilege escalation checks, security context verification, nsenter configuration, vulnerability exploitation, and post-escape analysis.
8. Exit

This option exits the script.
Exit Handling

The script includes proper exit handling, ensuring cleanup code is executed in case of unexpected terminations. If the script is terminated by the user (Ctrl+C), it will attempt to perform cleanup operations.
Contributions

Contributions and feedback are welcome. Feel free to submit issues or pull requests.
