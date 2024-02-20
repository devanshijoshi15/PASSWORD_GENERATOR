import random
import string

def generate_password(length):
  """Generates a random password of the given length, ensuring randomness.

  Args:
    length: The desired length of the password.

  Returns:
    A random password of the specified length.
  """

  # Combine character sets for more variety
  all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

  # Choose characters from each set using weighted random selection
  password = ""
  character_sets = (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation)
  for _ in range(length):
    # Ensure at least one character from each set is included
    if len(password) < len(character_sets):
      chosen_set = random.choice(character_sets)
    else:
      chosen_set = random.choices(character_sets, weights=[3, 3, 2, 2])[0]  # More weight for lowercase and uppercase
    password += random.choice(chosen_set)

  # Shuffle the characters for additional randomness
  password_list = list(password)
  random.shuffle(password_list)
  password = "".join(password_list)

  return password

# Get desired password length from the user
password_length = int(input("Enter desired password length: "))

# Generate and print the password
password = generate_password(password_length)
print(f"Your random password: {password}")
