import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).
    
    Parameters:
        min_value (int): The minimum integer value.
        max_value (int): The maximum integer value.
    
    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def select_operator():
    """
    Randomly select a math operator from '+', '-', or '*'.
    
    Returns:
        str: A randomly selected operator.
    """
    return random.choice(['+', '-', '*'])

def calculate_answer(num1, num2, operator):
    """
    Calculate the result of the math expression based on the operator.
    
    Parameters:
        num1 (int): The first operand.
        num2 (int): The second operand.
        operator (str): The operator, one of '+', '-', or '*'.
    
    Returns:
        tuple: The problem as a string and the correct answer as an integer.
    """
    problem = f"{num1} {operator} {num2}"
    
    # Correct the calculation based on the operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        raise ValueError("Unsupported operator")  # Adding safety for unknown operators
    
    return problem, answer

def math_quiz():
    """
    Run the math quiz game, where the user answers random math problems.
    """
    score = 0
    total_questions = 3  # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = select_operator()

        # Generate problem and calculate correct answer
        problem, correct_answer = calculate_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Error handling for invalid user input
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        # Check if user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
