year = int(input("enter a year: "))

def is_year_leap(year):
    if(year / 4) == 0:
        print(True)
    else:
        print(False)
print(is_year_leap(year))