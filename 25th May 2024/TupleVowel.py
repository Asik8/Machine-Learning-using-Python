t = ("Asik","Maruf","Mehedi")

for i in t:
    for ch in i:
        if ch.lower() not in ['a','e','i','o','u']:
            print(ch,end='') 
    print()