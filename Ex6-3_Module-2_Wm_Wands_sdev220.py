#ex 6.3 ch 6 sdev220 9/20/22
print('ex 6.3')
guess_me = int(5) 
for number in range(0, 11):
#IN THE LOOP
#process the number
    print(number)
    if number < guess_me:
     print('Too Low')
    elif number > guess_me:
        print("OOPS")
        break

    else:
     number == guess_me
     print('Found It')

