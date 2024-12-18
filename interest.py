k0 = float(input("Enter the initial balance (K0): "))
rate = float(input("Enter the interest rate : "))
time = int(input("Enter the number of years (n): "))
i = 0
k = k0
while i < time:
  k = k * (1 + rate)
  i += 1
print("The capital after", time, "years is:", k)
