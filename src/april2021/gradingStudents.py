def gradingStudents(grades):
    # Write your code here
    # create list to hold return value
    ans = []
    #  loop thru grades
    for num in grades:
        # append num if less than 41:
        if num < 41:      
            ans.append(num)
        print(num / 5)