#0.3 Deposit Calculator
deposit_sum = float(input())
deposit_term = int(input())
yearly_interest = float(input())

# interest = deposit_sum * (yearly_interest / 100) #1 Done.
# monthly_interest = interest / 12 #2 Done
# total_sum = deposit_sum + deposit_term * monthly_interest #3 Done

sum = deposit_sum + deposit_term * ((deposit_sum * yearly_interest / 100 ) / 12)
print(f"{sum:.2f}")