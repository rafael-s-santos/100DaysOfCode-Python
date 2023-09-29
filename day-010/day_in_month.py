def is_leap(year: int) -> bool:
    """Checks whether the year is a leap year and if so, 
    returns True. If not, it returns False.
    """
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False
    else:
        return False


def days_in_month(year: int, month: int) -> int:
    """Returns how many days are in the month based on the year 
    and month entered.
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        month_days[1] = 29
    else:
        return month_days[(month-1)]
    return month_days[(month-1)]


print(days_in_month(int(input("Year: ")), int(input("Month: "))))
