def even(l):
    for e in l:
        if e%2==0:
            print("Even Number is in the list")
            break
    else:
        print("Odd Number")

even([3,4,9])