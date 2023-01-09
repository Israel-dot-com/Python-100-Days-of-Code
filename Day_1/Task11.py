def num_of_char():
    num = input(str('Enter your name: '))
    j = 0
    for i in num:
        if i == ' ':
            continue
        else:
            j +=1
    print(j)


num_of_char()