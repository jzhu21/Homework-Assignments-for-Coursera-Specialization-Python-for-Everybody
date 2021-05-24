# Week 7, worked exercise 5.1 - Exercise 1

total = 0
count = 0

while True:
    number = input("Enter a number:")
    try:
        num_f = float(number)
        total = total + num_f
        count = count + 1
    except:
        if number == "done":
            break
        else:
            print("Invalid input")
            continue

avg =  total/count
print(total, count, avg)
