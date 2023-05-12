Data Recovery Script
This script is for educational purposes only. It allows you to recover a folder named "Pictures" from the current directory and copy it to a USB drive. It uses the Python os and shutil modules to accomplish this.

Warning
It is important to note that data recovery can be a delicate process, and it is always recommended to seek the help of a professional data recovery service to avoid permanent data loss. This script should be used with caution, as it may overwrite existing data on the USB drive or cause unintended data loss.

How to Use
Save the script to a directory on your computer.
Connect the USB drive to your computer.
Open a terminal or command prompt and navigate to the directory where the script is saved.
Run the script using the command python data_recovery.py.
The script will search for a folder named "Pictures" in the current directory and copy it to a new folder named "recovery_data" on the USB drive.
Requirements
Python 3
The os and shutil modules (included in Python standard library)
Notes
The script uses relative paths to ensure it can be executed from a USB drive.
If the script encounters an error, it will print an error message and exit.
