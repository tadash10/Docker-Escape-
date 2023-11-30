def main():
    try:
        setup_logging()
        logging.info("Welcome to the Advanced Docker Escape Attempt!")

        display_disclaimer()

        while True:
            print_menu()
            choice = get_valid_choice()

            if choice == '1':
                privilege_escalation_checks()
            elif choice == '2':
                security_context_verification()
            elif choice == '3':
                configure_nsenter()
            elif choice == '4':
                exploit_vulnerabilities()
            elif choice == '5':
                enhance_logging()
            elif choice == '6':
                post_escape_analysis()
            elif choice == '7':
                generate_report()
            elif choice == '8':
                logging.info("Exiting the Advanced Docker Escape Attempt. Goodbye!")
                break
    except KeyboardInterrupt:
        logging.info("Script terminated by the user. Cleaning up...")
        # Add cleanup code if needed
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        # Add cleanup code if needed
    finally:
        # Add any cleanup code that should run regardless of how the script exits
