#0.7 Food Delivery
CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGAN_MENU = 8.15
DELIVERY_COST = 2.50

chicken_count = int(input())
fish_count = int(input())
vegan_count = int(input())

chicken_price = chicken_count * CHICKEN_MENU
fish_price = fish_count * FISH_MENU
vegan_price = vegan_count * VEGAN_MENU
menu_price = chicken_price + fish_price + vegan_price
dessert_discount = menu_price * 0.20 #20% off of the total menu price.
total_price = menu_price + dessert_discount + DELIVERY_COST

print(f"{total_price:.2f}")