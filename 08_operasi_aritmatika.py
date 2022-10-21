# operasi aritmatika 

a = 2
b = 3

# operasi tambah (+)
hasil = a + b
print (a,"+",b,"=",hasil)

# operasi pengurangan (-)
hasil = a - b
print (a,"-",b,"=",hasil)

# operasi perkalian (*)
hasil = a * b
print (a,"x",b,"=",hasil)

# operasi pembagian (/)
hasil = a / b
print (a,"/",b,"=",hasil)

# operasi eksponen/pangkat (**)
hasil = a ** b
print (a,"**",b,"=",hasil)

# operasi modulus/sisa (%)
hasil = a % b
print (a,"%",b,"=",hasil)

# operasi floor division/pembulatan (//)
hasil = a // b
print (a,"//",b,"=",hasil)

#prioritas operasi, operational precedence
'''
urutan 
1. ()
2. exponen **
3. perkalian dan teman-temanya * / ** % //
4. pertambahan dan pengurangan + -
'''

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x, "**" ,y, "*" ,"(",z ,"+" ,x,")", "/" ,y, "-" ,y, "%" ,z, "//" ,x, "=", hasil)

hasil = x+y*z
print(x,"+",y,"*",z,hasil)

#kurung akan mengambil langkah paling pertama
hasil = (x+y)*z
print ("(",x,"+",y,")""*",z,"=",hasil)

print("check")
