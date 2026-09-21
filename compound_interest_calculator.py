# Python compound interest calculator


principle = 0
rate = 0
time = 0

while principle <= 0:
   principle = float(input("enter the principle amount: "))
   if principle <= 0:
     print("Principle cant be less than or equal to zero")

while rate <= 0:
   rate = float(input("enter the interest rate amount: "))
   if rate <= 0:
      print("Interest Rate cant be less than or equal to zero")

while time <= 0:
    time = float(input("enter the time is years: "))
    if time <= 0:
        print("Time cant be less than or equal to zero")


total = principle * pow((1 + rate / 100), time)
print(f"-----------------------------------------")
print(f"Balance after {time} year/s: ${total:.2f}")