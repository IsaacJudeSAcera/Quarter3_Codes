monthly_revenue = [
    [12000, 13500, 14000, 15000],
    [11000, 12500, 13000, 14500],
    [13000, 14000, 15000, 16000]
]
highest_revenue = 0

for month_number in range(len(monthly_revenue)):
    weekly_revenues = monthly_revenue[month_number]
    print("Month", month_number + 1, "weekly revenues:", weekly_revenues)
    
    total = 0
    for revenue in weekly_revenues:
        total += revenue
    
    average = total / len(weekly_revenues)
    
    print("Total revenue for Month", month_number + 1, ":", total)
    print("Average weekly revenue for Month", month_number + 1, ":", round(average, 2))
    print("--------------------")
    
    max_this_month = max(weekly_revenues)
    if max_this_month > highest_revenue:
        highest_revenue = max_this_month

print("The highest weekly revenue recorded is:", highest_revenue)
print ("maximum value in dataset:", highest_revenue)
#Using an array helped me organize the data neatly so I could easily access the revenue for each week and month. 
It made calculations like totals and averages straightforward because I could loop through the rows and columns systematically. 
#The easiest part was adding up the numbers since the data was well-structured. 
#The challenging part was making sure I checked every value correctly to find the highest revenue without missing anything