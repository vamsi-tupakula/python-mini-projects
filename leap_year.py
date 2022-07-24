def leap_or_not(year):
    # a leap year is either divisible by 400 or divisible by 4 but not with 100
    if(year%400 == 0):
        print(f"yes! {year} is a leap year")
        return
    
    if(year%4 == 0 and year%100 != 0):
        print(f"yes! {year} is a leap year")
        return
    
    print(f"no! {year} is not a leap year")

year = input("Enter any year :: ")
leap_or_not(int(year))