import mysql.connector as ms
mydb=ms.connect(host="localhost",user="root",passwd="allwin",database="inventory1")
if mydb.is_connected():
    print("Connected to STATIONARY DATABASE")
cr1=mydb.cursor()

def additem():
    print("")
    ItemId=input("Enter the Item_Id:")
    if len(ItemId)==4:
        Item_Name=input("Enter the NAME of the Item : ")
        Item_Cost=float(input("Enter the UNIT COST of item : "))
        Item_Brand=input("Enter the BRAND of the Item : ")
        Item_Unit=input("Enter the UNIT of item : ")
        cr1.execute("insert into Item(ItemId,Item_Name,Item_Cost,Item_Brand,Item_Unit)values('%s', '%s', %s, '%s', '%s')"%(ItemId,Item_Name,Item_Cost,Item_Brand,Item_Unit))
        mydb.commit()
        print("ADDED")
    else:
        print("Please enter a valid ItemId")
        additem()
        
def viewitem():
    print("")
    ItemId=input("Enter the Item ID to VIEW the DETAILS of the item : ")
    if len(ItemId)==4:
        print("Please Wait")
        cr1.execute("select * from Item where ItemId=('%s')"%(ItemId))
        row=cr1.fetchall()
        print("""THE DETAILS:""")
        for i in row:
            print(i)
    else:
        print("Enter a Valid ITEM Id")
        viewitem()
        
def updateitem():
    print("")
    ItemId=input("Enter the Item id to update the details of the item : ")
    if len(ItemId)==4:
        print("""
                  1.Change ITEM Name.
                  2.Change ITEM Cost.
                  3.Change ITEM Brand.
                  4.Change ITEM Unit.
                  """)
        ch=int(input("Enter your CHOICE"))
        if ch==1:
            Item_Name=input("Enter NEW NAME for the Item : ")
            q1="update Item set Item_Name=('%s') where ItemId=('%s')"%(Item_Name,ItemId)
            cr1.execute(q1)
            mydb.commit()
            print("UPDATED")
        elif ch==2:
            Item_Cost=int(input("Enter NEW COST for the Item : "))
            q2="update Item set Item_Cost=(%s) where ItemId=('%s')"%(Item_Cost,ItemId)
            cr1.execute(q2)
            mydb.commit()
            print("UPDATED")
        elif ch==3:
            Item_Brand=input("Enter NEW BRAND for the Item : ")
            q3="update Item set Item_Brand=('%s') where ItemId=('%s')"%(Item_Brand,ItemId)
            cr1.execute(q3)
            mydb.commit()
            print("UPDATED")
        elif ch==4:
            Item_Unit=input("Enter NEW UNIT for the Item : ")
            q4="update Item set Item_Unit=('%s') where ItemId=('%s')"%(Item_Unit,ItemId)
            cr1.execute(q4)
            mydb.commit()
            print("UPDATED")
        else:
            print("Enter VALID choice")
    else:
        print("Enter a VALID ItemId")
        updateitem()
            
def deleteitem():
    print("")
    ItemId=input("Enter the Item id of the item to be DELETED : ")
    if len(ItemId)==4:
        cr1.execute("delete from Item where ItemId=('%s')"%(ItemId))
        mydb.commit()
        print("DELETED")
    else:
        print("Enter a VALID ItemId")
        deleteitem()



def addsupplier():
    print("")
    SupplierId=input("Enter the Supplier_Id:")
    if len(SupplierId)==4:
        Supplier_Name=input("Enter the NAME of Supplier : ")
        Supplier_Phone=int(input("Enter the PHONE NUMBER of Supplier : "))
        Supplier_Mail=input("Enter EMAIL of Supplier : ")
        Supplier_Fax=int(input("Enter the FAX NUMBER of Supplier : "))
        cr1.execute("insert into Supplier(SupplierId,Supplier_Name,Supplier_Phone,Supplier_Mail,Supplier_Fax)values('%s', '%s', %s, '%s', %s)"%(SupplierId,Supplier_Name,Supplier_Phone,Supplier_Mail,Supplier_Fax))
        mydb.commit()
        print("ADDED")
    else:
        print("Enter a VALID Id")
        addsupplier()
        
