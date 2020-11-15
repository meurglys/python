# Define your functions
message = "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response."

def get_cup():
  res = input("Would you like to use our own reusable cup or a plastic one? \n [a] Reusable cup \n [b] Plastic cup \n")
  if res == 'a':
    return "Reusable cup"
  elif res == 'b':
    return "Plastic cup"
  else:
    return print(message), get_cup()

def order_latte():
  res = input("And what kind of milk for your latte? \n [a] 2% milk \n [b] Non-fat milk \n [c] Soy milk \n>")
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    return print(message), order_latte()

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    return print(message), get_size()

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>")
  if res == 'a':
    return "Brewed Coffee"
  elif res == 'b':
    return "Mocha"
  elif res == 'c':
    return order_latte()
  else:
    return print(message), get_drink_type()

def next_order():
  res = input("Would you like to make another order? \n [a] Yes, please. \n [b] No, thanks. \n")
  if res == 'a':
    return get_size(), get_drink_type(), get_cup()
  elif res == 'b':
    return "Have a good day!"
  else:
    return print(message)

def coffee_bot():
  print("Welcome to the cafe!")

  size = get_size()
  drink_type = get_drink_type()
  cup = get_cup()

  print("Alright, that's a %s %s in %s" %(size, drink_type, cup))

  name = input("Can I get your name please? \n")
  print("Thanks, %s! Your drink will be ready shortly."%(name))

  order = next_order()
  print(order)

# Call coffee_bot()!
coffee_bot()
