## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def age_checker(date_of_birth):
    """
    Takes a persons date of birth and checks if they are old enough
    If they are over 16 we grant them access
    If they are under 16 we deny them access, and tell them their current age and the required age (16)

    Parameters: date_of_birth: a date obj?

    Returns: a string 

    if they are over 16 --> "Access granted"
    if they are under 16 --> "Access denied. You are {age} and the requried age is 16."

    Side effects: 
    Prints a string 
    """

```


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a user is over 16 
It returns the string --> "Access granted"
"""

age_checker("2001-07-08") => "Aceess granted"

"""
Given a user is under 16
It returns a string --> "Access denied. You are 15, and the required age is 16."
"""
age_checker("2011-01-01") => "Access denied. You are 15, and the required age is 16."

"""
Given a None value
It throws an error
"""
age_checker(None) throws an error

"""
Given a user is exactly 16 
It returns the string --> "Access granted"
"""

age_checker("2010-01-08") => "Aceess granted"

"""
Given a date in the incorrect format 
It returns a string --> "Invalid date format. Please use YYYY-MM-DD"
"""

age_checker("apple") => "Invalid date format. Please use YYYY-MM-DD"


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
