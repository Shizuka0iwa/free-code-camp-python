sum = 0
count = 0
while True :
    num = input('Input a number: ')
    if num == 'done' :
        break
    try :
        fnum = float(num)
    except :
        print('Invarid input. Please input a number or a word \'done\'.')
        continue

    sum = sum + fnum
    count = count + 1
print('Total:', sum)
print('Count:', count)
print('Average:', sum / count)