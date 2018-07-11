def sleep_or_not(A,B,C):
    if C == A or C == B:
        print("Sleep in")

    else:
        print("Go to work")


A = "Saturday"
B = "Sunday"
C = input("Enter your day: ")
print(sleep_or_not(A,B,C))
