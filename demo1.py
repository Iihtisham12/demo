print("This is My Demo One Class")

def simple_calculate_sum(sum):
    if (1+6) == (sum):
        print("The Sum Result is",sum)
    else:
        print("Sorry I Can't Recongnaize")
simple_calculate_sum(7)

name = input('Enter Ur Name')
try:
    if int(name) // int(name) == 1:
        print("Sorry Number is Not Allowd!")
except:
    print(f"Hillo {name.capitalize()}")