def viewsupplier():
    print("")
    SupplierId=input("Enter the Supplier id to VIEW DETAILS of the supplier : ")
    if len(SupplierId)==4:
        print("PLEASE WAIT")
        cr1.execute("select * from Supplier where SupplierId=('%s')"%(SupplierId))
        row=cr1.fetchall()
        print("""THE DETAILS:""")
        for i in row:
            print(i)
    else:
        print("Enter a VALID Id")
        viewsupplier()
        
def updatesupplier():
    print("")
    SupplierId=input("Enter the Supplier id to UPDATE the details of Supplier : ")
    if len(SupplierId)==4:
        print("""
                  1.Change NAME.
                  2.Change PHONE NUMBER.
                  3.Change EMAIL.
                  4.Change FAX NUMBER.
                  """)
        ch=int(input("Enter your CHOICE"))
        if ch==1:
            Supplier_Name=input("Enter NEW NAME for the Supplier : ")
            q1="update Supplier set Supplier_Name=('%s') where SupplierId=('%s')"%(Supplier_Name,SupplierId)
            cr1.execute(q1)
            mydb.commit()
            print("UPDATED")
        elif ch==2:
            Supplier_Phone=int(input("Enter NEW PHONE NUMBER of the supplier : "))
            q2="update Supplier set Supplier_Phone=(%s) where SupplierId=('%s')"%(Supplier_Phone,SupplierId)
            cr1.execute(q2)
            mydb.commit()
            print("UPDATED")
        elif ch==3:
            Supplier_Mail=input("Enter NEW EMAIL of the supplier : ")
            q3="update Supplier set Supplier_Mail=('%s') where SupplierId=('%s')"%(Supplier_Mail,SupplierId)
            cr1.execute(q3)
            mydb.commit()
            print("UPDATED")
        elif ch==4:
            Supplier_Fax=int(input("Enter NEW FAX NUMBER of the supplier : "))
            q4="update Supplier set Supplier_Fax=(%s) where SupplierId=('%s')"%(Supplier_Fax,SupplierId)
            cr1.execute(q4)
            mydb.commit()
            print("UPDATED")
        else:
            print("Enter VALID choice")
    else:
        print("Enter a VALID Id")
        updatesupplier()
        
def deletesupplier():
    print("")
    SupplierId=input("Enter the Supplier id of the Supplier to be DELETED : ")
    if len(SupplierId)==4:
        cr1.execute("delete from Supplier where SupplierId=('%s')"%(SupplierId))
        mydb.commit()
        print("DELETED")
    else:
        print("ENTER A VALID ID")
        deletesupplier()




def addcustomer():
    print("")
    CustomerId=input("Enter the Customer_Id:")
    if len(CustomerId)==4:
        Customer_Name=input("Enter the name of Customer : ")
        Customer_Phone=int(input("Enter the phone no. of Customer : "))
        Customer_Mail=input("Enter email of Customer : ")
        Customer_Fax=int(input("Enter the Fax no. of Customer : "))
        cr1.execute("insert into Customer(CustomerId,Customer_Name,Customer_Phone,Customer_Mail,Customer_Fax)values('%s', '%s', %s, '%s', %s)"%(CustomerId,Customer_Name,Customer_Phone,Customer_Mail,Customer_Fax))
        mydb.commit()
        print("ADDED")
    else:
        print("Enter a VALID Id")
        addcustomer()
        
def viewcustomer():
    print("")
    CustomerId=input("Enter the Customer id to VIEW DETAILS of the Customer : ")
    if len(CustomerId)==4:
        print("PLEASE WAIT")
        cr1.execute("select * from Customer where CustomerId=('%s')"%(CustomerId))
        row=cr1.fetchall()
        print("""THE DETAILS:""")
        for i in row:
            print(i)
    else:
        print("Enter a VALID Id")
        viewcustomer()
        
