p_spam = 0.1
p_ham = 0.9
p_free_given_spam = 0.9
p_free_given_ham = 0.05
p_free = (p_free_given_spam * p_spam) + \
         (p_free_given_ham * p_ham)
p_spam_given_free = (p_free_given_spam * p_spam) / p_free
print("P(Free) =", round(p_free, 4))
print("P(Spam | Free) =", round(p_spam_given_free, 4))
print("Probability email is Spam if it contains 'Free' =", 
      round(p_spam_given_free * 100, 2), "%")
