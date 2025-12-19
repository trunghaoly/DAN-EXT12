import turtle
L = int(input('Nhap L: '))
Dep = int(input('Nhap Dep: '))
N = int(input('Nhap canh: '))
t = turtle.Turtle()
def a(L,Dep):
    if Dep > 0:
        a(L/3,Dep - 1)
        t.left(60)
        a(L/3,Dep - 1)
        t.right(120)
        a(L/3,Dep - 1)
        t.left(60)
        a(L/3,Dep - 1)
    elif Dep == 0:
        t.forward(L)
for i in range(N):
    a(L,Dep)
    t.left(360/N)
turtle.done()