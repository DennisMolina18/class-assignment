
class Menu:
 #2. Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
 
  def __repr__(self):
    return self.name + " menu available from " + str(self.start_time) + "h to " + str(self.end_time) + "h."
    
  def calculate_bill(self, purchased_items):
    total = 0
    for i in purchased_items:
      total += self.items.get(i, 0)
    return total
#3. Let’s create our first menu: brunch. Brunch is served from 11am to 4pm. The following items are sold during brunch:
items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu("brunch", items, 11, 16)
print(brunch)
#8. Try out our string representation. If you call print(brunch) 

#4. Let’s create our second menu item early_bird. Early-bird Dinners are served from 3pm to 6pm. The following items are available during the early-bird menu:

items2 = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu("early-bird", items2, 15, 18)
#5. Let’s create our third menu, dinner. Dinner is served from 5pm to 11pm. The following items are available for dinner:
items3 = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu("dinner", items3, 17, 23)
#6. And let’s create our last menu, kids. The kids menu is available from 11am until 9pm. The following items are available on the kids menu.
items4 = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("kids", items4, 11, 21)
#10. Test out Menu.calculate_bill(). We have a breakfast order for one order of pancakes, one order of home fries, and one coffee. Pass that into brunch.calculate_bill() and print out the price.
print("The price of a breakfast order for one order of pancakes, one order of home fries, and one coffee is: " + str( brunch.calculate_bill(['pancakes', 'home fries', 'coffee']) ))

#11.What about an early-bird purchase? Our last guests ordered the salumeria plate and the vegan mushroom ravioli. Calculate the bill with .calculate_bill()

print("The price of a salumeria plate and the vegan mushroom ravioli is: " + str( early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']) ))

#13. Give the Franchise class a constructor. Take in an address, and assign it to self.address. Also take in a list of menus and assign it to self.menus.

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return "the address of the restaurant is: " + self.address
  def available_menus(self, time):
    menu_list = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        menu_list.append(menu)
    return menu_list
#14. Let’s create our first two franchises! Our flagship store is located at "1232 West End Road" and our new installment is located at "12 East Mulberry Street". Pass in all four menus along with these addresses to define flagship_store and new_installment.
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
print(flagship_store)
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
print(new_installment)
#18. Let’s do another test! See what is printed if we call .available_menus() with 5pm as an argument and print out the results.

print(flagship_store.available_menus(12))
print(new_installment.available_menus(17))

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
    
#21. Let’s create our first Business. The name is "Basta Fazoolin' with my Heart" and the two franchises are flagship_store and new_installment.
    
first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepas_menu = Menu("arepa",{'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 10, 20)
#22. Before we create our new business, we’ll need a Franchise and before our Franchise we’ll need a menu. The items for our Take a’ Arepa available from 10am until 8pm are the following:
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
new_business = Business("Take a' Arepa", [arepas_place])
#24. Now let’s make our new Business! The business is called "Take a' Arepa"!
print(new_business.name)
print(new_business.franchises[0])