import os

def update_members():
    # Define full paths to your files
    current_file ='C:\Users\User\Desktop\savedfiles\currentfile.txt'
    ex_file = 'C:\Users\User\Desktop\savedfiles\exMem.txt'

    # Read all lines from current members file
    with open(current_file, 'r') as file:
        lines = file.readlines()

    # Separate header
    header = lines[0]
    active_members = [header]
    removed_members = []

    # Process each member line
    for line in lines[1:]:
        parts = line.strip().split()
        if parts[-1].lower() == 'no':
            removed_members.append(line)
        else:
            active_members.append(line)

    # Overwrite currentMem.txt with only active members
    with open(current_file, 'w') as file:
        file.writelines(active_members)

    # Append removed members to exMem.txt
    with open(ex_file, 'a') as file:
        file.writelines(removed_members)

    print("Update complete: Removed members moved to exMem.txt")

# Run the function
update_members()
