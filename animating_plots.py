import matplotlib.pyplot as plt
import random

# Counts for heads and tails
head_tail = [0, 0]

plt.ion()  # Interactive mode on
fig, ax = plt.subplots()

for _ in range(10000):
    # Randomly increment either heads (0) or tails (1)
    head_tail[random.randint(0, 1)] += 1

    # Clear previous frame
    ax.clear()

    # Draw bars with current counts
    ax.bar(['Heads', 'Tails'], head_tail, color=['red', 'blue'])

    # Add labels and title
    ax.set_ylabel("Count")
    ax.set_title("Coin Flip Simulation")

    # Small pause for animation effect
    plt.pause(0.0001)

plt.ioff()  # Turn off interactive mode
plt.show()
