import os

def update_members():
    current_file = r'C:\Users\User\Desktop\savedfiles\currentMem.txt'
    ex_file = r'C:\Users\User\Desktop\savedfiles\exMem.txt'

    if not os.path.exists(current_file):
        print(f"❌ File not found: {current_file}")
        return

    with open(current_file, 'r') as file:
        lines = file.readlines()

    if not lines:
        print("⚠️ currentMem.txt is empty.")
        return

    header = lines[0]
    active_members = [header]
    removed_members = []

    for line in lines[1:]:
        parts = line.strip().split()
        if parts and parts[-1].lower() == 'no':
            removed_members.append(line)
        else:
            active_members.append(line)

    with open(current_file, 'w') as file:
        file.writelines(active_members)

    with open(ex_file, 'a') as file:
        file.writelines(removed_members)

    print("✅ Update complete: Removed members moved to exMem.txt")

update_members()
