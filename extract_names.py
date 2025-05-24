
import pandas as pd

# 엑셀 파일 불러오기
df = pd.read_excel("sample.xlsx")

# 이름만 추출
names = df['이름']

# 이름을 텍스트 파일로 저장
names.to_csv("output_names.txt", index=False, header=False)

print("이름이 output_names.txt 파일에 저장되었습니다.")
