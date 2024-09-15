import json
import requests

# Set stream to False if you don't need streamed responses
stream = False

# The API URL for making requests
url = "https://proxy.tune.app/chat/completions"

# Your API key (ensure it is valid)
headers = {
    "Authorization": "sk-tune-ZgdhdHSpf63t5Hvx5k2jQoK0IkK3zo6kYPx",  # Replace with actual key
    "Content-Type": "application/json",
}

# Ask the user for the math topic they want to learn about
topic = input("Enter the Grade 5 math topic you'd like a lesson on (e.g., fractions, multiplication): ")

# Adjusting the data payload for a math lesson based on user input
data = {
    "temperature": 0.7,
    "messages": [
        {
            "role": "system",
            "content": "You are a math tutor specialized in solving math problems for 5th graders."
        },
        {
            "role": "user",
            "content": f"Generate a Grade 5 math lesson on {topic}, including an explanation and a practice problem."
        }
    ],
    "model": "meta/llama-3.1-8b-instruct",  # Ensure correct model
    "stream": stream,
    "frequency_penalty": 0.1,
    "max_tokens": 500  # Increased max tokens to avoid truncation
}

# Making the POST request to the API
response = requests.post(url, headers=headers, json=data)

# Handling streamed or non-streamed responses
if not response.ok:
    print(f"Error: {response.status_code} - {response.text}")
else:
    result = response.json()
    lesson = result['choices'][0]['message']['content']
    
    # Display the lesson
    print(f"AI Response: {lesson}")
    
    # Extract the practice problem dynamically from AI response
    print("\nHere is the practice problem for you to solve:")

    # Try to find the practice problem and solution
    try:
        # Look for both the practice problem and the solution
        practice_problem_start = lesson.lower().find("practice problem:")
        solution_start = lesson.lower().find("solution:", practice_problem_start)
        
        if practice_problem_start != -1:
            if solution_start != -1:
                practice_problem = lesson[practice_problem_start:solution_start].strip()
            else:
                # If there's no "solution" keyword, just get the remaining text
                practice_problem = lesson[practice_problem_start:].strip()

            print(practice_problem)
            
            # Ask the user for the answer to the problem
            user_answer = input("What's your answer to the practice problem? ")

            # If solution exists, show it
            if solution_start != -1:
                solution = lesson[solution_start:].strip()
                print("\nAI Solution:", solution)
            else:
                print("No solution provided in the AI response.")
        
        else:
            print("Could not extract a practice problem. Please try again.")
    
    except Exception as e:
        print(f"Error in extracting practice problem: {e}")
