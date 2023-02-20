costat=int(input("Dis-me el costat d'un rectangle."))
if costat < 10 or costat > 30:
    costat=int(input("El costat a de estar entre 10 i 30."))
costat2 = 100-2*costat
area = costat*costat2
print (area)
print (costat)
print (costat2)