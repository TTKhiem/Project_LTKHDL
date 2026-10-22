# Phishing URL Detection & Abuse-Type Classification

Đồ án phân tích dữ liệu và học máy với hai mục tiêu: (1) phân loại URL phishing/benign và (2) phân loại nhóm abuse của các URL được gắn nhãn phishing.

> **Trạng thái:** Khung repo ban đầu. Các notebook chỉ có kế hoạch và `TODO`, chưa cài đặt lời giải hoặc code mẫu. Mỗi thành viên tự hoàn thiện phần được phân công.

## Mục tiêu

1. Kiểm tra chất lượng dữ liệu, hiểu feature và nhãn, xác minh cách ghép hai bộ dữ liệu.
2. Huấn luyện và đánh giá mô hình binary classification với các tập `train`, `val`, `test` đã được cung cấp.
3. Huấn luyện và đánh giá mô hình multiclass cho `abuse_type`, đồng thời phân tích ảnh hưởng của mất cân bằng lớp.
4. Ghi lại quy trình, kết quả, giới hạn và khả năng tái lập thí nghiệm.

## Cấu trúc thư mục

```text
Project_LTKHDL_Phishing/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── data/
│   ├── raw/                 # Hai CSV đầu vào
│   └── processed/           # Dữ liệu trung gian do nhóm tạo
├── docs/                    # Dataset card, workflow và phân công
├── models/                  # Lưu model đã train (mặc định không commit)
├── notebooks/               # Mỗi thành viên phụ trách một notebook
├── reports/
│   ├── figures/
│   └── tables/
├── src/                     # Mã nguồn dùng chung do nhóm tự triển khai
├── .editorconfig
├── .gitignore
├── CONTRIBUTING.md
└── requirements.txt
```

## Dữ liệu

- `data/raw/vn_compphish.csv`: 53.116 dòng, 28 cột; có `label` và `split`.
- `data/raw/abuse_type.csv`: 36.706 dòng, 3 cột; có `url`, `abuse_type`, `rule`.
- Mô tả nhãn, phân bố và lưu ý ghép dữ liệu: [`docs/DATASET_CARD.md`](docs/DATASET_CARD.md).

**Lưu ý:** Trước khi công khai repo, nhóm cần xác minh nguồn gốc, cách trích dẫn và quyền tái phân phối của hai file dữ liệu. Việc file đang có trong repo không tự động có nghĩa là dữ liệu được phép phát hành công khai.

## Thiết lập môi trường

Khuyến nghị Python 3.10 trở lên. Từ thư mục gốc repo, chạy trong PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name project-ltkhdl-phishing --display-name "Python (Project LTKHDL Phishing)"
jupyter notebook
```

Trên macOS/Linux, tạo và kích hoạt môi trường ảo theo lệnh phù hợp với hệ điều hành.

## Thứ tự làm việc

1. Đọc [`docs/TEAM_TASKS.md`](docs/TEAM_TASKS.md) và [`CONTRIBUTING.md`](CONTRIBUTING.md).
2. Thành viên 1 hoàn thiện `01_data_audit_and_join.ipynb`, ghi lại quy tắc chuẩn hóa URL và xác minh split.
3. Thành viên 2 hoàn thiện `02_binary_phishing_classifier.ipynb`.
4. Thành viên 3 hoàn thiện `03_abuse_type_multiclass.ipynb`.
5. Mỗi notebook phải ghi rõ cách tạo kết quả, metric, giới hạn và kết luận; không chỉ nộp mỗi điểm số.
6. Review notebook của nhau trước khi merge vào `main`.

## Quy ước quan trọng

- Không tự chia lại dữ liệu binary khi chưa có lý do được nhóm thống nhất; sử dụng cột `split` có sẵn.
- Không đưa `label` hoặc `split` vào feature của mô hình binary.
- Không ghép multiclass chỉ bằng hostname; cần chuẩn hóa URL theo quy tắc thống nhất và giữ lại path/query khi tạo khóa ghép.
- Không đánh giá mô hình multiclass chỉ bằng accuracy vì các lớp mất cân bằng mạnh.
- Không commit môi trường ảo, model lớn, file cache hoặc output sinh tự động.

## Phân công

Xem [`docs/TEAM_TASKS.md`](docs/TEAM_TASKS.md).
