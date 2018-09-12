def all_triangle_numbers(n):
    Query = int(input("What multiple are you searching for? "))
    for i in range(1, n + 1):
        triangle = (i ** 2 + i)//2   
        print("n = {0}, triangle = {1}".format(i, triangle))
        if triangle % Query == 0:
            print("This number is a multiple of {}! Woohoo!".format(Query))
        else:
            print("No, this number is not a multiple of {}.".format(Query))
        

all_triangle_numbers(50)    