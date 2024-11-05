
import mysql.connector as msql


mydb = msql.connect(host='localhost',user='root', passwd='00989iiopo',database='hackathon')
if mydb.is_connected():
    print("mysql connected")

pointer = mydb.cursor()



print("____________________ SPENDY____________________\n")
print("     TRACKS ALL YOUR EXPENSES IN ONE PLACE             \n\n")

amount1=0

spend2={}

def amount():
    global kc
    global spend
    kc=int(input("\nPlease Enter The Amount: "))
    return kc
    
    

def spend():

    global spend
    spend1={}
  
    while True:

        spent=input("\n\nEnter The Amount Spent OR Enter 0 To Exit : ")

        if spent=="0":
            break

        For=input("Spent for: ")  # For is a variable here :)

        spend1.update({int(spent):For})
    return spend1
    


def show():

    global spend2

    for ch in spend2:

        print(spend2[ch],"------>",ch)
    

while True:

    print("\n---------HOME---------\n1.Add amount\n2.Expense\n3.History\n4.Exit\n-------------------")
    inp=int(input("\n\nEnter your choice!!: "))

    if inp==1:

        x=amount()
        amount1+=x
        print(x,"Added !!!\n__Balance__: ",amount1,)


        
    elif inp==2:

        x=spend()
        spend2.update(x)

        balance=amount1

        for keys in spend2:
            balance-=keys

        print("\n__Balance__:",balance)

        amount1=balance


    
    elif inp==3:
        show()

    elif inp==4:
        break

    else :
        print("\n*******Invalid Enter Again*******\n")

    