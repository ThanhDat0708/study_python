import os
import shutil
import gradio as gr
from loader import txt_loader
from chunker import chunk_by_token
from chromaDB_service import (
    add_documents, search, delete_collection,
    get_sources, delete_documents_by_source
)
from openai_service import get_response

DEFAULT_COLLECTION = "noi_quy_abc"
UPLOAD_DIR = "uploaded_documents"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def respond(message, history, collection_name):
    sources = get_sources(collection_name)
    if not sources:
        return "Chưa có tài liệu nào được nạp. Vui lòng vào tab 'Quản lý tài liệu' để upload trước."
    results = search(collection_name, message, n_results=5)
    context = "\n\n".join(results["documents"][0])
    augmented_query = f"Dựa trên thông tin sau:\n{context}\n\nTrả lời câu hỏi: {message}"
    chat_history = []
    for user_msg, assistant_msg in history:
        chat_history.append({"role": "user", "content": user_msg})
        if assistant_msg:
            chat_history.append({"role": "assistant", "content": assistant_msg})
    answer = get_response(augmented_query, chat_history)
    return answer


def upload_and_load(file, collection_name):
    if file is None:
        return "Vui lòng chọn file.", None
    original_name = file.orig_name if hasattr(file, 'orig_name') else os.path.basename(file.name)
    dest_path = os.path.join(UPLOAD_DIR, original_name)
    shutil.copy(file.name, dest_path)
    try:
        content = txt_loader(dest_path)
    except Exception as e:
        return f"Lỗi đọc file: {str(e)}", None
    chunks = chunk_by_token(content)
    ids = [f"{original_name}_{i}" for i in range(len(chunks))]
    metadatas = [{"source": original_name} for _ in chunks]
    try:
        add_documents(collection_name, ids, chunks, metadatas)
    except Exception as e:
        return f"Lỗi khi nạp vào ChromaDB: {str(e)}", None
    return f"Đã nạp {len(chunks)} đoạn từ '{original_name}' vào collection '{collection_name}'.", None


def refresh_sources(collection_name):
    sources = get_sources(collection_name)
    if not sources:
        return "Chưa có tài liệu nào."
    return "\n".join(f"- {s}" for s in sources)


def delete_source(source, collection_name):
    if not source.strip():
        return "Vui lòng nhập tên nguồn cần xoá."
    try:
        delete_documents_by_source(collection_name, source.strip())
        return f"Đã xoá tất cả chunks từ '{source.strip()}'."
    except Exception as e:
        return f"Lỗi: {str(e)}"


def clear_all(collection_name):
    try:
        delete_collection(collection_name)
        return f"Đã xoá collection '{collection_name}'."
    except Exception as e:
        return f"Lỗi: {str(e)}"


with gr.Blocks(title="RAG Web UI", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# RAG Web UI - Hệ thống hỏi đáp thông minh")
    collection_state = gr.State(DEFAULT_COLLECTION)

    with gr.Tab("Chat"):
        gr.ChatInterface(
            fn=respond,
            additional_inputs=[collection_state],
            title="Hỏi đáp về tài liệu",
            description="Nhập câu hỏi. Hệ thống tìm kiếm trong tài liệu đã nạp và trả lời.",
        )

    with gr.Tab("Quản lý tài liệu"):
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### Upload tài liệu")
                file_input = gr.File(label="Chọn file .txt", file_types=[".txt"])
                collection_input = gr.Textbox(label="Collection name", value=DEFAULT_COLLECTION)
                upload_btn = gr.Button("Nạp vào ChromaDB", variant="primary")
                upload_status = gr.Textbox(label="Trạng thái", interactive=False)
            with gr.Column(scale=1):
                gr.Markdown("### Danh sách tài liệu đã nạp")
                refresh_btn = gr.Button("Làm mới")
                sources_display = gr.Textbox(label="Các nguồn tài liệu", interactive=False, lines=6)
                gr.Markdown("### Xoá tài liệu")
                source_to_delete = gr.Textbox(label="Tên nguồn cần xoá")
                delete_btn = gr.Button("Xoá nguồn", variant="secondary")
                delete_status = gr.Textbox(label="Trạng thái", interactive=False)
                clear_btn = gr.Button("Xoá toàn bộ collection", variant="stop")
                clear_status = gr.Textbox(label="Trạng thái", interactive=False)

    upload_btn.click(
        fn=upload_and_load,
        inputs=[file_input, collection_input],
        outputs=[upload_status, file_input]
    )
    refresh_btn.click(
        fn=refresh_sources,
        inputs=[collection_input],
        outputs=[sources_display]
    )
    delete_btn.click(
        fn=delete_source,
        inputs=[source_to_delete, collection_input],
        outputs=[delete_status]
    )
    clear_btn.click(
        fn=clear_all,
        inputs=[collection_input],
        outputs=[clear_status]
    )

if __name__ == "__main__":
    demo.launch()
