class Bank:
    acc_bal=10000
    def viewOptions(self):
        wd_attempts=0
        while True:
            print("1.Deposit")
            print("2.Withdraw")
            print("3.Balance Enquiry")
            print("4.Exit")
            options=int(input("Enter your choice"))
            if options==1:
                obj.deposit()
            elif options==2:
                if wd_attempts<3:
                    obj.withdrawal()
                    wd_attempts+=1
                else:
                    print("Maximum number of withdrawals are only 3")
            elif options==3:
                obj.enquiry()
            elif options==4:
                exit()
            else:
                print("Please enter valid choice")
    def validate(self):
        for i in range(3):
            pin=int(input("Enter your pin number"))
            if pin==1234:
                print("Valid PIN")
                obj.viewOptions()
                break
            else:
                print("Invalid PIN ! Please try again")
    def deposit(self):
        dep_amount=int(input("Enter the amount to be deposited"))
        if 500<dep_amount<20000 and dep_amount%100==0:
            self.acc_bal+=dep_amount
            print(f"Amount {dep_amount} deposited successfully")
        else:
            print("Cannot deposit")
    def withdrawal(self):
        wd_amount=int(input("Enter the amount you want to withdraw"))
        if 100 <= wd_amount <= 20000 and wd_amount % 100 == 0 and self.acc_bal>=500 and wd_amount<=self.acc_bal:
                self.acc_bal -= wd_amount
                print(f"Withdrawal of {wd_amount} successful.")
        else:
            print("Withdrawal unsuccessful")
    def enquiry(self):
        print(f'Your account balance is {self.acc_bal}')
obj=Bank()
obj.validate()
