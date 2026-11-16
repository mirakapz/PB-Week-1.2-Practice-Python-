#0.8 Basketball Equipment
tax = int(input())

shoes_price = tax - (tax * 0.4) #Shoes = 40% from the tax for the year.
suit_price = shoes_price - (shoes_price * 0.2) #Suit = 20% cheaper than the Shoes
ball_price = suit_price / 4 #Ball = 1/4th from the suit price
accessory_price = ball_price / 5 #Accessories = 1/5th from the ball price

total_price = tax + shoes_price + suit_price + ball_price + accessory_price
print(total_price)