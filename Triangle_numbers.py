def all_triangle_numbers(n):
    Query = int(input("What multiple are you searching for? "))
    for i in range(1, n + 1):
        triangle = (i ** 2 + i)//2
        if triangle % Query == 0:
            print(triangle)
        

all_triangle_numbers(50)    