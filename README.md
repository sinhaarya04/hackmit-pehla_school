# 🏫 Pehla School

> *From horizon to horizon, learning made personal.*

![HackMIT 2024](https://img.shields.io/badge/HackMIT-2024-red)
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-app-FF4B4B?logo=streamlit&logoColor=white)
![LLaMA 3.1](https://img.shields.io/badge/Meta%20LLaMA-3.1-0467DF)
![Made for](https://img.shields.io/badge/Made%20for-grades%20K--8-brightgreen)

Pehla School is an AI-powered learning platform built at **HackMIT** to bridge the gap between rural and urban education. Students up to grade 8 get instant AI-generated lessons, quizzes with feedback, and access to real tutors — in **English and Hindi**.

---

## ✨ What it does

| Feature | Description |
|---|---|
| 🧠 **AI-Generated Lessons** | Type a topic, get an instant lesson with explanations and practice problems |
| 📝 **Assessments** | Take quizzes and receive immediate feedback with worked answers |
| 👩‍🏫 **Tutor Booking** | Book a session with a tutor for personalized help |
| 🌏 **Bilingual** | English + Hindi support to reach a wider audience |
| 🔐 **Auth** | Simple login for personalized sessions |

## ⚙️ How it works

- A **Streamlit** front end (`app.py`) drives the lesson, quiz, and booking flows.
- Lessons are generated in real time by **Meta LLaMA 3.1** through an LLM API.
- Math problems are served from `math_conversations.jsonl`, a curated conversation-style dataset.
- `convert.py` / `transform.py` / `filter_datasets.py` build and filter the dataset from Hugging Face `datasets` exports.

> **Note on data files:** `small_math_dataset.json` and `small_math_dataset_50.json` are **JSON Lines** (one JSON object per line) despite the `.json` extension — they're written by `datasets.Dataset.to_json()`. Parse them line-by-line, not with a single `json.load()`.

## 🚀 Getting started

```bash
git clone https://github.com/sinhaarya04/hackmit-pehla_school.git
cd hackmit-pehla_school
pip install -r requirements.txt

# add your LLM API key (not committed — see .gitignore)
echo 'TUNE_API_KEY=your-key-here' > s.env

streamlit run app.py
```

Open the local URL Streamlit prints (usually `http://localhost:8501`).

## 🛠 Tech stack

`Python` · `Streamlit` · `Meta LLaMA 3.1` · `Hugging Face datasets` · `requests`

## 🔮 Future ideas

- Expand subject coverage beyond math
- Mobile apps for iOS and Android
- Adaptive learning to personalize lesson difficulty

---

Built with ❤️ at HackMIT for students everywhere.
