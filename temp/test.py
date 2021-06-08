new_menu = ['Hawaiian', 'Margherita', 'Mushroom', 'Prosciutto', 'Meat Feast', 'Hawaiian', 'Bacon', 'Black Olive Special', 'Sausage', 'Sausage']

final_new_menu = list(dict.fromkeys(new_menu))

print(type(final_new_menu))

final_new_menu.remove('1')