from math import floor, ceil

pages_count = int(input())
pages_read_hour = int(input())
days_count = int(input()) 

total_time = (pages_count / pages_read_hour) #1 Done
hours_needed_day = total_time / days_count

print(floor(hours_needed_day))