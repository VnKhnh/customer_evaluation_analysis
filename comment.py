import csv
import re
from datetime import datetime


INPUT_FILE  = "D:/DataReviews/shopee-vn-2026-03-13.csv"
OUTPUT_FILE = "D:/DataReviews/shopee_reviews_clean.csv"


def parse_date(raw_date: str) -> str:
    """
    Trích datetime từ cột 'date'.
    """
    if not raw_date:
        return ""
    date_part = raw_date.split("|")[0].strip()
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            return datetime.strptime(date_part, fmt).strftime("%Y-%m-%d %H:%M")
        except ValueError:
            continue
    return date_part


def parse_variant(data6: str) -> str:
    """
    Trích tên variant từ cột 'data6'.
    """
    if not data6:
        return ""
    prefix = "Phân loại hàng:"
    if data6.startswith(prefix):
        return data6[len(prefix):].strip()
    return data6.strip()


def clean_comment(comment: str) -> str:
    """
    Xoá khoảng trắng đầu/cuối và gộp các dòng (xóa ký tự xuống dòng).
    """
    if not comment:
        return ""
    # Thay thế các ký tự xuống dòng (\n, \r, \t) và khoảng trắng liên tiếp thành 1 dấu cách
    cleaned = re.sub(r'\s+', ' ', comment)
    return cleaned.strip()


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------

def process(input_path: str, output_path: str) -> None:
    reviews = []
    
    # Các biến thống kê để theo dõi số lượng dòng bị loại bỏ
    skipped_empty_id_count = 0
    skipped_no_comment_count = 0
    skipped_duplicate_count = 0
    
    # Bộ nhớ lưu trữ các comment đã xuất hiện để check trùng lặp
    seen_comments = set()

    with open(input_path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            order_id = row.get("web_scraper_order", "").strip()
            
            # 1. Bỏ qua những dòng không có ID
            if not order_id:
                skipped_empty_id_count += 1
                continue

            raw_date   = row.get("date", "").strip()
            raw_variant = row.get("data6", "").strip()
            raw_product = row.get("data7", "").strip()
            raw_comment = row.get("comment", "").strip()

            # 2. Xử lý gộp dòng cho comment
            final_comment = clean_comment(raw_comment)

            # 3. Bỏ qua những dòng KHÔNG CÓ nội dung comment
            if not final_comment:
                skipped_no_comment_count += 1
                continue

            # 4. Lọc bỏ các comment bị trùng lặp
            if final_comment in seen_comments:
                skipped_duplicate_count += 1
                continue
            
            # Thêm vào bộ nhớ để check trùng cho các dòng sau
            seen_comments.add(final_comment)

            reviews.append({
                "web_scraper_order": order_id,
                "product":    raw_product,
                "variant":    parse_variant(raw_variant),
                "comment":    final_comment,
                "created_at": parse_date(raw_date),
            })

    # Ghi file đầu ra
    fieldnames = ["web_scraper_order", "product", "variant", "comment", "created_at"]
    with open(output_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reviews)

    # -----------------------------------------------------------------------
    # Thống kê nhanh
    # -----------------------------------------------------------------------
    total = len(reviews)
    if total == 0:
        print("Không có dữ liệu hợp lệ nào để lưu!")
        return

    has_product  = sum(1 for r in reviews if r["product"])
    has_variant  = sum(1 for r in reviews if r["variant"])

    from collections import Counter
    product_counts = Counter(r["product"] for r in reviews if r["product"])
    top_products   = product_counts.most_common(5)

    print("=" * 60)
    print("✅  XỬ LÝ HOÀN TẤT")
    print("=" * 60)
    print(f"  Tổng đánh giá giữ lại (đã làm sạch) : {total:,}")
    print(f"  Số dòng thiếu ID bị xóa            : {skipped_empty_id_count:,}")
    print(f"  Số dòng không có comment bị xóa    : {skipped_no_comment_count:,}")
    print(f"  Số comment trùng bị xóa            : {skipped_duplicate_count:,}")
    print(f"  Có thông tin sản phẩm              : {has_product:,}")
    print(f"  Có thông tin variant               : {has_variant:,}")
    print()
    print("  Top 5 sản phẩm được đánh giá nhiều nhất (trong data giữ lại):")
    for i, (name, cnt) in enumerate(top_products, 1):
        short = (name[:55] + "…") if len(name) > 56 else name
        print(f"    {i}. {short:<57} ({cnt} đánh giá)")
    print()
    print(f"  📄  File đầu ra: {output_path}")
    print("=" * 60)


if __name__ == "__main__":
    process(INPUT_FILE, OUTPUT_FILE)