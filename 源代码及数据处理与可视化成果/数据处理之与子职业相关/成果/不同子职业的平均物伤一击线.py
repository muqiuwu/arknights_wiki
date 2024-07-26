import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
# 设置中文及字符显示
plt.rcParams['font.sans-serif'] = 'SimSun'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('干员总览.xlsx', sheet_name='Sheet1')

df['物伤一击线'] = df['血量'] + df['物防']
df_sorted = df.sort_values(by='物伤一击线', ascending=False)#返回一个排序好了的表格
#pd.ExcelWriter 是 Pandas 提供的一个类，用于将多个 DataFrame 写入同一个 Excel 文件。
# output_file 是要输出的 Excel 文件的路径，例如 'output.xlsx'。
# engine='openpyxl' 指定了使用 openpyxl 引擎来写入 Excel 文件，这是 Pandas 支持的一种写入方式。
# as writer 将打开的 ExcelWriter 对象赋给 writer 变量，同时使用 with 语句可以确保在代码块结束时自动关闭文件，这是一种良好的资源管理方式。
output_file = '干员物伤一击线统计.xlsx'#定义一个路径用于保存
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_sorted.to_excel(writer, sheet_name='物伤一击线统计', index=False)
#to_excel() 方法用于将 DataFrame 写入 Excel 文件。
#writer 是之前创建的 ExcelWriter 对象，指定了要写入的 Excel 文件及其配置。
# sheet_name='物伤一击线统计' 指定了要写入的工作表的名称，这里的工作表名为 '物伤一击线统计'。
# index=False 表示不将 DataFrame 的索引写入到 Excel 文件中，如果设为 True，则会将索引作为额外的一列写入。
bins = [0, 1000, 2000, 3000, 4000, 5000, float('inf')]
# float('inf'): 表示正无穷大，是最后一个箱子的上限，表示最后一个箱子包含大于5000的所有数据。

labels = ['0~1000', '1000~2000', '2000~3000', '3000~4000', '4000~5000', '5000以上']
df_sorted['物伤一击线段'] = pd.cut(df_sorted['物伤一击线'], bins=bins, labels=labels, right=False)
#pd.cut()：这是 Pandas 提供的一个函数，用于将数据分段或分箱。
# # 第一个参数 df_sorted['物伤一击线'] 是要分段的数据列
# bins=bins：这个参数定义了分段的边界值，是之前你提供的一个列表 bins，用于指定分箱的区间。
# labels=labels：这个参数是可选的，用于指定每个分箱的标签。这个参数的长度必须与生成的分箱数相同。如果不提供此参数，则返回的结果将是整数分箱的索引。
# right=False：这个参数指示左闭右开的区间，默认为 True（右闭左开）。这意味着默认情况下，分箱的右边界是包含在内的，而左边界是不包含的。通过将 right 设置为 False，分箱变为左闭右开的形式。
pie_data = df_sorted['物伤一击线段'].value_counts()
#.value_counts()：这是 Pandas Series 对象的一个方法，用于计算每个唯一值的出现次数。
# 对于给定列中的每个唯一值，它返回一个 Series，其中索引是唯一值，值是该唯一值在原始 Series 中出现的次数。
plt.figure(figsize=(60, 40))
plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 60})
# startangle 参数用于设置起始绘制角度，即饼图的第一个分片从哪个角度开始。默认情况下，startangle 是0度，从正 x 轴方向开始逆时针绘制。
plt.title('物伤一击线分段统计',fontsize=60,loc='left')
plt.axis('equal')
# plt.axis('equal') 是一个 matplotlib.pyplot 中常用的函数调用，用于确保绘制的图形是在两个轴上具有相同的比例，从而使得图形看起来是正圆形而不是默认的椭圆形。
plt.tight_layout()
plt.savefig('物伤一击线分段饼状图.png')
plt.show()
df_sorted = df.sort_values(by='子职业')
average_dps = (df_sorted.groupby('子职业')['物伤一击线'].mean().reset_index())
# .mean() 方法用于计算数据的均值。当结合 .reset_index() 使用时，它的作用是：
# 计算均值：对数据进行聚合操作，计算每列数据的均值。例如，如果有一个 DataFrame，.mean() 将会返回每列的均值值，对于数值型列，计算每个数值的平均值。
# 重置索引：默认情况下，.mean() 方法返回的结果是一个 Series，其中索引是原始 DataFrame 的列名。
# 使用 .reset_index() 可以将这个 Series 转换回一个 DataFrame，并且重新设置默认的整数索引。
average_dps = average_dps.sort_values(by='物伤一击线')
plt.figure(figsize=(80, 40))
plt.bar(average_dps['子职业'], average_dps['物伤一击线'], color='skyblue')
plt.xticks(fontsize=60)
plt.yticks(fontsize=60)
plt.xlabel('子职业',fontsize=60)
plt.ylabel('平均物伤一击线',fontsize=60)
plt.title('不同子职业的平均物伤一击线',fontsize=60)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('平均物伤一击线柱状图.png')
plt.show()