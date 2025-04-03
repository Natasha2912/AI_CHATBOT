import gradio as gr
import requests

API_URL = "http://127.0.0.1:9999/chat"

def chatbot(message, model_name, provider, allow_search):
    request_payload = {
        "model_name": model_name,
        "model_provider": provider,
        "system_prompt": "Act as an AI chatbot who is smart and friendly",
        "messages": [message],
        "allow_search": allow_search,
    }
    response = requests.post(API_URL, json=request_payload)
    return response.json()

iface = gr.Interface(
    fn=chatbot,
    inputs=[
        gr.Textbox(label="Your Message"),
        gr.Dropdown(choices=["llama-3.3-70b-versatile", "gemini-1.5-pro-latest"], label="Select Model"),
        gr.Dropdown(choices=["Groq", "Google"], label="Model Provider"),
        gr.Checkbox(label="Enable Web Search"),
    ],
    outputs="text",
    title="AI Chatbot",
    live=True,
)

iface.launch()

