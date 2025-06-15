import streamlit as st
from huggingface_hub import InferenceClient
# Hugging Face API Token (keep it secure!)

# Connect to Zephyr hosted model
client = InferenceClient(
    model="HuggingFaceH4/zephyr-7b-beta",
    token=st.secrets["HUGGINGFACEHUB_API_TOKEN"]
)

# Prompt builder
def build_prompt(role, user_input):
    if role == "hr":
        system_prompt = "You are an expert HR assistant. Help with interview tips, candidate screening, and email writing."
    else:
        system_prompt = "You are an expert Python coding assistant. Help write, debug, and explain code."

    return f"<|system|>\n{system_prompt}\n<|user|>\n{user_input}\n<|assistant|>"

# Streamlit UI
st.set_page_config(page_title="Mini Copilot", layout="centered")
st.title("🤖 Mini Copilot – HR & Coding Assistant")

# Sidebar: Role selection
role = st.sidebar.radio("Choose your assistant role:", ("HR Assistant", "Coding Assistant"))
role_key = "hr" if role == "HR Assistant" else "code"

# User input
user_input = st.text_area("Enter your query:", height=150)

# Submit button
if st.button("Generate Response"):
    if user_input.strip() == "":
        st.warning("Please enter a query.")
    else:
        with st.spinner("Generating response..."):
            try:
                prompt = build_prompt(role_key, user_input)
                response = client.text_generation(prompt, max_new_tokens=500, temperature=0.7)
                st.text_area("Response", response.strip(), height=300)
            except Exception as e:
                st.error(f"❌ Error: {e}")
