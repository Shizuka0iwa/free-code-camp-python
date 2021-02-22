def comuputepay(hours, rate) :
    if hours > 40 :
        pay = 40 * rate + (hours - 40) * rate * 1.5
        return pay
    else :
        pay = hours * rate
        return pay

sh = input('Enter Hours: ')
try :
    fh = float(sh)
except :
    print("Error, please enter numeric input.")
    quit()
sr = input('Enter Rate: ')
try :
    fr = float(sr)
except :
    print("Error, please enter numeric input.")
    quit()


#if fh > 40 :
#    pay = 40 * fr + (fh - 40) * fr * 1.5
#else :
#    pay = fh * fr

print("Pay:", comuputepay(fh, fr)) 