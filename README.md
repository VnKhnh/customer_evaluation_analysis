# Phân Tích Dữ Liệu Đánh Giá E-commerce: Nhận Diện Vấn Đề & Tối Ưu Hóa Sản Phẩm

##  Tổng Quan Dự Án
Dự án này tập trung vào việc phân tích hàng ngàn đánh giá của khách hàng trên nền tảng Shopee (ngành hàng mỹ phẩm/son môi 3CE) nhằm tìm ra nguyên nhân cốt lõi khiến khách hàng không hài lòng. 


##  Phân Tích Dữ Liệu & Insight

### 1. Biểu đồ Tổng quan các nguyên nhân lỗi (Bar Chart)
(Tham khảo ảnh: `img/bieu_do_1_tong_quan_loi.png`)

**Phân tích:**
* Biểu đồ cột cho thấy sự phân bổ của tất cả các nhãn. Nhóm **"Khác / Không rõ"** chiếm tỷ trọng lớn nhất, điều này là bình thường vì nó có thể chứa các bình luận bâng quơ không chứa từ khóa lỗi.
* Khi nhìn vào các nhóm lỗi cụ thể, các vấn đề nổi cộm nhất thường tập trung vào: **"Chất lượng sản phẩm kém"** (khô, gãy, mau trôi) và **"Không giống mô tả / quảng cáo"** (nghi ngờ hàng giả, tem nhãn Made in China).
* Lỗi liên quan đến **"Hộp méo / rò rỉ"** và **"Dịch vụ CSKH kém"** cũng chiếm tỷ lệ đáng kể, cho thấy quy trình đóng gói và hậu mãi đang có lỗ hổng.

**Insight:** Khách hàng mỹ phẩm cực kỳ nhạy cảm với trải nghiệm sử dụng (chất son) và tính xác thực của sản phẩm (nguồn gốc). Lỗi vận chuyển (hộp méo) dù không do hãng trực tiếp gây ra nhưng vẫn bị tính vào trải nghiệm tồi tệ.

### 2. Biểu đồ "Điểm mù" lỗi trên Top 5 Sản phẩm (Heatmap)
(Tham khảo ảnh: `img/bieu_do_2_heatmap_san_pham.png`)

**Phân tích:**
* Biểu đồ nhiệt (Heatmap) giúp chúng ta "bắt bệnh" chéo giữa Tên sản phẩm và Nguyên nhân lỗi.
* *Ví dụ từ dữ liệu:* Các dòng son thỏi (như *3CE Blur Matte Lipstick* hay *Sketch Stick*) có xu hướng bị phàn nàn nhiều về việc **"Chất lượng sản phẩm kém"** (cụ thể là gãy son, chất son khô rít).
* Trong khi đó, các dòng son kem/tint (như *Blur Water Tint* hay *Velvet Lip Tint*) lại vướng nhiều vào khiếu nại **"Hộp méo / Rò rỉ"** (tràn son, lem nhem) và **"Không giống mô tả"** (nghi ngờ hàng Fake do thay đổi tem mác).

**Insight:** Mỗi định dạng sản phẩm (Texture) đang gặp một điểm yếu riêng biệt về mặt vật lý. Không có một lỗi hệ thống chung cho toàn bộ, mà R&D cần can thiệp cục bộ vào từng mã hàng.

### 3. Biểu đồ Xu hướng lỗi theo thời gian (Line Chart)
(Tham khảo ảnh: `img/bieu_do_3_xu_huong_thoi_gian.png`)

**Phân tích:**
* Biểu đồ đường cho thấy sự biến động của các khiếu nại theo từng tháng.
* Thường có những biến động tăng vọt vào các tháng có Mega Sale (Ví dụ: Tháng 11 - 11/11, Tháng 12 - 12/12, hoặc dịp lễ 8/3).
* Trong các giai đoạn này, đường biểu diễn của **"Giao hàng chậm"**, **"Dịch vụ CSKH kém"** và **"Hộp méo / hỏng"** thường dựng đứng lên. Lý do là lượng đơn hàng quá tải dẫn đến kho đóng gói cẩu thả, đơn vị vận chuyển ném hàng, và nhân viên CSKH không kịp phản hồi.

**Insight:** Sự suy giảm chất lượng dịch vụ có tính chu kỳ và hoàn toàn có thể dự báo trước dựa vào lịch khuyến mãi của sàn thương mại điện tử.


## Đề Xuất Giải Pháp Trọng Tâm (Actionable Solutions)

Dựa trên các phân tích trên, dưới đây là kế hoạch hành động đề xuất cho các phòng ban:

### 1. Dành cho R&D (Nghiên cứu & Phát triển) và Sản xuất
* **Sự cố Son thỏi gãy/khô:** Cần xem xét lại công thức sáp (wax formula) của dòng Blur Matte/Sketch Stick. Có thể do nhiệt độ bảo quản tại kho Việt Nam cao hơn Hàn Quốc khiến kết cấu son bị ảnh hưởng. Cần tăng cường độ liên kết của lõi son.
* **Sự cố Son kem rò rỉ:** Thay đổi thiết kế nút chặn (stopper) ở cổ lọ son cho dòng Water Tint/Velvet Lip Tint để chống trào khi áp suất hoặc nhiệt độ thay đổi trong quá trình vận chuyển.

### 2. Dành cho Packaging & Marketing (Bao bì & Truyền thông)
* **Xử lý khủng hoảng "Hàng Fake/Made in China":** Khách hàng đang thiếu thông tin. Marketing cần cập nhật rõ ràng trên mô tả sản phẩm (Product Description) và ảnh Banner về việc hãng có nhà máy gia công tại Trung Quốc, cũng như cập nhật hình ảnh các mẫu tem nhãn/bao bì mới nhất để tránh hiểu lầm.

### 3. Dành cho Operation & Logistics (Vận hành & Kho bãi)
* **Tối ưu đóng gói:** Nâng cấp từ hộp carton mỏng sang hộp nắp gài cứng cáp hơn, sử dụng màng xốp hơi (bubble wrap) 2 lớp cho các sản phẩm dễ rò rỉ.
* **Chuẩn bị cho mùa Mega Sale:**
  * Thuê thêm nhân sự thời vụ cho kho bãi trước các đợt sale lớn (11/11, 12/12) để giảm tải, tránh đóng gói sai/thiếu hàng.
  * Triển khai Chatbot AI để xử lý các câu hỏi lặp lại (hỏi mã vận đơn, hỏi thời gian giao hàng) nhằm giảm tải cho nhân sự CSKH.


## 🛠 Hướng Dẫn Cài Đặt & Chạy Code

Dự án sử dụng Python để gán nhãn dữ liệu (Keyword matching) và trực quan hóa (Data Visualization).

**1. Cài đặt các thư viện cần thiết:**
```bash
pip install pandas matplotlib seaborn
