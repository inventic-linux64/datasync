def calculate_pi(num_terms):
  pi = 0
  for i in range(1, num_terms + 1):
    term = 4 / (2 * i - 1) if i % 2 == 1 else -4 / (2 * i - 1)
    pi += term
  return pi

num_terms = 100000  # adjust for desired precision
pi_value = calculate_pi(num_terms)
print(f"Pi calculated with {num_terms} terms: {pi_value}")
