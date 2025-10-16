from openai import OpenAI

client = OpenAI()

# 1) previous_response_id 파라미터 추가
def chatbot_response(user_message: str, previous_response_id=None):
    result = client.responses.create(
        # 2) previous_response_id 파라미터에 이전 대화의 id값을 넘겨준다.
        model="gpt-5-mini", input=user_message, previous_response_id=previous_response_id)
    return result

if __name__ == "__main__":
    previous_response_id = None
    while True:
        user_message = input("메시지: ")
        if user_message.lower() == "exit":
            print("대화를 종료합니다.")
            break
        
        # 3) 이전 대화의 id 값을 추가로 넘겨준다.
        result = chatbot_response(user_message, previous_response_id)
        # 4) 이전 대화의 id를 response_id에 할당
        previous_response_id = result.id
        print("챗봇: " + result.output_text)