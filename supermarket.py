from datetime import datetime

name=input("enter your name:")
#list of items
lists='''
Rice        Rs 20/kg
Sugar       Rs 30/kg
Salt        Rs 20/kg
oil         Rs 80/liter
Paneer      Rs 110/kg
Horlicks    Rs 90/each
Colgate     Rs 85/each 
'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]

# rates of items
items={'rice':20,
'Sugar':30,
'Salt':20,
'oil':80,
'paneer':110,
'Horlicks':90,
'colgate':85}

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or press 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter the items you want :")
        quantity= int(input("Enter quantity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry the item you entered id not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
    if finalamount!=0:
        print(25*"=","RATNADEEP",25*"=")
        print(28*" ","GUNTUR")
        print("Name:",name,30*" ","Date:",datetime.now())
        print(75*"-")
        print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
        for i in range(len(pricelist)):
            print(1,8*' ',5*' ',ilist[i],10*' ',qlist[i],10*" ",plist[i])
            print(75*"-")
            print(50*" ",'Totalamount:','Rs',totalprice)
            print("gst amount",40*" ",'Gst Rs',gst)
            print(75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting")
            print(75*"-")







