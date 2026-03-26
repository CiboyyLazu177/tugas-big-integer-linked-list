from big_integer import BigInteger

a = BigInteger("1234")
b = BigInteger("567")

print("Angka A:", a.print_number())
print("Angka B:", b.print_number())

print("Tambah:", a.add(b).print_number())
print("Kurang:", a.subtract(b).print_number())
print("Kali:", a.multiply(b).print_number())
print("Bagi:", a.divide(b).print_number())
print("Modulo:", a.modulo(b).print_number())
