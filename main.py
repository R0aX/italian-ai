import gradio as gr
from openai import OpenAI
import os

# --- SETUP ---
# It is highly recommended to use an environment variable for your key
# For now, replace "YOUR_GROQ_API_KEY" with your actual key
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="your_api_key" 
)

SYSTEM_PROMPT = (
    "You are a cooking assistant. You talk like an unhinged Italian chef. "
    "Use plenty of hand gestures (in text), passion, and culinary intensity."
)

def chat_with_chef(message, history):
    """
    Gradio passes the current message and the chat history (as a list of pairs).
    """
    # Prepare the messages for the API
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    # Reconstruct history for the model
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    
    # Add the newest user message
    messages.append({"role": "user", "content": message})

    try:
        # High temperature for that 'passionate' Italian chef energy
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=1.3 
        )

        ai_reply = response.choices[0].message.content
        return ai_reply
        
    except Exception as e:
        return f"MAMMA MIA! THE STOVE IS ON FIRE: {e}"

# --- GRADIO UI ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🍝 The Unhinged Italian Chef")
    gr.Markdown("Step into my kitchen! But don't you dare overcook the pasta!")
    
    chatbot = gr.ChatInterface(
        fn=chat_with_chef,
        examples=["How do I make carbonara?", "Can I put pineapple on pizza?", "Teach me to toss dough!"],
        title="Chef's Kitchen",
    )

if __name__ == "__main__":
    demo.launch()
