# You are tasked with writing a Python programm to manage a list of clothing items and simulate the washing process. The goal is to iterate though a list of cloths. printout which items are being washed(excluding socks),and keep track pf the paired socks saperately.
l=[]
while(True):
    i = input("q to quit: ")
    if i.lower() == "quit":
        break
    else:
        if i not in l:
            print("Washing",i)
            l.append(i)
        else:
            l.remove(i)
            l.append(i)

print("Washed items:",end=' ')
for i in l:
    print(i,end=' ')