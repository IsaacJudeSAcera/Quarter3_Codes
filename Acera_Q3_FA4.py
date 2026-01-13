names = ["Me", "Lia", "Jake"]

steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]
total_steps = []

for person_steps in steps:
    total = sum(person_steps)
    total_steps.append(total)

max_steps = max(total_steps)
min_steps = min(total_steps)

max_index = total_steps.index(max_steps)
min_index = total_steps.index(min_steps)

print("Total steps per person:")
for i in range(len(names)):
    print(names[i] + ": " + str(total_steps[i]) + " steps")

print("Person with highest total steps: " + names[max_index] + " with " + str(max_steps) + " steps")
print("Difference between highest and lowest total steps: " + str(max_steps - min_steps))