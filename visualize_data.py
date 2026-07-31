import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./csv/5_trends_data.csv")

print(df.columns)
print(df.head())

plt.plot(df['period'], df['국내여행/레저'], df['스몰럭셔리/경험'], df['절약/짠테크'], df['해외여행'], df['헬시플레저/건강'], marker='o', color='b', label='트렌드')
plt.rc('font', family='Malgun Gothic')

plt.title('5 Trends Data')
plt.xlabel('Data')
plt.ylabel('Value')
plt.legend()
plt.grid(True)

plt.show()