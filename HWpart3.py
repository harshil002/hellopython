count = int(input("Enter character limt: "))
A = input("Enter Tweet: ")
if len(A)>count:
    print("Characters Limit Exceeded:", len(A))
    print("Trim the tweet characters by:",len(A)-count)
else:
    print("It fits the limit", len(A))
    print("Number of characters can be added:",count-len(A))
