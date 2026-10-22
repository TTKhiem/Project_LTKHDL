# Quy trình thực nghiệm tối thiểu

1. Giữ nguyên hai file gốc trong `data/raw/`.
2. Hoàn tất audit và ghi lại các giả định về nhãn, split, URL key và `tier`.
3. Dùng split có sẵn cho binary. Dùng split được kế thừa qua URL key đã kiểm chứng cho multiclass.
4. Fit mọi phép biến đổi (imputation, encoding, scaling, feature selection...) chỉ trên tập train thông qua pipeline phù hợp.
5. Sử dụng validation cho quyết định về mô hình và siêu tham số.
6. Sau khi chốt mô hình, đánh giá trên test một lần; không quay lại điều chỉnh mô hình dựa trên kết quả test.
7. Ghi seed, feature đã dùng, phiên bản thư viện, metric và các giới hạn.
8. Chỉ thêm model/đồ thị được chọn vào repo khi nhóm thấy cần thiết và đảm bảo artifact không quá lớn.
