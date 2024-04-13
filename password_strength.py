import re

def assess_password_strength(password):
    # Initialize variables to track criteria
    length = len(password)
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special_char = bool(re.search(r'[^A-Za-z0-9]', password))
    
    # Define criteria weights
    length_weight = 1
    uppercase_weight = 1
    lowercase_weight = 1
    digit_weight = 1
    special_char_weight = 2

    # Calculate total score based on criteria
    score = (length * length_weight) + \
            (has_uppercase * uppercase_weight) + \
            (has_lowercase * lowercase_weight) + \
            (has_digit * digit_weight) + \
            (has_special_char * special_char_weight)

    # Define threshold values for strength levels
    very_weak_threshold = 5
    weak_threshold = 10
    moderate_threshold = 15
    strong_threshold = 20

    # Determine strength level based on score
    if score < very_weak_threshold:
        strength = "Very Weak"
    elif score < weak_threshold:
        strength = "Weak"
    elif score < moderate_threshold:
        strength = "Moderate"
    elif score < strong_threshold:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, score

# Example usage

password = input("Enter your password: ")
strength, score = assess_password_strength(password)
print(f"Password Strength: {strength}")
print(f"Score: {score}")
