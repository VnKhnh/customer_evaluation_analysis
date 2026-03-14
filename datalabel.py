import pandas as pd

# 1. Đọc file CSV của bạn
# Hãy đảm bảo file "shopee_reviews_labeled.csv" nằm cùng thư mục với file code này
try:
    df = pd.read_csv("D:/DataReviews/shopee_reviews_clean.csv")
except FileNotFoundError:
    print("Không tìm thấy file CSV. Vui lòng kiểm tra lại tên hoặc đường dẫn!")
    exit()

def label_by_keyword(comment):
    # Nếu bình luận bị trống (NaN)
    if pd.isna(comment):
        return "Khác / Không rõ"
        
    # Chuyển bình luận về chữ thường để dễ so sánh
    text = str(comment).lower()
    
    # 1. Hộp méo / sản phẩm hỏng / rò rỉ (Bổ sung: móp, dập, chảy, bung, dơ, xì...)
    if any(word in text for word in ["bể", "vỡ", "méo", "hỏng", "rò rỉ", "tràn", "đổ", "nát", "trầy", "xước", "chảy", "bung", "móp", "dập", "biến dạng", "lem", "toe toét", "xì", "dơ"]):
        return "Hộp méo / sản phẩm hỏng / rò rỉ"
        
    # 2. Thiếu hàng / sai sản phẩm (Bổ sung: giao lộn, sai mẫu, ko đúng mẫu, thiếu sót...)
    elif any(word in text for word in ["thiếu", "sai", "nhầm", "ko đúng", "không đúng", "giao lộn", "khác màu", "sai mẫu", "giao nhầm", "thiếu sót"]):
        return "Thiếu hàng / sai sản phẩm"
        
    # 3. Gây kích ứng da / breakout (Bổ sung: mẩn đỏ, nóng ran, châm chích, lên mụn...)
    elif any(word in text for word in ["nổi mẩn","kích ứng", "dị ứng", "ngứa", "nổi mụn", "rát", "châm chích", "đỏ", "mẩn đỏ", "lên mụn", "nóng ran", "cay mắt", "xót"]):
        return "Gây kích ứng da / breakout"
        
    # 4. Không giống mô tả / quảng cáo (Bổ sung: nhái, lừa đảo, khác hình, ko như hình...)
    elif any(word in text for word in ["không giống", "khác xa", "quảng cáo", "fake", "giả", "lừa", "treo đầu dê", "china", "nhái", "lừa đảo", "ko như hình", "khác hình", "pha ke", "chuẩn auth", "không chuẩn", "chông chênh","k giống","review","qc"]):
        return "Không giống mô tả / quảng cáo"
        
    # 5. Giao hàng chậm (Bổ sung: ngâm đơn, chờ mòn mỏi, giao hàng kém...)
    elif any(word in text for word in ["giao chậm", "lâu", "đợi mỏi", "ship chậm", "giao trễ", "ngâm đơn", "chờ mòn", "giao hàng quá lâu", "delay"]):
        return "Giao hàng chậm"
        
    # 6. Dịch vụ CSKH kém (Bổ sung: seen không rep, nhắn không trả lời, vô trách nhiệm, block...)
    elif any(word in text for word in ["thái độ", "trả lời", "tư vấn", "k xử lý", "không xử lý", "cẩu thả", "cskh", "nhắn ko rep", "không thèm", "vô trách nhiệm", "chặn", "block", "đổ lỗi", "seen", "im re, hỗ trợ, nhắn sh","hoàn hàng"]):
        return "Dịch vụ CSKH kém"
        
    # 7. Chất lượng sản phẩm kém (Bổ sung: bết, rít, lộ vân, nồng, hôi, loãng...)
    elif any(word in text for word in ["khô", "gãy", "dở", "chán", "kém", "mau trôi", "nhanh trôi", "vón cục", "lỏng", "tệ", "hắc", "hôi", "bết", "rít", "lộ vân", "không bám", "nồng", "loãng", "nhạt","không lên màu","ko lên màu","tô lên màu","bôi lên tím"]):
        return "Chất lượng sản phẩm kém"
        
    # 8. Giá cao không xứng (Bổ sung: tiếc tiền, chát, hút máu...)
    elif any(word in text for word in ["mắc", "đắt", "không đáng", "giá cao", "phí tiền", "tiếc tiền", "chát"]):
        return "Giá cao không xứng"
        
    # Nếu vẫn không khớp với bất kỳ từ khóa nào ở trên
    else:
        return "Khác / Không rõ"

# 3. Tạo cột 'reason' bằng cách áp dụng hàm trên cho cột 'comment'
print("Đang xử lý dữ liệu...")
df['reason'] = df['comment'].apply(label_by_keyword)

# 4. Lưu lại thành file mới
output_file = "D:/DataReviews/shopee_reviews_keyword_labeled3.csv"
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"Đã hoàn thành! File mới được lưu với tên: {output_file}")