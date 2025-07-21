import random  # Built-in module for randomness

# 🎲 Simulate a dice roll
roll = random.randint(1, 6)
print("You rolled:", roll)

# 🎨 Pick a random item from a list
colors = ['red', 'blue', 'green']
random_color = random.choice(colors)
print("Random color:", random_color)

# 🔁 Generate 3 random numbers between 1 and 10
print("Three random numbers:")
for _ in range(3):
    print(random.randint(1, 10))
