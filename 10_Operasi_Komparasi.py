# Operasi Komparasi

# setiap hasil dari operasi komparasi adalah bolean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 3
c = 2

# lebih besar dari (>)
print("============ lebih besar dari (>)")
hasil = a > b
print(a , ">",b,"=",hasil)
hasil = c > b
print(c , ">",b,"=",hasil)
hasil = c > c
print(c , ">",c,"=",hasil)

# lebih kecil dari (<)
print("============ lebih kecil dari (<)")
hasil = a < b
print(a , "<",b,"=",hasil)
hasil = c < b
print(c , "<",b,"=",hasil)
hasil = c < c
print(c , "<",c,"=",hasil)

# lebih besar sama dengan (>=)
print("============ lebih besar sama dengan (>=)")
hasil = a >= b
print(a , ">=",b,"=",hasil)
hasil = c >= b
print(c , ">=",b,"=",hasil)
hasil = c >= c
print(c , ">=",c,"=",hasil)

# lebih kecil sama dengan (<=)
print("============ lebih kecil sama dengan (<=)")
hasil = a <= b
print(a , "<=",b,"=",hasil)
hasil = c <= b
print(c , "<=",b,"=",hasil)
hasil = c <= c
print(c , "<=",c,"=",hasil)

# sama dengan (==)
print("============ sama dengan (==)")
hasil = a == a
print(a , "==",a,"=",hasil)
hasil = c == a
print(c , "==",a,"=",hasil)

# tidak sama dengan (!=)
print("============ tidak sama dengan (!=)")
hasil = a != a
print(a , "!=",a,"=",hasil)
hasil = c != a
print(c , "!=",a,"=",hasil)

# 'is' sebagai komparasi object identity
print("============ object identity (is)")
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai x =',x,',id = ',hex(id(y)))

hasil = x is not y
print('x is y =',hasil)

x = 5 #ini adalah assignment membuat object
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai x =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =', hasil)

