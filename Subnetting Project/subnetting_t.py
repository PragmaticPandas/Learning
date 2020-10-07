#create a binary-centered version of my subnetting program

cidr = 19
counter = 0
binary = []

remainder = cidr%8
new_cidr = cidr - remainder

print(remainder)
print(new_cidr)

new_cidr = int(new_cidr / 8)

for i in range(new_cidr):
    binary.append(11111111)
    
print(binary)

#bin(30)[2:].zfill(8)
print('{0:08b}'.format(3))