password = "dolphin13!!!"
# password = input()

for char in password:
  has_upper = False
  if char.isupper():
    has_upper = True
    break
  
if not has_upper:
  print("Password must include capital letter")


# for char in password:
#   print(char)
#   has_upper = False
#   if char.isupper():
#     has_upper = True
#     break