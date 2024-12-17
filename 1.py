# Nasriddinov Ozodbek
# Vazifa - 5: Berilgan sonning barcha raqamlarini aniqlang va ularning yigib‚ yindisini hisoblang. Masalan, 456, 4 + 5 + 6 = 15.


n = int(input("N sonini kiriting: "))
c = 0
c2 = 0
while n > 0:
    
    c = n % 10  
    c2 += c     
    n //= 10 
print("Yigindi:", c2)
