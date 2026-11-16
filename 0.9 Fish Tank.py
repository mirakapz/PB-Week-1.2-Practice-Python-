#0.9 Fish Tank
length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input())

aquarium_volume = length_cm * width_cm * height_cm
volume_liters = aquarium_volume / 1000

#Percentage calculation:
occupied_volume = 1 - (percent / 100)

liters_needed = volume_liters * occupied_volume
print(liters_needed)