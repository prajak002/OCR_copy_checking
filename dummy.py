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

        # Truncate and rewrite currentMem with only active members
        currFile.seek(0)
        currFile.truncate()
        currFile.writelines(active_members)

        # Ensure the header is written once to exMem
        oldFile.seek(0)
        existing_lines = oldFile.readlines()
        oldFile.seek(0)
        oldFile.truncate()

        if existing_lines:
            if existing_lines[0].strip() != header.strip():
                oldFile.write(header)
            else:
                oldFile.write(existing_lines[0])
            oldFile.writelines(existing_lines[1:])
        else:
            oldFile.write(header)

        oldFile.writelines(inactive_members)
