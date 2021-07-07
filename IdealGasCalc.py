# ideal gas law - working out the unknown

def main(): # container

    r = 0.0821 # this is the constant for ideal gas

    x = str(input("What is unknown? (P,V,n,T) ")) # determining what's missing

    if x in 'Pp': # If x has either capital P or lowercase p then run the following

        v = float(input("Enter the volume of the gas: ")) # float value needed for going into decimal places
        t = float(input("Enter the temperature of the gas: "))
        n = float(input("Enter the moles of gas: "))
        p = float((n*r*t)/v)
        print("The value for pressure is "+str(p) + " atm") # concatonated string

        restart=input("Press 1 to return to the main menu or any other key to exit ") # asking to rerun the program
        if restart == "1":
            main() # calling upon main container to be rerun
        else: exit() # if the user selects any other key then the program is killed off

    elif x in 'Vv': # If x has either capital V or lowercase V then run the following

        p = float(input("Enter the pressure of the gas : "))
        t = float(input("Enter the temperature of the gas: "))
        n = float(input("Enter the moles of gas: "))
        v = float(n*r*t)/p
        print("The volume is " + str(p) + " litres")

        restart = input("Press 1 to return to the main menu or any other key to exit ") # asking to rerun the program
        if restart == "1":
            main()
        else:
            exit()

    elif x in 'Nn': # If x has either capital N or lowercase n then run the following

        p = float(input("Enter the pressure of the gas : "))
        v = float(input("Enter the volume of the gas: "))
        t = float(input("Enter the temperature of the gas "))
        n = float(p*v)/(r*t)
        print("There are " + str(n) + " moles of gas")

        restart = input("Press 1 to return to the main menu or any other key to exit ") # asking to rerun the program
        if restart == "1":
            main()
        else:
            exit()

    elif x in 'Tt': # If x has either capital T or lowercase t then run the following

        p = float(input("Enter the pressure of the gas : "))
        v = float(input("Enter the volume of the gas: "))
        n = float(input("Enter the moles of gas:  "))
        t = (p*v)/(r*n)
        print("The temperate of the gas is " + str(t))

        restart = input("Press 1 to return to the main menu or any other key to exit ") # asking to rerun the program
        if restart == "1":
            main()
        else:
            exit()

main() # end of container

























