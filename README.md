# hackmit-pehla_school

[![Repo](https://img.shields.io/badge/GitHub-hackmit-pehla_school-181717?logo=github)](https://github.com/sinhaarya04/hackmit-pehla_school)

## Overview

Pehla School is a platform designed to provide AI-generated lessons, assessments, and access to personalized tutoring for students up to grade 8. The project brings personalized learning into the hands of students and tutors, bridging the gap between rural and urban education.

## Features

- Project-specific implementation and experiments

## Tech Stack

- Node.js
- React
- Tailwind CSS
- npm
- Python

## Getting Started

### Prerequisites

- Git
- A recent runtime for the stack above (e.g., Python 3.10+ or Node 18+)

### Installation

```bash
npm install
```

### Run / Usage

```bash
# Common scripts (pick the one your repo supports)
npm run dev
npm run build
npm start
```

## Project Structure

- `small_math_dataset/`
- `small_math_dataset_50/`
- `app.py`
- `convert.py`
- `filter_datasets.py`
- `logo.png`
- `math_conversations.jsonl`
- `package-lock.json`
- `package.json`
- `project.py`

## Roadmap

- [ ] Add clearer usage examples and expected outputs
- [ ] Add tests / CI (if applicable)
- [ ] Document data sources and assumptions (if applicable)

## License

No license file found in this repository.


---

## Notes / Original README

The content below is preserved from the previous README for reference.

# Pehla School – From Horizon to Horizon, Learning Made Personal

Pehla School is a platform designed to provide AI-generated lessons, assessments, and access to personalized tutoring for students up to grade 8. The project brings personalized learning into the hands of students and tutors, bridging the gap between rural and urban education.

## Features

- **AI-Generated Lessons**: Students can input a topic and receive an instant lesson with explanations and practice problems.
- **Assessment Module**: Take quizzes and receive immediate feedback with correct answers and explanations.
- **Tutor Booking**: Book a session with one of our tutors, Mrs. Rania or Mrs. Prabhudas, for personalized help.
- **Bilingual Support**: English and Hindi support to reach a wider audience.
- **User Authentication**: Simple login system for personalized learning sessions.

## How to Run the Project

1. **Clone the Repository**:
   ```
   git clone https://github.com/YourUsername/PehlaSchool.git
   ```

2. **Install Dependencies**:
   Navigate to the project folder:
   ```
   cd PehlaSchool
   ```
   Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**:
   ```
   streamlit run app.py
   ```

   If using GitHub Codespaces, run the above command in the terminal provided by Codespaces.

4. **Access the App**:
   The Streamlit app will provide a local URL (like `http://localhost:8501`). Open it in your browser to use the platform.

## Demo

- Clone the project and install the dependencies.
- Run the command `streamlit run app.py`.
- Open the provided local URL to interact with the app.

## Technology Stack

- **Front-end**: Streamlit for building the user interface.
- **Backend**: AI-generated lessons using Meta LLaMA 3.1.
- **APIs**: The app communicates with the API for real-time responses and lesson generation.
- **Authentication**: Basic user login and session management.

## Future Features

- Expand subject coverage.
- Develop a mobile application for iOS and Android.
- Implement adaptive learning algorithms to personalize lesson difficulty.

---
