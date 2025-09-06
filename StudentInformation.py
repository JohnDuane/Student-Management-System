while True:
    op1 = input('Student Management System\n' \
                '[1] Add Student\n' \
                '[2] Show All Students\n' \
                '[3] Update Student\n' \
                '[4] Remove Student\n' \
                '[5] Exit\n' \
                'Choose an option: ')

    if op1 == '1':
        in1 = input('Enter Student\'s name: ')
        in2 = input('Enter Student\'s Age: ')
        in3 = input('Enter Student\'s ID Code: ')
        in4 = input('Enter Student\'s Grade: ')

        with open('students.txt', 'a') as f:
            f.write(in1 + ' ' + in2 + ' ' + in3 + ' ' + in4 + '\n')

    elif op1 == '2':
        try:
            with open('students.txt', 'r') as read:
                print('---- Database ----\n')
                print(read.read())
                print('------------------')
        except FileNotFoundError:
            print("No data found. The database is empty.")

    elif op1 == '3':

        student_id = input('Enter the Student ID Code to update: ')

        try:
            with open('students.txt', 'r') as file:
                lines = file.readlines()

            found = False
            for i, line in enumerate(lines):
                parts = line.strip().split(' ')
                if len(parts) < 4:
                    continue  
                name, age, id_code, grade = parts
                if id_code == student_id:
                    print(f"Current data: Name: {name}, Age: {age}, ID: {id_code}, Grade: {grade}")
                    new_name = input('Enter new name (leave blank to keep current): ')
                    new_age = input('Enter new age (leave blank to keep current): ')
                    new_grade = input('Enter new grade (leave blank to keep current): ')

                    new_name = new_name if new_name else name
                    new_age = new_age if new_age else age
                    new_grade = new_grade if new_grade else grade

                    lines[i] = f"{new_name} {new_age} {id_code} {new_grade}\n"
                    found = True
                    break

            if not found:
                print("Student ID not found.")
            else:
                with open('students.txt', 'w') as file:
                    file.writelines(lines)
                print("Student record updated successfully.")

        except FileNotFoundError:
            print("No data found. The database is empty.")

    elif op1 == '4':
        student_id = input('Enter the Student ID Code to remove: ')

        try:
            with open('students.txt', 'r') as file:
                lines = file.readlines()

            new_lines = []
            found = False
            for line in lines:
                parts = line.strip().split(' ')
                if len(parts) < 4:
                    new_lines.append(line)
                    continue
                id_code = parts[2]
                if id_code == student_id:
                    found = True
                else:
                    new_lines.append(line)

            if not found:
                print("Student ID not found.")
            else:
                with open('students.txt', 'w') as file:
                    file.writelines(new_lines)
                print("Student record removed successfully.")

        except FileNotFoundError:
            print("No data found. The database is empty.")

    elif op1 == '5':
        print("Exiting program.")
        break

    else:
        print("Invalid option. Please try again.")



