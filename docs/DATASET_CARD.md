# Dataset card

## Tổng quan

Repo hiện sử dụng hai CSV được cung cấp cùng yêu cầu của đồ án. Nguồn xuất bản ban đầu, giấy phép và điều kiện tái phân phối **chưa được xác minh trong repo này**; nhóm cần bổ sung trích dẫn nguồn có thể kiểm tra trước khi phát hành công khai.

### `vn_compphish.csv`

- Kích thước: **53.116 dòng, 28 cột**.
- Trường đích: `label`.
- Các giá trị quan sát được của `label`: `0` = 16.410 dòng; `1` = 36.706 dòng. Cần xác minh định nghĩa nhãn từ nguồn gốc trước khi mô tả chính thức trong báo cáo.
- Phân chia có sẵn: `train` = 36.909; `val` = 7.266; `test` = 8.941.
- Giao nhau split × label:

| Split | label 0 | label 1 | Tổng |
|---|---:|---:|---:|
| train | 11.004 | 25.905 | 36.909 |
| val | 1.561 | 5.705 | 7.266 |
| test | 3.845 | 5.096 | 8.941 |

- Hai giá trị `tld` bị thiếu được quan sát trong bản dữ liệu đã kiểm tra; các cột còn lại không có giá trị thiếu trong lần kiểm tra ban đầu.
- Có các trường URL và feature số như `url_len`, `dom_len`, `is_ip`, `tld_len`, `subdom_cnt`, các bộ đếm ký tự, tỷ lệ ký tự, `is_https`, `entropy`, `path_len`, `query_len`, cùng `split` và `tier`.
- Không dùng `label` và `split` làm đầu vào mô hình. Cần xem xét ý nghĩa của `tier` trước khi quyết định dùng làm feature; không mặc định đưa nó vào mô hình.

### `abuse_type.csv`

- Kích thước: **36.706 dòng, 3 cột** (`url`, `abuse_type`, `rule`).
- Phân bố nhãn quan sát được:

| `abuse_type` | Số dòng |
|---|---:|
| `unknown` | 32.666 |
| `brand_impersonation` | 3.364 |
| `gambling` | 337 |
| `investment` | 284 |
| `betting_stream` | 40 |
| `adult` | 15 |

- `rule` bị thiếu ở 32.666 dòng, trùng với số dòng có nhãn `unknown`. Không được tự động diễn giải `unknown` thành benign; đây là nhãn trong file và ngữ nghĩa cần được xác minh.
- Phân bố nhãn rất mất cân bằng; nên báo cáo precision/recall/F1 theo từng lớp và macro-F1, đồng thời diễn giải thận trọng các lớp quá ít mẫu.

## Quy tắc liên kết hai file

`abuse_type.csv` không có cột `split`. Khi ghép với `vn_compphish.csv`, cần kế thừa split từ dòng phishing tương ứng sau khi chuẩn hóa URL. Kiểm tra khám phá trên phiên bản CSV này cho thấy các khóa URL chuẩn hóa ở các dòng `label == 1` và file `abuse_type.csv` khớp được đầy đủ: 36.706 dòng mỗi bên, tương ứng 19.909 khóa chuẩn hóa duy nhất.

Quy tắc chuẩn hóa cần được triển khai và kiểm tra rõ ràng trong notebook: xử lý URL thiếu scheme, bỏ scheme để ghép, chuẩn hóa chuỗi URL theo quy ước chữ hoa/thường của bộ dữ liệu, chuẩn hóa dấu `/` cuối, và giữ cả tiền tố `www.` lẫn thông tin path/query trong khóa. Trong bản dữ liệu này, giữ `www.` là quan trọng: nếu bỏ `www.` thì các biến thể `www.domain` và `domain` bị gộp, làm giảm số khóa duy nhất từ 36.706 xuống 19.909 và có thể tạo phép ghép many-to-many. Không ghép chỉ theo hostname vì cùng hostname có thể có nhiều URL/path và nhãn khác nhau.

Trong bản kiểm tra hiện tại, chuẩn hóa URL theo quy ước trên cho ra 36.706 khóa duy nhất ở từng file và các khóa khớp đầy đủ giữa các dòng `label == 1` và `abuse_type.csv`. Các khóa chuẩn hóa trong tập phishing không trải qua nhiều split; nhóm vẫn cần tái kiểm chứng bằng kết quả thực thi trong notebook để bảo đảm không có lỗi thay đổi dữ liệu hoặc quy tắc chuẩn hóa.

## Cảnh báo và giới hạn

- Không rõ nguồn gốc/giấy phép chưa có nghĩa là dữ liệu không có giấy phép; cần tra cứu và trích dẫn chính xác trước khi public.
- `unknown` chiếm phần lớn tập multiclass; kết quả mô hình có thể thiên về lớp này.
- Các lớp cực ít mẫu, đặc biệt `adult`, không đủ để đưa ra tuyên bố hiệu năng chắc chắn nếu chỉ dựa trên một lần chia dữ liệu.
- Những đặc trưng được tạo từ URL không chứng minh website còn hoạt động hay đang độc hại ở thời điểm hiện tại.
- Tránh mở trực tiếp các URL trong dataset trên trình duyệt cá nhân. Báo cáo và biểu đồ nên hiển thị an toàn dưới dạng text.
