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

# Configure Streamlit page
st.set_page_config(page_title="Mini Copilot", layout="centered")
st.title("🤖 Mini Copilot – HR & Coding Assistant")

# Sidebar role selector
role = st.sidebar.radio("Choose your assistant role:", ("HR Assistant", "Coding Assistant"))
role_key = "hr" if role == "HR Assistant" else "code"
assistant_avatar = "🧑‍💼" if role_key == "hr" else "👨‍💻"
user_avatar = "🙋"

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 🔘 CLEAR CHAT BUTTON ---
if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# --- 📎 FILE UPLOAD ---
uploaded_file = st.sidebar.file_uploader("📎 Upload a .txt or .py file", type=["txt", "py"])
file_content = ""
if uploaded_file:
    file_content = uploaded_file.read().decode("utf-8")
    st.sidebar.success("File uploaded successfully.")

# --- INPUT AREA ---
with st.chat_message("user", avatar=user_avatar):
    user_input = st.text_area(
        "Ask something...",
        placeholder="e.g., Summarize this code / Suggest interview questions",
        key="input_box",
        height=150
    )

# --- HANDLE INPUT & GENERATE RESPONSE ---
if st.button("Generate Response"):
    if not user_input.strip():
        st.warning("Please enter a query.")
    else:
        full_input = f"{user_input}\n\nFile content:\n{file_content}" if file_content else user_input
        st.session_state.messages.append({"role": "user", "content": full_input})

        with st.chat_message("assistant", avatar=assistant_avatar):
            with st.spinner("Thinking..."):
                try:
                    prompt = build_prompt(role_key, full_input)
                    raw_response = client.text_generation(prompt, max_new_tokens=500, temperature=0.7)
                    response = raw_response.strip()
                except Exception as e:
                    response = f"❌ Error: {e}"

            # Markdown with code copy buttons
            st.markdown(response, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- DISPLAY CHAT HISTORY ---
for msg in st.session_state.messages:
    avatar = user_avatar if msg["role"] == "user" else assistant_avatar
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"], unsafe_allow_html=True)

# Inject JavaScript for copy button (works for <pre><code>)
st.markdown("""
<style>
.copy-btn {
    position: absolute;
    top: 6px;
    right: 12px;
    background: #eee;
    border: none;
    padding: 2px 6px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 12px;
}
.code-block {
    position: relative;
}
</style>
<script>
function copyCode(btn) {
    const code = btn.parentElement.querySelector("code").innerText;
    navigator.clipboard.writeText(code).then(() => {
        btn.innerText = "✅ Copied";
        setTimeout(() => btn.innerText = "📋 Copy", 2000);
    });
}
window.addEventListener("load", () => {
    document.querySelectorAll("pre").forEach(block => {
        const btn = document.createElement("button");
        btn.innerText = "📋 Copy";
        btn.className = "copy-btn";
        btn.onclick = () => copyCode(btn);
        const wrapper = document.createElement("div");
        wrapper.className = "code-block";
        block.parentNode.replaceChild(wrapper, block);
        wrapper.appendChild(block);
        wrapper.appendChild(btn);
    });
});
</script>
""", unsafe_allow_html=True)
