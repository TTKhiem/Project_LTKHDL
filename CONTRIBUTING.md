# Hướng dẫn đóng góp

## Cách làm việc với Git

1. Đồng bộ nhánh `main` trước khi bắt đầu.
2. Tạo nhánh riêng cho nhiệm vụ, ví dụ `feature/data-audit`, `feature/binary-model`, hoặc `feature/abuse-model`.
3. Chỉ chỉnh sửa notebook/tài liệu liên quan đến nhiệm vụ đang làm.
4. Chạy lại notebook từ đầu đến cuối trước khi tạo Pull Request; kiểm tra không còn đường dẫn phụ thuộc máy cá nhân.
5. Tạo Pull Request vào `main`, mô tả thay đổi, kết quả kiểm tra và các điểm cần thành viên khác review.
6. Không tự ý sửa hoặc xóa dữ liệu gốc trong `data/raw/`.

## Quy ước commit

Nên dùng thông điệp ngắn, nói rõ thay đổi, ví dụ:

- `docs: describe dataset and split policy`
- `feat: complete binary classification experiments`
- `feat: add abuse type evaluation`
- `fix: correct URL normalization checks`

## Yêu cầu khi hoàn thiện notebook

- Có mục tiêu, bước thực hiện và kết luận.
- Giải thích các quyết định quan trọng, không chỉ đưa code và số liệu.
- Nêu rõ split sử dụng, metric và cách chọn mô hình.
- Không dùng test set để lựa chọn feature hoặc tinh chỉnh mô hình.
- Ghi nhận dữ liệu thiếu, trùng lặp, mất cân bằng và các hạn chế liên quan.
- Không commit output/plot không cần thiết hoặc thông tin đường dẫn riêng trên máy cá nhân.

## Review chéo

Mỗi thành viên cần review ít nhất một notebook do thành viên khác thực hiện. Khi góp ý, tập trung vào tính đúng đắn, khả năng tái lập, leakage, tính phù hợp của metric và cách diễn giải kết quả.
