# yozm-ai-agent

OpenAI API를 활용한 간단한 AI 챗봇 프로젝트입니다.

## 프로젝트 설명

이 프로젝트는 OpenAI의 Chat Completion API를 사용하여 사용자의 질문에 응답하는 AI 비서를 구현합니다.

## 파일 구조

- `hello_openai.py`: OpenAI API를 사용한 챗봇 메인 프로그램
- `hello.py`: 기본 Hello World 예제
- `.env`: 환경 변수 설정 파일 (API 키 포함)

## 설치 방법

1. 저장소 클론
```bash
git clone <repository-url>
cd yozm-ai-agent
```

2. 필요한 패키지 설치
```bash
pip install openai python-dotenv
```

3. 환경 변수 설정

`.env` 파일을 생성하고 OpenAI API 키를 추가합니다:
```
OPENAI_API_KEY=your_api_key_here
```

## 사용 방법

```bash
python hello_openai.py
```

프로그램을 실행하면 질문을 입력할 수 있으며, AI가 응답을 생성합니다.

## 주요 기능

- OpenAI Chat Completion API 연동
- 환경 변수를 통한 안전한 API 키 관리
- 사용자 입력 기반 대화형 인터페이스

## 요구 사항

- Python 3.7+
- openai
- python-dotenv

## 라이선스

MIT
