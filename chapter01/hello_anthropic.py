import anthropic

client = anthropic.Anthropic()

# 1) 대화 기록을 저장할 리스트
conversation = []

# 사용자 입력 추가
conversation.append({"role":"user", "content":"안녕 나는 다연이야."})

# 2) 클로드 호출
response = client.messages.create(
    model="claude-3-5-haiku-latest",
    max_tokens=1000,
    messages=conversation
)

# 3) 응답 출력 및 대화 기록에 추가
assistant_message = response.content[0].text
print(assistant_message)
conversation.append({
    "role":"user", "content":assistant_message
})

# 4) 다음 사용자 입력
conversation.append({
    "role":"user", "content": "내 이름이 뭐라고?"
})

# 다시 클로드 호출
response = client.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=1000,
    messages=conversation
)

# 5) 두 번째 응답 출력
print(response.content[0].text)