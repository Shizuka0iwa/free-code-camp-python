sh = input('Enter Hours: ')
sr = input('Enter Rate: ')

# convert str to float
fh = float(sh)
fr = float(sr)

if fh > 40 :
    pay = 40 * fr + (fh - 40) * fr * 1.5
else :
    pay = fh * fr

print("Pay:", pay)