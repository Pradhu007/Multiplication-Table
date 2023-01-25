import time

i = 1
j = 1

print("Welcome to Time table program by Pradhyumna MADHUSUDAN")
time.sleep(3)
numberinput = input("What time tables do you want to calculate ")
print("How many numbers do you want to go for the timetable to go up to {}".format(numberinput))
howmanytimesperinnerloop = input(">")
print("Ok initialising time table ")
time.sleep(2)




if numberinput.isnumeric() == False:
    print("Input field invalid!")
    exit()

if howmanytimesperinnerloop.isnumeric() == False:
    print("Input field invalid!")
    exit()




while i < int(numberinput) + 1 :
    j = 1





    while j < int(howmanytimesperinnerloop) + 1 :
        c = (i * j)
        print("{:2d} ".format(c),end=' ')
        j = j + 1



    print('\n')
    i = i +1

print("This is the in depth analysis for the outer and the inner loop")
for a in range(1,int(numberinput)+1):
    print(a,'table row')
    for b in range(1,int(howmanytimesperinnerloop)+1):
        c=a*b
        print("{}x{} = ".format(a,b),c)
    print()
