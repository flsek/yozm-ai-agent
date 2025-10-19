from agents import Agent, Runner, function_tool
from tavily import TavilyClient
import os
import json

# 1) Tavily 클라이언트 (환경변수에서 키를 읽습니다)
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@function_tool()
def news_search(query: str) -> str:
    """
    Tavily를 사용한 뉴스/웹 검색 핸들러
    - 상위 에이전트가 URL 3개를 뽑아가도록, 상위 5건에서 3건만 추립니다.
    - include_answer=True면 요약도 같이 옵니다.
    """
    try:
        resp = tavily_client.search(
            query=query,
            max_results=5,         # 결과 개수
            include_answer=True,   # 요약 포함
            include_images=False,  # 이미지 불필요시 False
            search_depth="basic",  # "basic" | "advanced"
            topic="news",          # "news"로 가중치
            days=7                 # 최근 7일
        )
        # resp 구조 예시: {"answer": "...", "results": [{"title","url","content",...}, ...]}
        results = resp.get("results", [])
        top3 = results[:3]

        lines = [f"🔎 '{query}' 검색 결과 상위 3건"]
        for i, r in enumerate(top3, 1):
            title = r.get("title", "제목 없음")
            url = r.get("url", "")
            snippet = (r.get("content") or "")[:180].replace("\n", " ")
            lines.append(f"{i}. {title}\n   {url}\n   - {snippet}...")
        # 요약이 있으면 덧붙이기
        if resp.get("answer"):
            lines.append("\n📝 요약:")
            lines.append(resp["answer"])
        return "\n".join(lines) if results else "검색 결과가 없습니다."
    except Exception as e:
        # Tavily는 인증/요청 형식 오류 시 에러를 던집니다
        return f"검색 중 오류가 발생했습니다: {e}"

# 2) 에이전트 정의
news_agent = Agent(
    name="NewsSearchAgent",
    model="gpt-5-mini",
    instructions=(
        "당신은 한국어 뉴스 리포터입니다. "
        "news_search 도구를 사용하여 최신 뉴스를 검색하고, "
        "항상 3개의 기사 URL을 함께 알려주세요."
    ),
    tools=[news_search],
)

if __name__ == "__main__":
    print("뉴스 검색 에이전트를 시작합니다.")
    result = Runner.run_sync(
        starting_agent=news_agent,
        input="최신 기술 뉴스 검색해주세요",
    )
    print(result.final_output)