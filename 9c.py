import openai
import gradio
openai.api_key = "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"
messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.Chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "INTELLIGENT CHATBOT")
demo.launch(share=True)
