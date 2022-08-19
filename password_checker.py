# 1. Must have at least one capital letter
# 2. Must have at least one number
# 3. Must have at least one symbol or special character
# 4. Must include the word "dolphin"

def user_password():
  password = input(
    """
    1. Must have at least one capital letter
    2. Must have at least one number
    3. Must have at least one symbol or special character
    4. Must include the word "dolphin"
  
    """
    
    "Please create a password that meets the conditions above: "
  )
  
  return password

def check_capital_letter(password):
  has_upper = False
  for char in password:
    if char.isupper():
      has_upper = True
      break

  if not has_upper:
    print("Password must include capital letter")
      
  return has_upper
  
def check_number(password): 
  has_digit = False
  for char in password:
    if char.isdigit():
      has_digit = True
      break
    
  if not has_digit:
    print("Password must include number")
    
  return has_digit
  
def check_symbol(password):
  has_char = False
  for char in password:
    if not char.isalnum():
      has_char = True
      break
    
  if not has_char:
    print("Password must include symbol")
    
  return has_char
  
def check_dolphin(password):
  has_dolphin = False
  if "dolphin" in password.lower():
    has_dolphin = True
  else:
    print("password must include the word dolphin")
    
  return has_dolphin


  
  
password = user_password()
# rule_1 = check_capital_letter(password)
# rule_2 = check_number(password)
#rule_3 = check_symbol(password)
rule_4 = check_dolphin(password)
