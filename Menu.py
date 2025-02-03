def menu_Admin():
    print('''Admin Menu
    1. Get number of questions available
    2. Add Question
    3. Get students performance report
    4. Delete a question
    5. Exit...''')
    ch=int(input('Enter your choice : '))
    print('')
    return ch

def menu_Student():
    print('''Student Menu
    1. Give Examination
    2. Get your performance report
    3. Exit...''')
    ch=int(input('Enter your choice : '))
    print('')
    return ch

def menu_Subject():
    status = True
    while status:
        print('''Select Subject
        1. Physics
        2. Maths
        3. Chemistry''')
        ch1 = int(input('Enter you\'r choice : '))
        if ch1 == 1:
            return "Physics"
        elif ch1 == 2:
            return "Maths"
        elif ch1 == 3:
            return "Chemistry"

        else:
            print("Enter valid subject")