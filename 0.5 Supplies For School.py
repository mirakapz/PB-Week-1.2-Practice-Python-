#0.5 Supplies For School
PENS = 5.80
MARKERS = 7.20
WHITEBOARD_CLEANER = 1.20

pens_count = int(input())
markers_count = int(input())
cleaner_liters = int(input())
discount = int(input())

pen_price = pens_count * PENS #1 Done
marker_price = markers_count * MARKERS #2 Done
cleaner_price = cleaner_liters * WHITEBOARD_CLEANER #3 Done
total_price = pen_price + marker_price + cleaner_price #4 Done

discount_price = total_price - (total_price * (discount / 100)) #5 Done

print(discount_price)
