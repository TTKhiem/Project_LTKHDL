# PhishGuardVN — Programming for Data Science Final Project



## 1. Cấu trúc

```text
Project_LTKHDL/
├── README.md
├── environment.yml
├── LLM_USAGE.md
├── .gitignore
├── data/
│   ├── raw/                  # CSV dùng cục bộ; không commit lên Git
│   └── processed/            # sản phẩm trung gian do nhóm tự tạo
├── notebooks/
│   ├── 01_collection_exploration.ipynb
│   ├── 02_analysis_q1_q2.ipynb
│   ├── 02_analysis_q3_q4.ipynb
│   ├── 02_analysis_q5.ipynb
│   └── 03_ml_question.ipynb
└── src/                      
```


## 2. Thành viên và phân công


| Thành viên | Tên | MSSV | Phần phụ trách chính |
|---|---|---|---|
| Thành viên 1 | `[tên]` | `[MSSV]` | Data source/Data Card; Q1, Q2 |
| Thành viên 2 | `[tên]` | `[MSSV]` | Data quality/preprocessing plan; Q3, Q4 |
| Thành viên 3 | `[tên]` | `[MSSV]` | Auxiliary data audit; Q5, Q6 (ML) |

Mỗi thành viên sở hữu đúng hai câu hỏi. Phân công chính không có nghĩa là các thành viên khác được miễn trách nhiệm hiểu toàn bộ repo.
## 3. Dataset và việc bắt buộc xác minh

| Vai trò | File | Ghi chú |
|---|---|---|
| Dataset chính | `data/raw/vn_compphish.csv` | Dùng cho phân tích và bài toán phân loại URL phishing/benign. |
| Dataset bổ trợ | `data/raw/abuse_type.csv` | Dùng cho Q5 kiểm toán độ nhất quán nhãn/metadata. |


## 4. Sáu câu hỏi nghiên cứu

Năm câu đầu là câu hỏi phân tích dữ liệu; Q6 là câu hỏi ML. 

| ID | Câu hỏi | Chủ sở hữu | Chiều sâu dự kiến |
|---|---|---|---|
| Q1 | Độ phức tạp cấu trúc URL có khác giữa phishing và benign khi so sánh trong các nhóm độ dài URL tương đương không? | Thành viên 1 | D3, D4, D5 |
| Q2 | Việc sử dụng HTTPS có liên quan đến khả năng URL mang nhãn phishing khác biệt như thế nào sau khi xét nhóm TLD và độ dài URL? | Thành viên 1 | D4, D5, D6 |
| Q3 | Mối liên hệ giữa TLD và nhãn phishing có thay đổi khi gộp TLD hiếm và so sánh trong các nhóm độ dài URL tương đương không? | Thành viên 2 | D3, D4, D6 |
| Q4 | Các hostname xuất hiện nhiều lần có tỷ lệ URL phishing khác hostname chỉ xuất hiện một lần không, và kết quả có thay đổi theo nhóm TLD không? | Thành viên 2 | D3, D4, D5 |
| Q5 | `abuse_type.csv` nhất quán đến đâu với nhãn trong dataset chính khi đối chiếu theo hostname, và kết quả thay đổi thế nào theo quy tắc chuẩn hóa/khử trùng lặp? | Thành viên 3 | D1, D5, D6 |
| Q6 (ML) | Có thể phân loại một URL thành phishing hoặc benign tại thời điểm nhận URL bằng các đặc trưng có sẵn hay không? | Thành viên 3 | Yêu cầu ML ở đề cương |

D1: kết hợp dữ liệu; D3: biến dẫn xuất; D4: kiểm soát yếu tố gây nhiễu; D5: định lượng bất định; D6: robustness check.

## 5. TODO theo notebook

### Notebook 01 — Collection & Exploration

- Thành viên 1: hoàn tất Data Card, provenance, license, collection method, related work.
- Thành viên 2: mô tả đơn vị quan sát, schema, kiểu dữ liệu, nhãn, split; kiểm tra missing, duplicate, outlier và giá trị bất thường.
- Thành viên 3: mô tả dataset bổ trợ và kiểm tra các vấn đề chất lượng/khả năng đối chiếu.
- Cả nhóm: thống nhất quyết định preprocessing; ghi số dòng trước/sau mỗi thao tác làm thay đổi dữ liệu và lý do, tổng kết 3–5 quan sát và các câu hỏi cần xác minh trước khi phân tích.

