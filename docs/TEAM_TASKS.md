# Phân công công việc nhóm 3 người

## Thành viên 1 — Data audit, EDA và liên kết dataset

**Notebook:** `notebooks/01_data_audit_and_join.ipynb`

Nhiệm vụ:
- Xác minh schema, kiểu dữ liệu, missing values, duplicate và phân bố nhãn/split/tier.
- Đánh giá các feature và các nguy cơ leakage trước khi mô hình hóa.
- Thiết kế, triển khai và kiểm tra khóa chuẩn hóa URL dùng chung.
- Ghép `abuse_type.csv` với các dòng phishing từ `vn_compphish.csv`; kiểm tra cardinality, nhãn thiếu/trùng và sự nhất quán của split.
- Ghi lại những phát hiện chính và đề xuất cho Thành viên 2/3.

Bàn giao: notebook hoàn chỉnh, bảng/biểu đồ audit cần thiết và mô tả quy tắc ghép dữ liệu trong báo cáo.

## Thành viên 2 — Binary phishing classification

**Notebook:** `notebooks/02_binary_phishing_classifier.ipynb`

Nhiệm vụ:
- Tạo pipeline dựa trên train/val có sẵn; không tự chia lại dữ liệu nếu chưa được nhóm thống nhất.
- Lựa chọn và giải thích feature; không dùng `label` hoặc `split` làm đầu vào. Kiểm tra ý nghĩa của `tier` trước khi quyết định giữ hay loại.
- So sánh baseline với một hoặc nhiều mô hình phù hợp, chọn mô hình trên validation.
- Chỉ dùng test cho đánh giá cuối cùng; báo cáo confusion matrix, precision, recall, F1 và các metric phù hợp khác.
- Phân tích lỗi và ghi giới hạn mô hình.

Bàn giao: notebook tái lập được, bảng so sánh thực nghiệm và kết luận có căn cứ.

## Thành viên 3 — Multiclass abuse-type classification

**Notebook:** `notebooks/03_abuse_type_multiclass.ipynb`

Nhiệm vụ:
- Kết hợp feature URL với `abuse_type` và split kế thừa từ dataset chính bằng khóa URL đã thống nhất.
- Phân tích `unknown` và tình trạng mất cân bằng; không được tự ý xóa `unknown` mà không nêu rõ mục tiêu và lý do.
- Xây dựng pipeline multiclass; lựa chọn metric phản ánh cả lớp ít mẫu.
- Đánh giá per-class precision/recall/F1, macro-F1 và confusion matrix; nêu rõ giới hạn của lớp chỉ có rất ít mẫu.
- Kiểm tra leakage và không sử dụng test để điều chỉnh mô hình.

Bàn giao: notebook tái lập được, bảng metric theo lớp và phần thảo luận giới hạn.

## Quy tắc phối hợp

- Thành viên 1 công bố quy tắc khóa URL và kết quả kiểm tra split sớm để hai thành viên còn lại sử dụng thống nhất.
- Mỗi thành viên làm việc trên nhánh riêng và mở Pull Request.
- Thống nhất các thư viện, cách đặt tên artifact và metric trước khi merge kết quả.
- Các notebook trong repo hiện chỉ chứa TODO; không coi đó là kết quả thực nghiệm hay baseline.
