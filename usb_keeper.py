import os
import shutil

def main():
    # Get the path of the USB drive
    usb_path = os.path.abspath(os.path.join(os.sep, 'media', os.getlogin()))

    # Get the current script's path
    script_path = os.path.dirname(os.path.abspath(__file__))

    try:
        # Iterate through the files in the current folder
        for filename in os.listdir(script_path):
            file_path = os.path.join(script_path, filename)

            if os.path.isdir(file_path) and filename == 'Pictures':
                # Create a new folder to store the recovered files
                recovery_folder = os.path.join(usb_path, 'recovery_data')
                os.makedirs(recovery_folder, exist_ok=True)

                # Copy the 'Pictures' folder to the recovery folder
                shutil.copytree(file_path, os.path.join(recovery_folder, filename))
                
        print('Data recovery has been successfully completed.')
    except Exception as e:
        print(f'An error has occurred: {e}')

if __name__ == "__main__":
    main()