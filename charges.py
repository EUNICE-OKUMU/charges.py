# bill calculator
def kplc(customer_ID, customer_Name,units):
    if units<=199:
        charge= 1.2*units
    elif units>=200 and units<=400:
        charge= 1.5*units
    elif units>=400 and units<=600:
        charge= 1.8*units
    elif units>=600:
        charge= 2.0*units
    return charge
customer_ID= int(input("Enter your ID:"))
customer_Name= input("Enter your Name:")
units_Consumed= int(input("Enter your units:"))
print(kplc(customer_ID, customer_Name,units_Consumed))





























