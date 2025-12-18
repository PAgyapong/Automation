# To begin  the project, I will import datetime because it
#will allow me to prefix it .

import datetime
from datetime  import datetime

# importing socket will allow low level network operations,like establishing connections.

import socket
from urllib.parse import urlparse

# Will request this so its can save my webpage under the option 5.
import requests

# importing paramiko so the script will act as ssh client.
import paramiko
from paramiko.ssh_exception import  AuthenticationException


print("Hello World")

class NewAutomationMenu:
    def __init__(self):
        # Remote server credentials (hardcoded as per requirements) Hardcoded to prevent anyone,
         # change it without modifying the source, and it will required code before one

        self.remote_host = "127.0.0.1"  #  IP Address
        self.remote_username = "prince"  #  username
        self.remote_password = "nanayaw3092"  #  password
        self.remote_port = 5679


    # Now going to display the menu. # will use "\n" + "=" * 40 to give a nice
    #holizontal  on top and underneath of the title of the menu.


    def display_menu(self):
        """Display the main menu options"""
        print("\n" + "<->" * 15)
        print("         ARU NEW AUTOMATION ")
        print("<->" * 15)
        print("1. Show date and time (local computer)")
        print("2. Show IP address (local computer)")
        print("3. Show remote home directory listing")
        print("4. Backup remote file")
        print("5. Save web page")
        print("Q. Quit")
        print("<->" * 15)

    # im defining the option 1, which I will use def,try,and except to show the date and time

    def option_1_show_datetime (self):
        """Option 1: Display current local date and time"""
        try:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            print(f"\nCurrent Local Date and Time: {formatted_datetime}")
        except Exception as e:
            print(f"Error retrieving date and time: {e}")

    # im defining the option 2 which I will use def,try,and
    # except to show the date and time

    def option_2_show_ip_address(self):
        """Option 2: Display IP address of local computer"""
        try:
            # Get hostname and corresponding IP address
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            print(f"\nLocal Computer Information:")
            print(f"Hostname: {hostname}")
            print(f"IP Address: {ip_address}")
        except Exception as e:
            print(f"Error retrieving IP address: {e}")

    # im defining the option 3 which I will use def,try,and
    # except to show the date and time

    def option_3_remote_directory_listing(self):
        """Option 3: Display contents of remote home directory"""
        try:
            print(f"\nConnecting to remote server: {self.remote_host}")

            # Create SSH client

            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect to remote server by using ssh paramiko

            ssh_client.connect(
                hostname=self.remote_host,
                username=self.remote_username,
                password=self.remote_password,
                port=self.remote_port
            )

            # Execute command to list home directory.

            stdin, stdout, stderr = ssh_client.exec_command('ls -la ~')
            directory_listing = stdout.read().decode()

            print(f"Remote Home Directory Listing:")
            print("-" * 40)
            print(directory_listing)

            # Close ssh connection

            ssh_client.close()

        except paramiko.AuthenticationException:
            print("Error: Authentication failed. Please check username and password.")
        except paramiko.SSHException as e:
            print(f"SSH1"
                  f" connection error: {e}")
        except Exception as e:
            print(f"Error connecting to remote server: {e}")

    # im defining the option 4 which I will use def,try,and
    # except to show the date and time

    def option_4_backup_remote_file(self):
        """Option 4: Backup remote file with .old suffix"""
        try:
            file_path = input("\n  Enter your full path to the file  ").strip()

            if not file_path:
                print("Error: No file path provided.")
                return

            print(f"Attempting to backup: {file_path}")

            # Create SSH client
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect to remote server
            ssh_client.connect(
                hostname=self.remote_host,
                username=self.remote_username,
                password=self.remote_password,
                port=self.remote_port
            )

            # Create backup by copying file with .old extension


            backup_command = f'cp "{file_path}" "{file_path}.old"'
            stdin, stdout, stderr = ssh_client.exec_command(backup_command)

            # Check for errors

            error_output = stderr.read().decode()
            if error_output:
                print(f" Sorry Error creating backup: {error_output}")
            else:
                print(f" Well done Backup created successfully: {file_path}.old")


            # Close connection

            ssh_client.close()

        except Exception as e:
            print(f"Error during remote backup: {e}")

    # will define a class, a templet from which I can instantiate and objects to a def: which
    # is doing to define the functions and that will be use once but will run through.


    def option_5_save_webpage(self):
        """Option 5: Save web page content to local file"""
        try:
            url = input("\n Enter the Full URL of the webpage: ").strip()

            if not url:
                print("Error: No URL provided.")
                return

            # def Validate URL format

            parsed_url = urlparse(url)
            if not parsed_url.scheme:
                url = "https://" + url

            print(f"Downloading content from: {url}")

            # Send HTTP GET request

            response = requests.get (url, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes


            # Create filename from URL
            filename = parsed_url.netloc + ".html" if parsed_url.netloc else "webpage.html"


            # Save content to file,

            with open(filename, "w", encoding='utf-8') as file:
                file.write(response.text)

            print(f"Web page saved successfully as: {filename}")
            print(f"File size: {len(response.text)} characters")

        except requests.exceptions.RequestsException as e:
            print(f"Error downloading web page: {e}")
        except Exception as e:
            print(f"Error saving web page: {e}")


    # im defining the option 2 which I will use def,try,and
    # except to show the date and time

    def run(self):
        """Main program loop"""
        print("New Automation  Starting...")

        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5 or Q): ").strip().upper()

            if choice == "1":
                self.option_1_show_datetime()
            elif choice == "2":
                self.option_2_show_ip_address()
            elif choice == "3":
                self.option_3_remote_directory_listing()
            elif choice == "4":
                self.option_4_backup_remote_file()
            elif choice == "5":
               self. option_5_save_webpage()
            elif choice == "Q":
                print("\nThank you for using ARU MENU .... Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter 1, 2, 3, 4, 5, or Q.")


            # Pause before showing menu again
            if choice != "Q":
                input("\nPress Enter to continue...")


def main():
    """Main function to start the program"""
    try:
        tool = NewAutomationMenu()
        tool.run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()