### Các notebook 02 — Analysis (Q1–Q5)

- `02_analysis_q1_q2.ipynb` — Thành viên 1: hoàn thành Q1 và Q2.
- `02_analysis_q3_q4.ipynb` — Thành viên 2: hoàn thành Q3 và Q4.
- `02_analysis_q5.ipynb` — Thành viên 3: hoàn thành Q5 và tổng hợp Q1–Q5 cho cả nhóm.
- Mỗi câu hỏi: mô tả preprocessing bằng Markdown; giải thích phương pháp; có ít nhất hai biểu đồ được gắn nhãn đầy đủ; trả lời bằng số liệu; nêu bất định/robustness theo thiết kế; thảo luận ý nghĩa và hạn chế.
- Sau mọi bước filter/merge/drop: ghi row count trước và sau.

### Notebook 03 — ML (Q6)

- Thành viên 3 thực hiện; hai thành viên còn lại review thiết kế và kiểm tra khả năng tái lập.
- Xác định người dùng, thời điểm dự đoán, target và feature hợp lệ tại thời điểm đó.
- Liệt kê cột bị loại và lý do leakage/identifier/không có sẵn tại prediction time.
- Xác minh split có sẵn và nguy cơ một hostname/domain xuất hiện ở nhiều partition; không tự chia lại dữ liệu nếu chưa có lý do được nhóm/giảng viên thống nhất.
- So sánh ít nhất hai mô hình và một trivial baseline.
- Đặt toàn bộ preprocessing trong scikit-learn Pipeline; tuning bằng cross-validation trên train.
- Chọn mô hình/ngưỡng bằng validation; chỉ đánh giá test một lần sau khi khóa quyết định.
- Chọn metric phù hợp mất cân bằng lớp; báo cáo kết quả, confusion matrix, phân tích lỗi và diễn giải mô hình.

### TODO trong `src` — viết module được tái sử dụng

- Notebook là nơi thực hiện và giải thích phân tích. Chỉ đưa vào `src` thao tác dùng chung thực sự; không chuyển câu trả lời, biểu đồ hay toàn bộ workflow của notebook thành module.
- **Thành viên 2 — `src/data_io.py`:** viết helper đọc CSV và kiểm tra dữ liệu cơ bản dùng lại được (ví dụ: kích thước, cột, missing values, duplicates). Không sửa dữ liệu raw; giữ các nhận xét và quyết định preprocessing trong notebook.
- **Thành viên 3 — `src/url_utils.py`:** viết helper trích xuất/chuẩn hóa URL và hostname dùng chung (ví dụ: HTTPS, TLD, đặc trưng cấu trúc và hostname). Ghi rõ quy tắc xử lý dữ liệu thiếu/không hợp lệ; không tự sửa nhãn hoặc đưa metadata bổ trợ vào feature ML.
Chỉ thêm helper khi có từ hai chỗ sử dụng trở lên; gọi và kiểm tra helper từ notebook liên quan, tránh tạo thêm module nếu chưa cần.

### Hoàn thiện chung
- Điền tên/MSSV tại README và các Markdown section được giao trong notebook.
- Chạy lại notebook theo thứ tự trên cùng một môi trường.
- Hoàn thiện phần findings, limitations, future work.
- Mỗi thành viên tự viết individual reflection.
- Cập nhật `LLM_USAGE.md` bằng các lần sử dụng LLM thực tế.
- Hoàn thiện `slides.pdf` để giải thích toàn bộ dự án.

## 6. Cài đặt môi trường

Tạo môi trường từ `environment.yml` bằng Conda, kích hoạt môi trường `phishguard-vn`. Mở repo tại thư mục gốc và chạy lần lượt các notebook: `01_collection_exploration.ipynb`, ba notebook phân tích Q1–Q5 theo thứ tự, rồi `03_ml_question.ipynb`.

## 7. Quy ước làm việc nhóm

- Không chỉnh sửa trực tiếp dữ liệu raw; giữ bản gốc bất biến.
- Mỗi thành viên commit những thay đổi mình thực hiện, với commit message mô tả rõ nội dung.
- Trước khi merge/push, chạy lại phần notebook mình phụ trách và kiểm tra `git diff`.
- Thống nhất người tích hợp cuối để tránh chỉnh sửa đồng thời cùng một notebook.
- Không đưa mật khẩu, token, dữ liệu cá nhân hoặc file dung lượng lớn lên GitHub.
