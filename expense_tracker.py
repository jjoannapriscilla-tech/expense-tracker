print("Expense Tracker Started")

d=[]
#options
while(True):
    print("-----------------------------------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Category Summary")
    print("5. Exit")
    ch=int(input("Enter your choice(1,2,3,4,5)"))
    print("-----------------------------------------")

#1. Add Expense:

    if(ch==1):
        ex_name=input("Enter the Expense name:")
        amount=int(input("Enter the Amount:"))
        category=input("Enter the Category:")
        d.append([ex_name,amount,category])
        print("Expense added successfully")

#2. View Expenses
    elif(ch==2):
        print("=====All Expenses=====")
        if(len(d)==0):
            print("No expenses added yet.")
        for i in range(len(d)):
            print(i+1,". ",d[i][0],"\t",d[i][1],"\t",d[i][2])

#3. Total Spending
    elif(ch==3):
        total_sp=0
        for i in range(len(d)):
            total_sp+=d[i][1]
        print("Total amount spent: ₹",total_sp)

#4. Category Summary
    elif(ch==4):
        print("===== Category Summary=====")
        cat=[]
        for i in range(len(d)):
            found = False
            for j in range(len(cat)):
                if(d[i][2] == cat[j][0]):
                    cat[j][1] = cat[j][1] + d[i][1]
                    found = True
                    break

            if(found == False):
                cat.append([d[i][2], d[i][1]])

        for i in range(len(cat)):
            print(cat[i][0], ":\t₹", cat[i][1])

#5. Exit
    elif(ch==5):
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Kindly enter the right option:")


            
            




