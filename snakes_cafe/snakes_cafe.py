user_order = {
  'Wings': 0,
  'Cookies': 0,
  'Spring Rolls': 0,
  'Salmon': 0,
  'Steak': 0,
  'Meat Tornado': 0,
  'A Literal Garden': 0,
  'Ice Cream': 0,
  'Cake': 0,
  'Pie': 0,
  'Coffee': 0,
  'Tea': 0,
  'Unicorn Tears': 0,
}

cont_order = True

def __welcome__():
  print('''
  **************************************
  **    Welcome to the Snakes Cafe!   **
  **    Please see our menu below.    **
  *                                    *
  ** To quit at any time, type "quit" **
  **************************************

  Appetizers
  ----------
  Wings
  Cookies
  Spring Rolls

  Entrees
  -------
  Salmon
  Steak
  Meat Tornado
  A Literal Garden

  Desserts
  --------
  Ice Cream
  Cake
  Pie

  Drinks
  ------
  Coffee
  Tea
  Unicorn Tears

  ***********************************
  ** What would you like to order? **
  ***********************************
  ''')

def __order__():
  order = input()
  if order  == 'quit':
    global cont_order
    cont_order = False
  elif order in user_order.keys():
    user_order[order] += 1
    print(str('** ' + str(user_order[order]) + ' orders of ' + order + 'have been added to your meal**'))
  else:
    print("Sorry, we don't carry that. Try our Vancouver location.") 

__welcome__()
while cont_order == True:
  __order__()