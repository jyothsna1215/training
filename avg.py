number=int(input("Enter the student number"))
name=input("Enter the student name")
c=int(input("Enter the marks in c"))
cpp=int(input("Enter the marks in c++"))
java=int(input("Enter the marks in java"))
total=c+cpp+java
avg=total/3
if avg<70:
  print("Fail")
else:
  print("Pass")
  if avg>90:
    print("A")
  elif avg>80:
    print("B")
  else:
    print("C")
