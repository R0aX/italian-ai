# 🍝 The Unhinged Italian Chef

Welcome to the kitchen of the most passionate, loud, and slightly unhinged Italian chef you've ever met! This project uses **Gradio** and the **Groq API** (Llama 3) to bring a high-energy culinary assistant to your desktop.

![Alt text](italianai.png)

## 🤌 Features

- **Unhinged Personality:** Experience a system prompt designed to deliver maximum Italian intensity, hand gestures (🤌🤌🤌), and culinary wisdom.
- **Powered by Llama 3:** Uses the `llama-3.3-70b-versatile` model via Groq for lightning-fast, high-quality responses.
- **Gradio Interface:** A clean, user-friendly web UI featuring a soft theme, chat history, and quick-start examples.
- **High Energy:** The model is set to a high temperature (`1.3`) to ensure the chef stays unpredictable and vibrant.

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/unhinged-italian-chef.git](https://github.com/your-username/unhinged-italian-chef.git)
    cd unhinged-italian-chef
    ```

2.  **Install dependencies:**
    ```bash
    pip install gradio openai
    ```

3.  **Set up your API Key:**
    Inside the Python script, replace `"your_api_key"` with your actual Groq API key:
    ```python
    client = OpenAI(
        base_url="[https://api.groq.com/openai/v1](https://api.groq.com/openai/v1)",
        api_key="YOUR_GROQ_API_KEY" 
    )
    ```

## 🚀 Usage

Run the script to launch the local web server:

```bash
python your_script_name.py
