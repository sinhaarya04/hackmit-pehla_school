import json
import requests

# Step 1: Load your dataset
math_problems = []
with open('math_conversations.jsonl', 'r') as f:
    for line in f:
        math_problems.append(json.loads(line))

def display_problems(problems):
    """ Display math problems for user to select from """
    print("\n=== Choose a math problem by number (or type 'quit' to exit) ===")
    for i, problem in enumerate(problems[:5]):  # Show the first 5 problems
        print(f"{i+1}. {problem['conversations'][1]['content']}")  # Display the question content

# Initialize grading variables
total_questions = 0
correct_answers = 0

while True:
    # Display a few math problems to the user
    display_problems(math_problems)

    # Get the user's choice
    user_input = input("\nEnter the problem number or 'quit' to exit: ")

    if user_input.lower() == 'quit':
        print(f"\nExiting the program. Final Score: {correct_answers}/{total_questions} correct!")
        break

    try:
        problem_number = int(user_input) - 1
        if problem_number < 0 or problem_number >= len(math_problems):
            raise ValueError("Invalid choice")
        problem = math_problems[problem_number]['conversations'][1]['content']
    except ValueError:
        print("\n[Error]: Please enter a valid number.")
        continue

    # Display the selected problem to the user
    print(f"\nYou selected problem:\n{problem}")

    # Ask the user for their answer
    user_answer = input("\nWhat is your answer to the problem? ")

    # Step 2: Send the selected problem and the user's answer to the API
    url = "https://proxy.tune.app/chat/completions"
    headers = {
        "Authorization": "sk-tune-ZgdhdHSpf63t5Hvx5k2jQoK0IkK3zo6kYPx",  # Your actual key
        "Content-Type": "application/json",
    }

    # Define the payload for the API request
    data = {
        "temperature": 0.7,
        "messages": [
            {
                "role": "system",
                "content": "You are a math tutor specialized in solving math problems for 5th graders. After the user gives an answer, explain the correct solution, and say if their answer was correct or not."
            },
            {
                "role": "user",
                "content": f"The math problem is: {problem}. The user's answer is: {user_answer}. Now, explain the correct solution and if their answer is correct."
            }
        ],
        "model": "meta/llama-3.1-8b-instruct",  # Ensure correct model
        "stream": False,
        "frequency_penalty": 0.1,
        "max_tokens": 200
    }

    # Step 3: Send the request to Tune AI
    response = requests.post(url, headers=headers, json=data)

    # Step 4: Print the AI's response and check correctness
    if response.ok:
        result = response.json()
        ai_response = result['choices'][0]['message']['content']
        print("\nAI's Explanation: ", ai_response)

        # Step 5: Check if AI's response mentions that the answer is correct or incorrect
        if "incorrect" in ai_response.lower():
            print("\nSorry, your answer is incorrect.")
        elif "correct" in ai_response.lower():
            correct_answers += 1
            print("\nWell done! You got it right.")
        else:
            print("\nThe AI couldn't determine if your answer was correct or not.")

        # Increment the total questions counter
        total_questions += 1

    else:
        print("\n[Error]: ", response.status_code, response.text)

    # Show the current score after each question
    print(f"\nCurrent Score: {correct_answers}/{total_questions}")
