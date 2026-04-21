from datetime import date

def age_checker(date_of_birth):
    try:
        dob = date.fromisoformat(date_of_birth)
        today = date.today()

        # calculates the age based on whether the birthday has passed this year
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        if age < 16:
            return f"Access denied. You are {age}, and the required age is 16."
        return "Access granted"
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

    

