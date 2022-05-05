calcultion_to_unit = 24
name_of_unit = "hours"


def days_to_unit(num_of_days):
    if  num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calcultion_to_unit} {name_of_unit}"
    elif num_of_days == 0:
        return "You enter a 0 "
    else:
        return "You enter a negative number"

user_input = input("Hey user enter a number\n")
user_input_number = int(user_input)
calculate_value = days_to_unit(user_input_number)
print(calculate_value)


days_to_unit(35)