steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

total_steps_per_day = []

number_of_days = len(steps[0])

for day_index in range(number_of_days):
    total_for_day = 0
    for person_steps in steps:
        total_for_day += person_steps[day_index]
    total_steps_per_day.append(total_for_day)

for i in range(number_of_days):
    print(days[i] + ": " + str(total_steps_per_day[i]) + " steps")

most_active_day_index = total_steps_per_day.index(max(total_steps_per_day))

print("Most active day overall: " + days[most_active_day_index])