#3. n butun soni va  a haqiqiy soni berilgan 
# (n > 0). a ni#ng n - darajasini aniqlovchi 
# dastur tuzilsin. a^n=a*a*a...a;

a=float(input("Haqiqiy son kiriting: "))
n=int(input("Sonnig darajasini kiritng: "))
s=1
for i in range (n):
    s*=a
print("A = ",s)
