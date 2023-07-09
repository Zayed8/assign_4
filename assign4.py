username = str(input("Enter UserName : "))
print(f"WELCOME MY {username} ")


def fbreak(x):  #FOR LOOP WITH BREAK cmd
    print("For Loop with using BREAK -->")
    for i in x:
     if(i==b):
       break
     else:
       print(i)

def fpass(x):  #FOR LOOP WITH PASS cmd
    print("For Loop with using PASS -->")
    for i in x:
     if(i==b):
       pass
     else:
       print(i)

def fcontinue(x):  #FOR LOOP WITH CONTINUE cmd
    print("For Loop with using CONTINUE -->")
    for i in x:
     if(i==b):
       continue
     else:
       print(i)

def wbreak(a):  #WHILE LOOP WITH BREAK cmd
    print("While Loop with using BREAK -->")
    while a<=5:
     if a==3:
        break
     else:
        print(a)
    a+=1

def wpass(a):  #WHILE LOOP WITH PASS cmd
    print("While Loop with using PASS -->")
    while a<=5:
      if a==3:
        pass
      else:
         print(a)
         a+=1

def wcontinue(a):  #WHILE LOOP WITH CONTINUE cmd
    print("While Loop with using CONTINUE -->")
    while a<=5:
       if a==3:
           a+=1
           continue
       else:
           print(a)
       a+=1

def felsebreak(x):  #FOR LOOP WITH ELSE AND BREAK cmd
    print("FOR Loop with Else using BREAK -->")
    for i in x:
       if(i==b):
          break
       else:
        print(i)
        print(chr(1))
    else:
      print("it has Else block")

def felsepass(x):  #FOR LOOP WITH ELSE AND PASS cmd
    print("FOR Loop with Else using PASS -->")
    for i in x:
        if(i==b):
           pass
        else:
           print(i)
           print(chr(1))
    else:
        print("it has Else block")

def felsecontinue(x):  #FOR LOOP WITH ELSE AND CONTINUE cmd
    print("FOR Loop with Else using CONTINUE -->")
    for i in x:
        if(i==b):
           continue
        else:
           print(i)
           print(chr(1))
    else:
       print("it has Else block")

def welsebreak(a):  #FOR LOOP WITH ELSE AND BREAK cmd
    print("FOR Loop with Else using BREAK -->")
    while a<=5:
        if a==3:
            break
        else:
            print(a)
        a+=1
    else:
        print("👻")

def welsepass(a):  #FOR LOOP WITH ELSE AND PASS cmd
    print("FOR Loop with Else using PASS -->")
    while a<=5:
        if a==3:
           a+=1
           pass
        else:
           print(a)
        a+=1
    else:
        print("👻")

def welsecontinue(a):  #FOR LOOP WITH ELSE AND CONTINUE cmd
    print("FOR Loop with Else using CONTINUE -->")
    while a<=5:
        if a==3:
           a+=1
           continue
        else:
            print(a)
        a+=1
    else:
       print("👻")

print(" ENTER 1 TO SEE FOR LOOP WITH BREAK....! \n ENTER 2 TO SEE FOR LOOP WITH pass....! \n ENTER 3 TO SEE FOR LOOP WITH CONTINUE....! \n ENTER 4 TO SEE WHILE LOOP WITH BREAK....! \n ENTER 5 TO SEE WHILE LOOP WITH PASS....! \n ENTER 6 TO SEE WHILE LOOP WITH CONTINUE....! \n ENTER 7 TO SEE FOR ELSE LOOP WITH BREAK....! \n ENTER 8 TO SEE FOR ELSE LOOP WITH PASS....! \n ENTER 9 TO SEE FOR ELSE LOOP WITH CONTINUE....! \n ENTER 10 TO SEE WHILE ELSE LOOP WITH BREAK....! \n ENTER 11 TO SEE WHILE ELSE LOOP WITH PASS....! \n ENTER 12 TO SEE WHILE ELSE LOOP WITH CONTINUE....!")

op = int(input("ENTER THE OPERATION NO. TO BE PERFORMED: "))
x = str(input("Enter the String to be passed: "))
b = str(input("Enter the character to break the string: "))
a = int(input("Enter the number to be passed: "))

if op == 1:
   fbreak(x)
elif op == 2:
   fpass(x)
elif op == 3:
   fcontinue(x)
elif op == 4:
   wbreak(a)
elif op == 5:
   wpass(a)
elif op == 6:
   wcontinue(a)
elif op == 7:
   felsebreak(x)
elif op == 8:
   felsepass(x)
elif op == 9:
   felsecontinue(x)
elif op == 10:
   welsebreak(a)
elif op == 11:
   welsepass(a)
elif op == 12:
   welsecontinue(a)      

    