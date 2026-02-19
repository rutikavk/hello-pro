import random
actions = ["Click", "Scroll", "Exit"]
sample_space = []
for a1 in actions:
    for a2 in actions:
        sample_space.append((a1, a2))
print("Sample Space S:")
print(sample_space)
event_E = []
for outcome in sample_space:
    if "Click" in outcome:
        event_E.append(outcome)
total_outcomes = len(sample_space)
favorable_outcomes = len(event_E)
probability_E = favorable_outcomes / total_outcomes
print("\nTotal Outcomes:", total_outcomes)
print("Favorable Outcomes (At least one Click):", favorable_outcomes)
print("Probability of at least one Click:", round(probability_E, 4))
trials = 1000
count_sum_7 = 0
for i in range(trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 7:
        count_sum_7 += 1
experimental_probability = count_sum_7 / trials
print("\nExperimental Probability of sum = 7 after 1000 rolls:",
      round(experimental_probability, 4))
