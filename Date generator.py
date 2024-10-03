def func(day_number, year):
    months = [
        ("January", 31),
        ("February", 28),  
        ("March", 31),
        ("April", 30),
        ("May", 31),
        ("June", 30),
        ("July", 31),
        ("August", 31),
        ("September", 30),
        ("October", 31),
        ("November", 30),
        ("December", 31),
    ]

    def is_leap_year(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    if is_leap_year(year):
        months[1] = ("February", 29)

    month_name = ""
    day = 0
    for month, days in months:
        if day_number <= days:
            month_name = month
            day = day_number
            break
        day_number -= days  
    return f"{day} {month_name}, {year}"

i_day = 256
i_year = 2021
o_date = func(i_day, i_year)
print(o_date)  
