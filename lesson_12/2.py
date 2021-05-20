a=1
if a==1:
    b=2


def go():
    global a
    print(a)


def go1():
    a=6
    def gooo():
        print(a)
    gooo()
    print(a)



go1()
go()
