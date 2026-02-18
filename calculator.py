print("This is a simple calculator")
n = 0 
a = input(":")
def lenlef(t):
    leni = 0
    for i in t[::-1]:
        if i not in['*','/','-','+']:
            leni+=1
        else:
            return leni
    return leni
def lenrig(t):
    leni = 0
    for i in t:
        if i not in ['*','/','-','+']:
            leni+=1
        else:
            return leni
    return leni

while n==0:
    if '/' in a or '*' in a:
        if '/' in a: 
            p = a.index('/')
            q = a[0:(p-lenlef(a[:p]))]
            r = float(a[p-lenlef(a[:p]):p])
            s = float(a[p+1:p+lenrig(a[p+1:])+1])
            u = a[p+lenrig(a[p+1:])+1:]
            a = q + str(r/s) + u
            print(a)
        elif '*' in a:
            p = a.index('*')
            q = a[0:(p-lenlef(a[:p]))]
            r = float(a[p-lenlef(a[:p]):p])
            s = float(a[p+1:p+lenrig(a[p+1:])+1])
            u = a[p+lenrig(a[p+1:])+1:]
            a = q + str(r*s) + u
            print(a)
    elif '+' in a or '-' in a:
        if '+' in a:
            p = a.index('+')
            q = a[0:(p-lenlef(a[:p]))]
            r = float(a[p-lenlef(a[:p]):p])
            s = float(a[p+1:p+lenrig(a[p+1:])+1])
            u = a[p+lenrig(a[p+1:])+1:]
            p = a.index('+')
            a = q + str(r+s) + u
            print(a)
        elif '-' in a:
            p = a.index('-')
            q = a[0:(p-lenlef(a[:p]))]
            r = float(a[p-lenlef(a[:p]):p])
            s = float(a[p+1:p+lenrig(a[p+1:])+1])
            u = a[p+lenrig(a[p+1:])+1:]
            p = a.index('-')
            a = q + str(r-s) + u
            print(a)
    else:
        n+=1
        print(a)
    

