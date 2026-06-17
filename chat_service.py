import gradio as gr
import main_chat
gr.ChatInterface(
    fn=main_chat.chat_fn,
    title="ứng dụng với gradio",
    description="Nhập tên để cem kết quả",
    examples=["Python là gì","Gradio là gì"]

).launch(debug=False)
