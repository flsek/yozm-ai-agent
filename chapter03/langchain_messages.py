from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI(model="gpt-5-mini")

messages = [
    SystemMessage(content="당신은 사용자의 질문에 간결하고 명확하게 답변하는 AI 도우미입니다."),
    HumanMessage(content="Langchain에 대해 설명해주세요."),
    AIMessage(content="Langchain은 대규모 언어 모델(LLM)을 활용하여 애플리케이션을 구축하기 위한 프레임워크입니다."), # 이전 대화 예시
    HumanMessage(content="주요 기능 세 가지만 알려주세요.") # 사용자의 질문
] # 1) 예제 메시지 목록

result = chat_model.invoke(messages) # 2) 메시지의 리스트를 인자로 넘김
print("AI의 응답 : ", result.content) # 3) 응답은 AIMessage 타입