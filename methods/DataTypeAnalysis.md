# Phân tích trong việc thực hiện xử lý file từ ngày 9/3/2024 - 15/3/2024

## Các byte trống trong file là gì
- Các byte trống trong file được định nghĩa có giá trị là <span style="color:red">***0x00***</span> hoặc <span style="color:red">***0x0f***</span>
- Việc thêm hoặc quy định lấy 1 hoặc nhiều bit tại các byte trống có thể không gây ra việc thay đổi nội dung của văn bản đã cho trước
- Các việc cần xử:
  - [x] Xác định phương pháp trích xuất các byte trống trong file
  - [x] Chuẩn bị tập dữ liệu test (100 Files khác nhau và được sắp xếp ngẫu nhiên)
  - [x] Xác định phương pháp xử lí file để tối ưu performance và thời gian thực hiện nhúng từng file
  - [ ] Cài đặt hàm nhúng dữ liệu
  - [ ] Cài đặt hàm trích xuất
  - [ ] Tối ưu độ phức tạp của bài toán để tiết kiệm tài nguyên

## Một số loại file không có byte trống (dựa trên kết quả trên 47 file test mẫu)
- HTML
- Text (.txt)
- Encapsulated PostScript (.eps)
- Excel (.csv)
- Tab-separated values (.tsv)

## Các vấn đề gặp phải khi thực hiện
- Việc phân phối các byte trong token sau khi được chuyển đổi thành dạng byte sẽ gây ra thay đổi đáng để của văn bản khi thực hiện thay thế các byte 0x00
- Chuyển các byte cần được nhúng thành dạng bit để phân bổ vào các byte 0x00 trong văn bản
- Có 2 phương pháp chính khi thực hiện thêm bit và detect bit sau khi nhúng
  - Vị trí nhúng phải động hoặc tĩnh
  - Nếu tĩnh thì trích xuất sao cho phù hợp vì bit 0x00 byte ==> 00000000 (bits) => **Dẫn đến phải hiểu rõ cấu trúc của file và phương thức mã hóa của nó**
  - Cấu trúc file PDF

## Các loại file đã xử lí được nhúng
- File có nội dung là hình ảnh
- Xử lí bằng phương pháp sắp xếp lại bảng màu và thay đổi bằng các màu có khoảng cách euclidean gần nhất
- Phù hợp với ảnh có 256 màu và là 1 dimension có dài rộng bằng nhau (Ví dụ trong lần demo là ảnh gif có kích thước 512x512 và có bảng màu là 256 màu)
- Tính vô hình của phương pháp: cao
- Các điểm cần cải thiện trong: tìm và tối ưu thuật toán sắp xếp màu và cách thức xử lí các byte phù hợp để không gây ra sự thay đổi không đáng có trong kết quả sau khi nhúng token xác thực vào 

## Một số câu hỏi
- Một số tài liệu về làm việc với file?
- Tham khảo ý kiến khi chỉnh sửa thay đổi các giá trị byte rỗng trong file?
- Thống nhất với Thịnh về nội dung và độ dài của token?


## Tài liệu tham khảo
- <a href="https://www.youtube.com/watch?v=GqEH8XvPZwM">What is a PDF?</a>
- <a href="https://youtu.be/K7oxZCgO1dY?si=gR_rwn2JSVWzydEJ">Types of PDF - Computerphile</a>
- <a href="https://youtu.be/9vNdFpjEmXw?si=k1BFVeW8YPuIkp5E">Bits And Bytes | What and Why?</a>
- <a href="https://youtu.be/ixJCo0cyAuA?si=gq4pa1GCi4daatFT">Where did Bytes Come From? - Computerphile</a>
- <a href="https://www.save-emails-as-pdf.com/news/pdf-file-format-internal-document-structure-explained/#:~:text=The%20PDF%20file%20format%20has,the%20author%20of%20the%20file.">PDF file format: Internal Document Structure Explained</a>