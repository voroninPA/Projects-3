a1=int(input("Первое число:"))
a2=int(input("Второе число:"))
def nod(a1,a2):
    k=1
    maxx=max(a1,a2)
    for i in range(2,maxx):
        if a1%i==0 and a2%i==0:
            a1=a1//i
            a2=a2//i
            k=k*i
    return k
print(nod(a1,a2))
