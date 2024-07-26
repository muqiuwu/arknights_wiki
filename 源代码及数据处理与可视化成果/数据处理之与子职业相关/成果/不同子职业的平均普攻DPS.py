import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
# 设置中文及字符显示
plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('干员总览.xlsx', sheet_name='Sheet1')
df.head()
df['攻速'] = df['攻速'].str.replace('s', '').astype(float)
df['普攻DPS'] = df['攻击'] / df['攻速']
df_sorted = df.sort_values(by='子职业')
average_dps = (df_sorted.groupby('子职业')['普攻DPS'].mean().reset_index())
average_dps = average_dps.sort_values(by='普攻DPS')
output_file = '干员普攻DPS统计.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    average_dps.to_excel(writer, sheet_name='普攻DPS统计', index=False)
plt.figure(figsize=(80, 40))
plt.bar(average_dps['子职业'], average_dps['普攻DPS'], color='skyblue')
plt.xticks(fontsize=60)
plt.yticks(fontsize=60)
plt.xlabel('子职业',fontsize=60)
plt.ylabel('平均普攻DPS',fontsize=60)
plt.title('不同子职业的平均普攻DPS',fontsize=60)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('平均普攻DPS柱状图.png')
plt.show()