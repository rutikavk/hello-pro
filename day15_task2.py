p_heads = 1 / 2
p_six = 1 / 6
p_independent = p_heads * p_six

print("---- Independent Event ----")
print("P(Heads AND Rolling a 6) =", p_independent)
total_marbles = 10
red_marbles = 5
p_first_red = red_marbles / total_marbles
remaining_red = 4
remaining_total = 9
p_second_red = remaining_red / remaining_total
p_dependent = p_first_red * p_second_red

print("\n---- Dependent Event ----")
print("P(Both marbles are Red) =", p_dependent)
print("\nReflection:")
print("The denominator changed for the second marble because")
print("we removed one marble from the bag (no replacement).")
print("Total marbles decreased from 10 to 9.")
