import os
from langchain.prompts import load_prompt

# 1) 현재 디렉터리 절대 경로
current_dir_path = os.path.dirname(os.path.abspath(__file__))

# 2) 템플릿 파일 로드
file_prompt = load_prompt(f"{current_dir_path}/template_example.yaml")
print(file_prompt.format(context="서울은 한국 수도이다.", question="수도는?"))