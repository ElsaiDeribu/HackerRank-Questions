def gradingStudents(grades):
    arr = []
    for i in grades:
        n = ((int((i/5)+1))*5)
        if i < 38:
            arr.append(i)
        elif (n - i) < 3:
            arr.append(n)
        else:
            arr.append(i)
    return arr
