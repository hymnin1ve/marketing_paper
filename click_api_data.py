import json
import urllib.request
import urllib.error

from data_to_pandas import data_transfer

client_id = "xmjeuj3xd2"
client_secret = "r8hmrUXrbKsbqziSIJR9sATy61CM6w4q9qB9f72K"

url = "https://naverapihub.apigw.ntruss.com/search-trend/v1/search"

headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/json"
}

body = json.dumps({
    "startDate": "2023-08-01",
    "endDate": "2026-08-01",
    "timeUnit": "month",
    "keywordGroups": [
        {
            "groupName": "실속소비",
            "keywords": ["당근마켓", "번개장터", "테무"]
        },
        {
            "groupName": "디저트",
            "keywords": ["요아정", "두바이 초콜릿", "두바이 쫀득쿠키"]
        }
    ]
})

try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        print("데이터 수집 성공! 👏")
        response_body = response.read().decode('utf-8')
        raw_result = json.loads(response_body)

        final_df = data_transfer(raw_result)

        print("\n[변환된 데이터 미리보기]")
        print(final_df.head())

        csv_name = "4_click_data.csv"
        
        final_df.to_csv(csv_name, encoding='utf-8-sig')
        print(f"\n데이터가 {csv_name} 파일로 예쁘게 저장되었습니다!")

except urllib.error.HTTPError as e:
    print(f"API 호출 실패! 에러 코드: {e.code}")
    print(f"에러 메시지: {e.read().decode('utf-8')}")
except Exception as e:
    print(f"알 수 없는 에러 발생: {e}")