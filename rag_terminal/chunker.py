import tiktoken
def chunk_by_token(text, chunk_size=400, overlap=0):
    """
    Chia văn bản thành các đoạn dựa trên số lượng token.

    Args:
        text (str): Văn bản cần chia.
        chunk_size (int): Số lượng token tối đa trong mỗi đoạn.
        overlap (int): Số lượng token chồng lấn giữa các đoạn.

    Returns:
        List[str]: Danh sách các đoạn văn bản.
    """
    # Khởi tạo bộ mã hóa token
    encoding = tiktoken.get_encoding("cl100k_base")
    
    # Mã hóa văn bản thành danh sách token
    tokens = encoding.encode(text)
    
    chunks = []
    start = 0
    while start < len(tokens):
        end = min(start + chunk_size, len(tokens))
        chunk_tokens = tokens[start:end]
        chunk_text = encoding.decode(chunk_tokens)
        chunks.append(chunk_text)
        
        # Cập nhật vị trí bắt đầu cho đoạn tiếp theo, với chồng lấn
        start += chunk_size - overlap
    
    return chunks