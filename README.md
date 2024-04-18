# libs

## image.py

### `capture_screen(save_path=None)`
- 스크린 캡처를 수행하고 저장된 파일의 경로를 반환합니다.
- `save_path`가 지정되지 않으면 바탕화면에 저장됩니다.

### `resize_image(file_path)`
- 지정된 이미지 파일의 크기를 사용자의 입력에 따라 조정합니다.
- 조정된 이미지는 원본 파일 경로에 `{width}x{height}.png` 형식의 파일명으로 저장됩니다.

### `png_to_pdf(folder_path)`
- 지정된 폴더 내의 PNG 이미지 파일들을 PDF 파일로 변환하여 저장합니다.
- 사용자에게 PDF 파일 저장 경로를 입력받습니다.

## web.py

### `crawl_website(url)`
- 주어진 URL의 웹 페이지를 크롤링하여 HTML 내용을 반환합니다.

### `open_url(url)`
- 주어진 URL을 Chrome 웹 브라우저에서 열어 브라우저 객체를 반환합니다.

## data.py

### `read_data(file_path)`
- 지원되는 파일 형식(Excel, CSV)의 데이터를 읽어 DataFrame 객체로 반환합니다.

### `show_bar(df, save_path=None)`
- 주어진 DataFrame 객체를 막대 그래프로 시각화합니다.
- `save_path`가 지정되면 그래프를 이미지 파일로 저장합니다.

### `mean_data(df, column_name)`
- 주어진 DataFrame 객체의 특정 열의 평균값을 계산하여 반환합니다.
