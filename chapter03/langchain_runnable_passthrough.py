from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template(
    "주어진 '{word}'와 유사한 단어 3가지를 나열해주세요. 단어만 나열합니다."
)
model = ChatOpenAI(model="gpt-5-mini")
parser = StrOutputParser()

# 1) 병렬 처리 체인 구성
chain = RunnableParallel(
    {
        "original" : RunnablePassthrough(), # 2) 원본 보존
        "processed" : prompt | model | parser, # 3) 처리된 데이터
    }
)

result = chain.invoke({"word" : "행복"})
print(result)