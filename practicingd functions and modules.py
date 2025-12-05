###No Parameters, No Return Value

def happy_birthday():
    print("Happy Birthday!")
    

# Code to call the function
happy_birthday()

### Parameters, but No Return Value  

def happy_birthday(age, name):

    print(f"Happy Birthday {name} and congratulations on turning {age} years old!")

# Code to call the function
happy_birthday(22, "Nora")





###No Parameters, but a Return Value

import random

def get_lucky_number():
  lucky_num = random.randint(1,100)
  return lucky_num

# Get a lucky number between 1 and 100
lucky_number = get_lucky_number()

print("Your lucky number is:", lucky_number)





### Parameters and Return Value  

def calc_sale_price(amount, member):
	if member:
		# Members receive a 15% discount (0.15)
		amount = amount - (amount * 0.15)
		
	else:
		# Non-members get a 5% discount (0.05)
		amount = amount - (amount * 0.05)

	rounded_amount = round(amount, 2)
	amount = rounded_amount
	

	# Return amount to the main program
	return amount

# Example price (already provided)
full_price = 150.50

# Call function for members
member_price = calc_sale_price(full_price, True)
print("Member price:",member_price)

# Call function for non-members
non_member_price = calc_sale_price(full_price, False)
print("Non-member price:",non_member_price)






### Scope

shirt_color = "Pink"

def display_color_works():
  
  print("First shirt color is:", shirt_color)
  
def display_color_failure():
  # Try to access 'color' directly (this will cause an error)
  print("Your shirt color is:", shirt_color)

# The shirt_color variable is in scope in this function
display_color_works()

# The shirt_color variable is not in scope in this function
display_color_failure()





###Importing a module  

import menus


# Call the display_menu function in the menus module
user_choice = menus.display_menu()

print(user_choice)