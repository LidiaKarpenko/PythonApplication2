#ülesanne 0. 
#s = 0
#for i in range(1,101): 
#    s+=i 
#    print(s) 
#i = 0
##
#s = 0
#while i<= 100: 
#    s+=1 
#    i+=1 
#    print(s)
#ülesanne 2. 
#print("sisestage 10 arvu")
#print()
#q = int (input())
#w = int (input())
#e = int (input())
#r = int (input())
#t = int (input())
#y = int (input())
#u = int (input())
#i = int (input())
#o = int (input())
#p = int (input())
#variable = [q, w, e, r, t, y, u, i, o, p]
#for x in variable:
#    while x == " ":
#        break
#    else: 
#        print(q + w + e + r + t + y + u + i + o + p);
#        break

#print("sisestage 10 arvu")
#print()
#sum = 0
#for x in range(10):
#    numln = input()
#    if(numln== ""):
#        break
#    num = int(numln)
#    sum += num
#print(sum)














#ülesanne 16.
#ans = random.randint(1,10)
#while True:
    #g = input("mis numbri ma arvasin? (1-10, mängu lõpetamiseks kirjutage *lõpp*) \n")
    #if g.lower() == "lõpp":
        #print("mäng on läbi!")
        #break
    #if not g.isnumeric():
        #print("vale andmetüpp!")
        #continue
    #g = int(g)
    #if g == ans:
        #print("vahemil on vale!")
        #continue
   #elif g !=ans:
        #print(f"vale! proovi veel korra!")
        #continue

#ülesanne 3.
#g = 1
#try:
#    f = int(input("mitu algarvu sa tahad?"))
#    for d in range (0,f,1):
#        print("täienduskoolitus")
#        a = randint(1,50)
#        b = randint(1,50)
#        c = a + b
#        for i in range(0,5,1):
#            answer = int(input(f"{a}={b}=? "))
#        if answer == a+b:
#            print("see on õige")
#            break
#        else:
#            print("proovi veel kord")
#            print()
#    g = g+1
#    print("see ei ole õige")
#except:

#ülesanne 13.
#print("arv", "ruut", "kuup")
#for i in range(1,11):
#    print(f"{i}  {i ** 2}   {i ** 3}   ")
#print("teine variant")
#print("arv", "ruut", "kuup") 
#while i < 11:
#    print(f"{i}  {i ** 2}   {i ** 3}   ")
#    i += 1

#
#import string
#import random

#print("arva taht - (Aa kuni Zz)")
#letter = random.choise(string.ascii_letters)

#while True:
#    answ = str(input("teie oletus: "))
#    if letter == answ:
#        print("tubli!")
#        break
#else: print("proovi uuesti!")

#while True:
#    print("tahan kommi!")
#    a = str(input())
#    if a.lower() == "komm":
#        print("Aitäh! Oli vaja")
 
#print()
#print("ülesanne 6 1")
#print()
#for i in range(0,5):
#    print("* "*1)
#print()
#for i in range(0,10):
#    print("* "*(10-i))
#print()

#while True:
#    try:
#        mainnumber = int(input("vali number 1-100:"))
#        break
#    except ValueError:
#        print("see pole täisarv")
#if mainnumber<1 or mainnumber>100:
#    print("vali õige number")
#else:
#    paaris = 0
#    paaritu = 0
#    x = 0
#    while x != mainnumber:
#        x = x + 1
#        print(int(x), end=" ")
#        if x % 2 == 0:
#            paaris += 1
#        else:
#            paaritu +=1
#print("paaris numbrid:", paaris)
#print("paaritu numbrid:", paaritu)

#import time
#a = 1000

#while a > 7:
#    time.sleep(0.05)
#    a -= 7
#    print(f'{a+7} - 7 = {a}')
#print('1000-7')