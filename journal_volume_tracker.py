import os

# Define the main folder and the subfolder naming pattern
main_folder = 'Volume 1'
subfolder_pattern = 'Volume 1 Issue{}'

# Create the main folder if it doesn't already exist
if not os.path.exists(main_folder):
    os.makedirs(main_folder)

# Create subfolders named Volume1Issue1 to Volume1Issue12
for i in range(1, 13):
    subfolder_name = subfolder_pattern.format(i)
    subfolder_path = os.path.join(main_folder, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

print(f"Folder structure under '{main_folder}' created successfully.")
