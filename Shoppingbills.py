salary=int(input("Enter your salary"))
bill1=float(input("enter your bill amount 1"))
bill2=float(input("enter your bill amount 2"))
bill3=float(input("enter your bill amount 3"))
total=bill1+bill2+bill3
print(f'total shopping bill amount {total:.2f}')
percent1=(bill1/total)*100
print(f'percentage of bill1 amount is {percent1:.2f}')
percent2=(bill2/total)*100
print(f'percentage of bill2 amount is {percent2:.2f}')
percent3=(bill3/total)*100
print(f'percentage of bill3 amount is {percent3:.2f}')
