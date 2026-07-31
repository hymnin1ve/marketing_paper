import requests
import json
from data_to_pandas import data_transfer

# 1. 발급받은 API 키 입력
CLIENT_ID = "dkMDoNKT_2o4cfsiSYPW"        
CLIENT_SECRET = "xFlwTm8J0K" 

# 2. 데이터랩 API URL (검색어 트렌드)
url = "https://openapi.naver.com/v1/datalab/search"

# 3. 요청 헤더(Header) 설정
headers = {
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_SECRET,
    "Content-Type": "application/json"
}

#4. 5대 소비 트렌드 통합 body
body = {
    "startDate": "2024-01-01",  # 최근 2년~최신 트렌드 분석 추천
    "endDate": "2026-06-30",
    "timeUnit": "month",
    "keywordGroups": [
        # [2번 종합] 헬시플레저 & 건강 소비
        {
            "groupName": "헬시플레저/건강",
            "keywords": ["제로슈가", "제로음료", "저당", "단백질음료", "프로틴", "유산균", "홈트레이닝"]
        },
        # [3번-A] 불황형 절약 소비 (짠테크)
        {
            "groupName": "절약/짠테크",
            "keywords": ["앱테크", "무지출", "가성비", "중고거래", "당근마켓", "알뜰폰"]
        },
        # [3번-B] 쾌락형/경험 소비 (스몰럭셔리)
        {
            "groupName": "스몰럭셔리/경험",
            "keywords": ["두바이초콜릿", "프리미엄디저트", "오마카세", "팝업스토어", "플래그십스토어"]
        },
        # [4번-A] 해외 여가 소비
        {
            "groupName": "해외여행",
            "keywords": ["해외항공권", "해외호텔", "일본여행", "동남아여행", "환전"]
        },
        # [4번-B] 국내 여가 & 야외 레저 소비
        {
            "groupName": "국내여행/레저",
            "keywords": ["국내호텔", "호캉스", "캠핑", "글램핑", "차박", "등산"]
        }
    ],
    "device": "",  # 전체 _ pc, mo (빈칸이면 전체)
    "gender": "",  # 전체
    "ages": []     # 전체
}

# 5. API 호출 (POST 방식)
response = requests.post(url, headers=headers, data=json.dumps(body))

# 6. 결과 확인
if response.status_code == 200:
    print("데이터 수집 성공! 👏")
    raw_result = response.json()

    final_df = data_transfer(raw_result)

    print("\n[변환된 데이터 미리보기]")
    print(final_df.head())

    csv_name = "5_trends_data.csv"
    
    final_df.to_csv(csv_name, encoding='utf-8-sig')
    print(f"\n데이터가 {csv_name} 파일로 예쁘게 저장되었습니다!")
else:
    print(f"API 호출 실패! 에러 코드: {response.status_code}")
    print(response.text)