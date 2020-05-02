EUR = 1
USD = 1.13798
RUP = 74.94781

def currencyConverter():
    chosenCurrency=input("Do you wish to convert your euros into \n1)USD \n2)RUP\n\n")
    print(("_"*36)+"\n")
    print(chosenCurrency, "\n\n" + ("_"*36))

    if(chosenCurrency)=="1":
        eurAmount = round(float(input("How many euros do you wish to convert into USD?\n\n")))
        print(("_"*36)+ "\n")
        print(eurAmount, "euros is", round((eurAmount)*1.13798, 2),"US dollers.\n\n"+("_"*36))


    elif(chosenCurrency)=="2":
        eurAmount = round(float(input("How many euros do you wish to convert into RUP?\n\n")))
        print(("_"*36)+ "\n")
        print(eurAmount, "euros is", round((eurAmount)*74.9478, 2),"IND rup.\n\n"+("_"*36))

    else:
        print("error!!!!!!!!!")


currencyConverter()


    
