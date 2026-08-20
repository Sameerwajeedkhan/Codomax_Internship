import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Code Explainer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Code Explainer")
st.caption("Module 5 Mini Project — AI Tools & Productivity")

st.sidebar.header("Settings")
api_key = st.sidebar.text_input(
    "Gemini API Key",
    type="password",
    help="Your key is used only for the current Streamlit session."
)

language = st.sidebar.selectbox(
    "Programming Language",
    ["Python", "Java", "JavaScript", "C", "C++", "Other"]
)

task = st.sidebar.selectbox(
    "AI Task",
    [
        "Explain the code",
        "Find and fix bugs",
        "Improve the code",
        "Give time and space complexity",
        "Suggest an alternative solution"
    ]
)

default_code = """def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
"""

code = st.text_area(
    "Paste your code",
    value=default_code,
    height=300
)

if st.button("🚀 Analyze Code", type="primary"):
    if not api_key.strip():
        st.error("Please enter your Gemini API key in the sidebar.")
        st.stop()

    if not code.strip():
        st.warning("Please paste some code first.")
        st.stop()

    prompt = f"""
You are an expert programming tutor.

Programming language: {language}
Requested task: {task}

Analyze the following code:

```{language.lower()}
{code}
```

Give a beginner-friendly answer.
If there is a bug, clearly identify it and provide corrected code.
For complexity, state time complexity and space complexity with a short reason.
Use headings and code blocks where useful.
Do not invent execution results.
"""

    try:
        client = genai.Client(api_key=api_key.strip())
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        st.subheader("AI Analysis")
        st.markdown(response.text)

    except Exception as exc:
        st.error("The AI request failed.")
        st.code(str(exc))

st.divider()
st.info(
    "Learning note: AI tools should assist your understanding. "
    "Review, test, and verify generated code before using it."
)
