import streamlit as st
import json
import requests

# Define users for authentication
users = {
    "username1": "password1",
    "username2": "password2"
}

def load_math_problems():
    math_problems = []
    try:
        with open('math_conversations.jsonl', 'r') as file:
            for line in file:
                math_problems.append(json.loads(line))
    except Exception as e:
        st.error(f"Failed to load problems: {e}")
    return math_problems

def fetch_lesson(topic):
    url = "https://proxy.tune.app/chat/completions"
    headers = {
        "Authorization": "Bearer sk-tune-ZgdhdHSpf63t5Hvx5k2jQoK0IkK3zo6kYPx",
        "Content-Type": "application/json",
    }
    data = {
        "temperature": 0.7,
        "messages": [
            {"role": "system", "content": "You are a math tutor specialized in solving math problems for 5th graders."},
            {"role": "user", "content": f"Generate a Grade 5 math lesson on {topic}, including an explanation and a practice problem."}
        ],
        "model": "meta/llama-3.1-8b-instruct",
        "stream": False,
        "frequency_penalty": 0.1,
        "max_tokens": 500
    }
    response = requests.post(url, headers=headers, json=data)
    if response.ok:
        return response.json()['choices'][0]['message']['content']
    else:
        st.error(f"Failed to fetch lesson: {response.text}")
        return "Failed to generate lesson."

def app():
    option = st.selectbox("Choose an option:", ["Learn", "Assessment", "Connect to Tutor"])

    if option == "Learn":
        topic = st.text_input("Enter a Math Topic (e.g., fractions, multiplication)")
        if st.button("Generate Lesson"):
            lesson = fetch_lesson(topic)
            st.write(lesson)

    elif option == "Assessment":
        problems = load_math_problems()
        num_problems = st.number_input("How many problems would you like to solve?", min_value=1, max_value=len(problems), step=1, value=5)
        problem_indices = range(min(num_problems, len(problems)))
        problem_options = [problems[i]['conversations'][1]['content'] for i in problem_indices]
        selected_indices = st.multiselect("Select problems to solve", problem_indices, format_func=lambda x: problem_options[x])
        answers = {}
        for index in selected_indices:
            answer_key = f"answer_{index}"
            answers[answer_key] = st.text_input(f"Answer for: {problems[index]['conversations'][1]['content']}", key=answer_key)
        if st.button("Submit Answers"):
            correct_answers = 0
            for answer_key, user_answer in answers.items():
                index = int(answer_key.split('_')[1])
                correct_answer = problems[index]['conversations'][2]['content'].strip()
                if user_answer.strip().lower() == correct_answer.lower():
                    correct_answers += 1
                    st.write(f"Correct! The solution to {problems[index]['conversations'][1]['content']} is indeed {correct_answer}.")
                else:
                    st.write(f"Incorrect. The correct solution to {problems[index]['conversations'][1]['content']} is {correct_answer}, not {user_answer}.")
            st.success(f"You answered {correct_answers} out of {len(answers)} correctly.")
    
    elif option == "Connect to Tutor":
        st.subheader("Book a Session with a Tutor")
        tutor = st.selectbox("Choose your tutor:", ["Mrs. Rania", "Mrs. Prabhudas"])
        day = st.selectbox("Select Day:", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
        time = st.selectbox("Select Time Slot:", ["10:00 AM - 11:00 AM", "11:00 AM - 12:00 PM", "2:00 PM - 3:00 PM", "3:00 PM - 4:00 PM"])
        if st.button("Book Session"):
            st.success(f"You have successfully booked a session with {tutor} on {day} at {time}.")

def main():
    st.image("logo.png", width=200)  # Display the logo
    st.title("Welcome to Pehla School - From Horizon to Horizon Learning made personal")
    st.title("स्वागत है पहला स्कूल में - सिखाने की सीमा से सीमा तक व्यक्तिगत बनाना")

    if 'login_status' not in st.session_state:
        st.session_state['login_status'] = False

    if not st.session_state['login_status']:
        with st.sidebar:
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                if users.get(username) == password:
                    st.session_state['login_status'] = True
                    st.session_state['username'] = username
                    st.sidebar.success(f"Logged in as {username}")
                else:
                    st.sidebar.error("Incorrect username or password")

    if st.session_state.get('login_status', False):
        app()

if __name__ == "__main__":
    main()
