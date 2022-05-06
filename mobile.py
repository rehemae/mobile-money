from ast import If


print("\t\t\tMOBILE MONEY SYSTEM")
print("\t\t\t-------------------")
phonenumber="0757487892"
Amount=20000

#user.... send money/ withdraw money
print("1. send money")
print("2. withdraw money")
# User choice...
Choice=input("Enter choice:\n")
if(Choice=="1"):
    print("send money")
    print("1.MTN user")
    print("2.Vodacom User")
    user= input("select user:\n")
    
    if(user==1):
        print("MTN user")
        number=input("Enter phone number:\n")
        if(number=="phone number"):
            amount=input("Enter amount to send?\n")
            if(float(amount )>float(Amount)):
                print("insufficient fund, rechard and continue sending")
            else:
                print(float(amount), "semd amount sucessful to number",phonenumber)    

        else:
            print("invald input")
                


    elif(user==2):
        print("Vodacom User")    
elif (Choice=="2"):
    print("withdraw money") 
else:
    print("invalid input") 
         

