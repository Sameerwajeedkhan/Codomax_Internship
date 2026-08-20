# Module 5 — AI Tools & Mini Project

## Project: AI Code Explainer

This project was created for Module 5 (Day 17–Day 20): **AI Tools & Mini Project**.

### Objective

Build a simple AI-powered application that helps students and developers:

- Understand source code
- Find and fix bugs
- Improve code
- Understand time and space complexity
- Explore alternative solutions

### AI Tool Used

The application uses the **Google Gemini API** through the current `google-genai` Python SDK and a Streamlit interface.

### Technologies

- Python
- Streamlit
- Google Gemini API
- `google-genai`

## Features

1. Enter a Gemini API key securely in the Streamlit sidebar.
2. Select the programming language.
3. Select an AI task.
4. Paste source code.
5. Ask Gemini to analyze the code.
6. View an easy-to-understand response.

## Project Structure

```text
Module5_AI_Tools_Mini_Project/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Open PowerShell in this project folder:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```powershell
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## API Key

For this learning project, the UI accepts the Gemini API key at runtime so it does not need to be hard-coded into the source code.

Never commit an API key to GitHub.

For production applications, use environment variables or a secure secrets manager.

## Example

Paste:

```python
def add(a, b):
    return a - b

print(add(5, 2))
```

Choose **Find and fix bugs**.

The AI should identify that subtraction is being used instead of addition and suggest a corrected implementation.

## Learning Outcomes

### AI Tools Explored

**ChatGPT**
- Coding assistance
- Debugging
- Learning concepts
- Brainstorming
- Documentation and writing

**Google Gemini**
- Code explanation
- Generative AI API
- AI-powered application development
- Research and multimodal capabilities

**Microsoft Copilot**
- Coding assistance
- Productivity support
- Developer workflow assistance

### Responsible AI Usage

AI-generated code should be reviewed and tested. AI can produce incorrect, incomplete, outdated, or insecure suggestions. The developer remains responsible for the final code.

## Module 5 Completion

- [x] Explored AI tools
- [x] Learned how AI can assist coding
- [x] Learned how AI can assist research and productivity
- [x] Built an AI-powered mini project
- [x] Prepared GitHub repository structure
- [ ] Publish repository to GitHub
- [ ] Publish learning journey on LinkedIn

## Official References

Google Gemini API documentation:
https://ai.google.dev/gemini-api/docs

Google Gemini API key documentation:
https://ai.google.dev/gemini-api/docs/api-key
