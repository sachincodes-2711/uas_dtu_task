# 1. Create the main list
camps = [
    {'color': 'Pink', 'assigned': []},
    {'color': 'Blue', 'assigned': []}
]

# 2. Pick one camp out of the list (Logic from your code)
best_camp = None
for camp in camps:
    if camp['color'] == 'Pink':
        best_camp = camp  # <--- This creates a REFERENCE, not a copy

# 3. Modify 'best_camp'
print(f"Before update: {camps}")
best_camp['assigned'].append("Survivor_1")

# 4. Check the original 'camps' list
print(f"After update:  {camps}")