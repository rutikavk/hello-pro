import numpy as np

# Step 1: Create a 5x3 array of random integers between 50 and 100
np.random.seed(0)   # for reproducible output (optional)
scores = np.random.randint(50, 101, size=(5, 3))

# Step 2: Calculate column-wise mean (mean of each subject)
mean_scores = np.mean(scores, axis=0)

# Step 3: Subtract mean from original scores (broadcasting)
centered_scores = scores - mean_scores

# Step 4: Print results
print("Original Scores (5 students x 3 subjects):")
print(scores)

print("\nMean of each subject (column-wise mean):")
print(mean_scores)

print("\nCentered Scores (after subtracting mean):")
print(centered_scores)
