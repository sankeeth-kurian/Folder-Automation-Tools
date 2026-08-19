import os

# Function to create folders and subfolders based on user input
def create_folders():
    # Ask for the number of main folders
    num_folders = int(input("Enter the number of main folders to create: "))

    # Loop through each folder
    for i in range(num_folders):
        main_folder_name = input(f"Enter the name for main folder {i + 1}: ")

        # Create the main folder if it doesn't exist
        if not os.path.exists(main_folder_name):
            os.makedirs(main_folder_name)
            print(f"Main folder '{main_folder_name}' created successfully.")

        # Ask for the number of subfolders to create under the main folder
        num_subfolders = int(input(f"Enter the number of subfolders to create inside '{main_folder_name}': "))
        
        # Loop to create subfolders
        for j in range(num_subfolders):
            subfolder_name = input(f"Enter the name for subfolder {j + 1} under '{main_folder_name}': ")
            subfolder_path = os.path.join(main_folder_name, subfolder_name)

            # Create the subfolder if it doesn't exist
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
                print(f"Subfolder '{subfolder_name}' created inside '{main_folder_name}'.")

    print("Folder structure created successfully.")

# Call the function to start the process
create_folders()
