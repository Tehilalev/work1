def find_eps(num):
    epsilon = 0
    run = True
    while run:
        epsilon = num
        num /= 2
        if num == 0:
            run = False
    return epsilon


print("The Machine precision is: ", find_eps(3))