def updatecustomer():
    print("")
    CustomerId=input("Enter the Customer id to UPDATE the details of Customer : ")
    if len(CustomerId)==4:
        print("""
                  1.Change Name.
                  2.Change Phone Number.
                  3.Change Email.
                  4.Change Fax Number.
                  """)
        ch=int(input("Enter your CHOICE"))
        if ch==1:
            Customer_Name=input("Enter  NEW NAME  for the Customer : ")
            q1="update Customer set Customer_Name=('%s') where CustomerId=('%s')"%(Customer_Name,CustomerId)
            cr1.execute(q1)
            mydb.commit()
            print("UPDATED")
        elif ch==2:
            Customer_Phone=int(input("Enter new phone no. of the Customer : "))
            q2="update Customer set Customer_Phone=(%s) where CustomerId=('%s')"%(Customer_Phone,CustomerId)
            cr1.execute(q2)
            mydb.commit()
            print("UPDATED")
        elif ch==3:
            Customer_Mail=input("Enter new email of the Customer : ")
            q3="update Customer set Customer_Mail=('%s') where CustomerId=('%s')"%(Customer_Mail,CustomerId)
            cr1.execute(q3)
            mydb.commit()
            print("UPDATED")
        elif ch==4:
            Customer_Fax=int(input("Enter NEW FAX NUMBER of the Customer : "))
            q4="update Customer set Customer_Fax=(%s) where CustomerId=('%s')"%(Customer_Fax,CustomerId)
            cr1.execute(q4)
            mydb.commit()
            print("UPDATED")
        else:
            print("Enter VALID choice")
    else:
        print("Enter a valid Id")
        updatecustomer()
        
def deletecustomer():
    print("")
    CustomerId=input("Enter the CUSTOMER ID  of the Customer to be DELETED: ")
    if len(CustomerId)==4:
        cr1.execute("delete from Customer where CustomerId=('%s')"%(CustomerId))
        mydb.commit()
        print("DELETED")
    else:
        print("PLEASE ENTER A VALID ID")
        deletecustomer()



def addsalesman():
    print("")
    SalesmanId=input("Enter the Salesman_Id:")
    if len(SalesmanId)==4:
        Salesman_Name=input("Enter the NAME of the Salesman : ")
        cr1.execute("insert into Salesman(SalesmanId,Salesman_Name)values('%s', '%s')"%(SalesmanId,Salesman_Name))
        mydb.commit()
        print("ADDED")
    else:
        print("Please enter a VALID Id")
        addsalesman()

def viewsalesman():
    print("")
    SalesmanId=input("Enter the Salesmanid to VIEW DETAILS  of the Salesman : ")
    if len(SalesmanId)==4:
        print("Please Wait")
        cr1.execute("select * from Salesman where SalesmanId=('%s')"%(SalesmanId))
        row=cr1.fetchall()
        print("the details:")
        for i in row:
            print(i)
    else:
        print("Enter a Valid Id")
        viewsalesman()

def updatesalesman():
    print("")
    SalesmanId=input("Enter the Salesman id to UPDATE the NAME of Salesman : ")
    if len(SalesmanId)==4:      
            Salesman_Name=input("Enter NEW NAME for the Salesman : ")
            q1="update Salesman set Salesman_Name=('%s') where SalesmanId=('%s')"%(Salesman_Name,SalesmanId)
            cr1.execute(q1)
            mydb.commit()
            print("UPDATED")   
    else:
        print("Enter a VALID Id")
        updatesalesman()

def deletesalesman():
    print("")
    SalesmanId=input("Enter the Salesman id of the Salesman to be DELETED:")
    if len(SalesmanId)==4:
        cr1.execute("delete from Salesman where SalesmanId=('%s')"%(SalesmanId))
        mydb.commit()
        print("DELETED")
    else:
        print("PLEASE ENTER A VALID ID")
        deletesalesman()
        
        


def item():
    print("")
    print("""
              1.ADD AN ITEM
              2.VIEW AN ITEM
              3.UPDATE AN ITEM
              4.DELETE AN ITEM
              5.EXIT OR PREVIOUS MENU""")
    op=int(input("Enter your CHOICE")) 
    
    if op==1:
        print("")
        print("You Chose To ADD an Item")
        additem()
        
    elif op==2:
        print("")
        print("You Chose To VIEW An Item")
        viewitem()
        
    elif op==3:
        print("")
        print("You Chose To UPDATE An Item")
        updateitem()
        
    elif op==4:
        print("")
        print("You Chose To DELETE An Item")
        deleteitem()
    
    elif op==5:
        print("")
        print("You Chose To Go To PREVOIUS MENU")
        mastercreation()
    
    else:
        print("")
        print("Enter a VALID Choice")
        item()



