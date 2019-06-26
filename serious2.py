price={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3}
stock={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15}
total=0
for key in price:
    print(key,': price = ',price[key],', stock = ',stock[key])
    total=total+price[key]*stock[key]
print('If you sold all of the food, you got',total)




