#0.6 Repainting
SAFETY_NYLON = 1.50
PAINT_LITER = 14.50
PAINT_THINNER = 5
BAGS = 0.40
EXTRA_PAINT = 10 / 100 #10% = 0.1 to the paint

nylon_needed = int(input())
paint_needed = int(input())
thinner_litres = int(input())
hours_work = int(input())

#Extras:
paint_extra = paint_needed * EXTRA_PAINT # paint_needed * 0.1 = needed extra paint.
mats_extra = 30 / 100 #Needed for workers | 30% of the sum of all costs for materials. 30 / 100 = 0.3

nylon_price = (nylon_needed + 2) * SAFETY_NYLON #1 Done
paint_price = (paint_needed + paint_extra) * PAINT_LITER #2 Done #Extra paint: 10 / 100 = 0.10, 11 * 0.10 = 1.1
thinner_price = thinner_litres * PAINT_THINNER #3 Done
material_price = (nylon_price + paint_price + thinner_price) + 0.40 #4 Done
worker_price = (material_price * mats_extra) * hours_work #5 Done 

sum = material_price + worker_price

print(sum)