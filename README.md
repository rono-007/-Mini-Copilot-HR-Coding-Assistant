# 🤖 Mini Copilot – HR & Coding Assistant

A smart, interactive assistant built using **Streamlit** and **Hugging Face Inference API**, designed to help with:

* 💼 HR tasks like interview tips, email writing, and candidate screening
* 👨‍💻 Python coding help, debugging, and code explanations

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mini-copilot-hr-coding-assistant.streamlit.app/)

---

## 🚀 Features

* ✅ ChatGPT-style interface with role avatars
* ✅ Role-based assistant: HR or Coding
* ✅ Upload `.py` or `.txt` files for analysis
* ✅ Copyable code outputs & markdown support
* ✅ Clear chat button
* ✅ Powered by Zephyr via Hugging Face API

---

## 💠 Installation

```bash
git clone https://github.com/rono-007/-Mini-Copilot-HR-Coding-Assistant.git
cd -Mini-Copilot-HR-Coding-Assistant
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🔐 Hugging Face API Setup

Create a file `.streamlit/secrets.toml` and add your token:

```toml
HUGGINGFACEHUB_API_TOKEN = "your_hf_token_here"
```

Get your token from [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

## 📦 Dependencies

* `streamlit`
* `huggingface_hub`

---

## 👨‍💻 Author

* **Ranajoy Nag** – [@rono-007](https://github.com/rono-007)

---

## 📄 License

This project is under MIT license
