import secrets
from tropical_key_exchange import generate_m_h
from tropical_key_exchange import generate_exponent
from tropical_key_exchange import compute_intermediaries, generate_exponent
from tropical_algebra import multiply
from tropical_algebra import add
from tropical_algebra import adj_multiply
from tropical_algebra import semigroup_op_1
from tropical_algebra import semigroup_op_2

def sub(x,y):
    return [[a - b for a, b in zip(x_rows, y_rows)] for x_rows, y_rows in zip(x, y)]

m,h = generate_m_h(2)
print("m="+str(m),"h="+str(h))

c = list(range(1000))
d = list(range(1000))
c[0] = m
d[0] = h
for i in range(1,1000): 
    c[i],d[i] = semigroup_op_1(c[i-1],d[i-1],m,h)

xx = generate_exponent(5)
yy = generate_exponent(5)
A = c[xx]
B = c[yy]
print(xx,yy)

print("A="+str(A),"B="+str(B))

KeyA = add(add(add(A,B),d[xx]),multiply(B,d[xx]))
KeyB = add(add(add(A,B),d[yy]),multiply(A,d[yy]))
print()
print("ALICE KEY=",KeyA)
print()
print("BOB KEY=",KeyB)
Diff1 = sub(KeyA,multiply(A,B))
print()
print("Difference="+str(Diff1))
print()

KeyA = list(range(100))
Dif = list(range(100))
for i in range(20,50):
    KeyA = add(add(add(c[i],B),d[i]),multiply(B,d[i]))
    Dif[i] = sub(KeyA,multiply(c[i],B))
    print(Dif[i])
    
for i in range(10,30):
    for j in range(10,30):
        while Dif[i] == Dif[j]:
            print("ATTACK_SUCCESSSS")
            print(i,j)
            break
