def cleanFiles(currentMem, exMem):
    with open(currentMem, 'r+') as currFile, open(exMem, 'a+') as oldFile:
        currFile.seek(0)
        lines = currFile.readlines()

        if not lines:
            return

        header = lines[0]
        members = lines[1:]

        active_members = [header]
        inactive_members = []

        for member in members:
            parts = member.strip().split()
            if parts and parts[-1].lower() == 'no':
                inactive_members.append(member)
            else:
                active_members.append(member)

        currFile.seek(0)
        currFile.truncate()
        currFile.writelines(active_members)

        oldFile.writelines(inactive_members)


# === File paths ===
memReg = 'members.txt'     # Current members file
exReg = 'inactive.txt'     # Inactive (ex) members file

# Run the function
cleanFiles(memReg, exReg)

# Print the updated files
print("Active Members: \n")
with open(memReg, 'r') as readFile:
    print(readFile.read())

print("Inactive Members: \n")
with open(exReg, 'r') as readFile:
    print(readFile.read())
