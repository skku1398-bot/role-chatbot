import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Role-based Creative Chatbot", page_icon="🎭", layout="wide")

ROLES = {
    "🩺 Medical Advisor": {
        "system": (
            "You are a medical advisor and clinical specialist. Provide structured, "
            "evidence-based health information and physiological explanations. Always "
            "include a polite reminder that your advice is for informational purposes "
            "and does not replace professional medical diagnosis."
        ),
        "hint": "Think like a clinician: analyze symptoms, biological mechanisms, and health guidance.",
        "placeholder": "e.g., What physiological factors cause chronic fatigue?",
    },
    "⚖️ Legal Advisor": {
        "system": (
            "You are a legal advisor and legal analyst. Provide clear explanations of "
            "legal concepts, rights, obligations, and analytical frameworks. Always "
            "add a brief note that this does not constitute formal legal counsel."
        ),
        "hint": "Think like a legal expert: analyze rules, contracts, and precedents.",
        "placeholder": "e.g., What are the basic copyright principles for digital artworks?",
    },
    "🔮 Fortune Teller": {
        "system": (
            "You are a mystical and insightful fortune teller. Answer with symbolic metaphors, "
            "arcane imagery, cryptic wisdom, and intuitive readings. Interpret questions through "
            "the lens of fate, hidden patterns, and future possibilities."
        ),
        "hint": "Think like a mystic: read the symbols, cards, and hidden patterns of fate.",
        "placeholder": "e.g., What does my creative future hold for the next project?",
    },
    "🏛️ Historian": {
        "system": (
            "You are a meticulous historian and archivist. Answer by connecting current ideas "
            "to historical precedents, cultural eras, and long-term societal shifts. Provide "
            "context from past centuries."
        ),
        "hint": "Think like a historian: look for echoes of the past in current patterns.",
        "placeholder": "e.g., How have artists historically reacted during times of great transition?",
    },
    "🦉 Philosopher": {
        "system": (
            "You are a profound philosopher and ethicist. Answer by exploring existential questions, "
            "moral frameworks, and the deeper meaning behind human actions. Use historical "
            "philosophical concepts to frame your advice."
        ),
        "hint": "Think like a philosopher: question the core assumptions and seek deep meaning.",
        "placeholder": "e.g., Is true originality possible in modern creative work?",
    },
}

with st.sidebar:
    st.subheader("🔑 API & Role Settings")
    api_key = st.text_input("Enter your OpenAI API Key:", type="password", placeholder="sk-xxxxxxxxxxxxxxxxx")
    role_name = st.selectbox("Choose a role:", list(ROLES.keys()))
    st.info(ROLES[role_name]["hint"])
    model = st.selectbox("Model:", ["gpt-4o-mini", "gpt-4o"], index=0)

st.title("🎭 Role-based Creative Chatbot")
st.write("Select a creative role and ask your question!")

question = st.text_area(
    "💬 Enter your question or idea:",
    placeholder=ROLES[role_name]["placeholder"],
)

if st.button("Generate Response"):
    if not api_key:
        st.warning("Please enter your OpenAI API key in the sidebar.")
    elif not question.strip():
        st.warning("Please enter a question or idea.")
    else:
        try:
            client = OpenAI(api_key=api_key)
            with st.spinner("Thinking..."):
                resp = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": ROLES[role_name]["system"]},
                        {"role": "user", "content": question},
                    ],
                    temperature=0.8,
                )
            st.markdown(f"### {role_name}")
            st.write(resp.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")

st.divider()
st.caption("Built for 'Art & Advanced Big Data' • Prof. Jahwan Koo (SKKU)")
