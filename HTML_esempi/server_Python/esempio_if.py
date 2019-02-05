# esempio uso del blocco if

età=eval(input("Quanti anni ha il tuo cane? "))

if età < 1 :
    print("non ci credo!")
elif età == 1 :
    print("allora corrisponde a 14 anni")
elif età == 2:
    print("allora corrisponde a 22 anni")
else:
    print("allora corrisponde a ", (età-2)*5+22, " anni")