def supplier():
    print("")
    print("""
              1.ADD A SUPPLIER
              2.VIEW A SUPPLIER
              3.UPDATE A SUPPLIER
              4.DELETE A SUPPLIER
              5.EXIT OR PREVIOUS MENU""")
    op=int(input("Enter your choice")) 
    
    if op==1:
        print("")
        print("You Chose To ADD A Supplier")
        addsupplier()
        
    elif op==2:
        print("")
        print("You Chose To VIEW A Supplier")
        viewsupplier()
        
    elif op==3:
        print("")
        print("You Chose To UPDATE  A Supplier")
        updatesupplier()
        
    elif op==4:
        print("")
        print("You Chose To DELETE A Supplier")
        deletesupplier()
    
    elif op==5:
        print("")
        print("You Chose To Go To PREVIOUS MENU")
        mastercreation()
        
    else:
        print("")
        print("PLEASE ENTER A VALID CHOICE")
        supplier()
   


def customer():
    print("")
    print("""
              1.ADD A CUSTOMER
              2.VIEW A CUSTOMER
              3.UPDATE A CUSTOMER
              4.DELETE A CUSTOMER
              5.EXIT OR PREVIOUS MENU """)
    op=int(input("ENTER YOUR CHOICE")) 
    
    if op==1:
        print("")
        print("You Chose To ADD a Customer")
        addcustomer()
        
    elif op==2:
        print("")
        print("You Chose To VIEW A Customer")
        viewcustomer()
        
    elif op==3:
        print("")
        print("You Chose To UPDATE A Customer")
        updatecustomer()
        
    elif op==4:
        print("")
        print("You Chose To DELETE A Customer")
        deletecustomer()
    
    elif op==5:
        print("")
        print("You Chose To Go To PREVIOUS MENU")
        mastercreation()
        
    else:
        print("")
        print("PLEASE ENTER A VALID CHOICE")
        customer()



def salesman():
    print("")
    print("""
              1.ADD A SALESMAN
              2.VIEW A SALESMAN
              3.UPDATE A SALESMAN
              4.DELETE A SALESMAN
              5.EXIT OR PREVIOUS MENU """)
    op=int(input("ENTER YOUR CHOICE")) 
    
    if op==1:
        print("")
        print("You Chose To ADD a Salesman")
        addsalesman()
        
    elif op==2:
        print("")
        print("You Chose To VIEW A Salesman")
        viewsalesman()
        
    elif op==3:
        print("")
        print("You Chose To UPDATE A Salesman")
        updatesalesman()
        
    elif op==4:
        print("")
        print("You Chose To DELETE A Salesman")
        deletesalesman()
    
    elif op==5:
        print("")
        print("You Chose To Go To PREVIOUS MENU")
        mastercreation()
        
    else:
        print("")
        print("PLEASE ENTER A VALID CHOICE")
        salesman()




def mastercreation():
    print("")
    print("************CLOUD STATIONARY*******************")
    print("****************ABU DHABI**********************")
    print("             1. Item_Creation                                      ")
    print("             2. Supplier_Creation                                  ")
    print("             3. Customer_Creation                                    ")
    print("             4. Salesman_Creation                                           ")
    option=int(input("Enter your Choice:"))
    
    if option==1:
        print("")
        print("You Chose Item_Creation")
        item()
        
    elif option==2:
        print("")
        print("You Chose Supplier_Creation")
        supplier()
    
    elif option==3:
        print("")
        print("You Chose Customer_Creation")
        customer()

    elif option==4:
        print("")
        print("You Chose Salesman_Creation")
        salesman()
        
    else:
        print("")
        print("PLEASE ENTER A VALID CHOICE")
        mastercreation()
        
ch="y"
while ch=="y":
    mastercreation()
    ch=input("Enter 'y' to continue...")
    if ch=="y":
        continue
    else:
        print("Exiting")
        break
