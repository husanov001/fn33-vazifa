son = int(input("son kiriting: "))

son = abs(son)

raqamlar = [int(raqam)
for raqam in str(son)]

kichik_raqam = min(raqamlar)

print("Eng kichik raqam:", kichik_raqam)