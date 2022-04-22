import random

verification_code = ''

for i in range(6):
    x = chr(random.randint(65, 90))
    y = chr(random.randint(65, 90)).lower()
    z = random.randint(0, 9)
    code = random.choice([x, y, z])
    verification_code += str(code)

print(verification_code)
