import pandas as pd

def data_transfer(api_result):
    data_list = []

    for group in api_result.get('results', []):
        title = group['title']
        for item in group['data']:
            data_list.append({
                'period': item['period'],
                'category': title,
                'ratio': item['ratio'] # 상대적 검색 비율 (0 ~ 100)
            })

    # 데이터프레임 생성
    df = pd.DataFrame(data_list)

    # 데이터가 정상적으로 있다면 보기 좋게 피벗(가로세로 변환) 적용
    if not df.empty:
        # 날짜를 세로(index)로, 그룹명을 가로(columns)로 배치
        df_pivot = df.pivot(index='period', columns='category', values='ratio').fillna(0)
        return df_pivot
    else:
        # 데이터가 없으면 빈 데이터프레임 반환
        return df