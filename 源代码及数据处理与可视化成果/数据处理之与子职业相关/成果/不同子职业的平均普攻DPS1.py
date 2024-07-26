import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
# 设置中文及字符显示
plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('干员总览.xlsx', sheet_name='Sheet1')
df['法伤一击线'] = df['血量'] / (1 - df['法防'] * 0.01)
df_sorted = df.sort_values(by='法伤一击线', ascending=False)
output_file = '干员法伤一击线统计.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_sorted.to_excel(writer, sheet_name='法伤一击线统计', index=False)
bins = [0, 1000, 2000, 3000, 4000, 5000, float('inf')]
labels = ['0~1000', '1000~2000', '2000~3000', '3000~4000', '4000~5000', '5000以上']
df_sorted['法伤一击线段'] = pd.cut(df_sorted['法伤一击线'], bins=bins, labels=labels, right=False)
pie_data = df_sorted['法伤一击线段'].value_counts()
plt.figure(figsize=(60, 40))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 60})
plt.title('法伤一击线分段统计',fontsize=60,loc='left')
plt.axis('equal')
plt.tight_layout()
plt.savefig('法伤一击线分段饼状图.png')
plt.show()
df_sorted = df.sort_values(by='子职业')
average_dps = (df_sorted.groupby('子职业')['法伤一击线'].mean().reset_index())
average_dps = average_dps.sort_values(by='法伤一击线')
plt.figure(figsize=(80, 40))
plt.bar(average_dps['子职业'], average_dps['法伤一击线'], color='skyblue')
plt.xticks(fontsize=60)
plt.yticks(fontsize=60)
plt.xlabel('子职业',fontsize=60)
plt.ylabel('平均法伤一击线',fontsize=60)
plt.title('不同子职业的平均法伤一击线',fontsize=60)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('平均法伤一击线柱状图.png')
plt.show()