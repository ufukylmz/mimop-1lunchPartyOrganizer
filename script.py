menu_item = "pizza"
menu_item2 = "hamburger"
guests = 10
print(f"{menu_item}, {menu_item2}")
print(guests)
menu_item = "biryani"
print(f"Updated menu item is: {menu_item}, {menu_item2}")
biryani_per_person = 1
hamburger_per_person = 2
biryani_needed = biryani_per_person * guests
hamburger_needed = hamburger_per_person * guests
biryani_prepared = 10
hamburger_prepared = 12
enough_biryani = biryani_prepared >= biryani_needed
enough_hamburger = hamburger_prepared >= hamburger_needed
guests += 1
guests -= 3
biryani_per_guest = biryani_prepared / guests
hamburger_per_guest = hamburger_prepared / guests
print(biryani_per_guest)
print(hamburger_per_guest)
if biryani_per_guest < 1:
  print("Prepare more Biryani!")
if hamburger_per_guest <1:
  print("Prepare more Hamburger!")
if (biryani_per_guest >=1) and (hamburger_per_guest >=1):
  print("Ready to Serve!!")