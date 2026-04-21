from datetime import date


def age_checker(date_of_birth):
    date_object = date.fromisoformat(date_of_birth)
    year = date_object.year
    current_year = 2026
    age = current_year - year
    if age < 16:
        return f"Access denied. You are {age}, and the required age is 16."
    elif age >= 16:
        return "Access granted"