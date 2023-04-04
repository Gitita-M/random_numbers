import lcg
m = int(input('Type in your modulus:\t'))
a = int(input('Type in your multplier:\t'))
c = int(input('Type in your increment:\t'))
z_0 = int(input('Type in your seed:\t'))

random_numbers, gen_z = lcg.getrandomnumber(m,a,c,z_0)

print("\n")
print(f'Behold, your random numbers: {random_numbers}' )
print("\n")
print(f'And behold, their gen-zees: {gen_z}' )
