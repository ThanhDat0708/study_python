import gradio as gr

def hello(name:str,yob:int, gender:str) -> str:
    return f"xin chào {name},giới tính{gender},năm nay{2026-yob} tuổi"

gr.Interface(
    fn=hello,
    inputs=[gr.Textbox(label="Nhập Tên"),
            gr.Number(label="Năm Sinh",minimum=1990, value=2000),
            gr.Dropdown(label="Giới Tính", choices=["Nam","Nữ","Khác"]),
            ],
    outputs=gr.Textbox(label="Kết Quả"),

    title="Ứng dụng web với Gradio",
    description="Nhập tên để xem kết quả"
).launch(debug=False)

