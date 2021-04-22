hour = input("Please enter hour here:")
rate = input("Please enter rate per hour here:")
try:
    h = float(hour)
    r = float(rate)
    if h <= 40:
      pay = h * r
    else:
      pay = 40 * r + (h-40) * r * 1.5

    print(pay)
except:
    print("Error, please enter numeric input.")
