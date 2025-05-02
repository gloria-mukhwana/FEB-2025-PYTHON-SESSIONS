import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('PANDAS\data.csv')
pd.options.display.max_rows = 999

print(df.head(10))

x = df['Calories'].median()
print(x)
df.fillna(x, inplace=True)
print(df)

a = df['Calories'].mean()
print(a)
b = df['Calories'].sum()
print(b)
c = df['Calories'].max()
print(c)

df_sorted = df.sort_values(by=['Duration', 'Pulse'], ascending=[True, False])
print(df_sorted)

        #SCATTER GRAPH.
df.plot(kind='scatter', x='Duration', y='Calories')
plt.show()

        #HISTOGRAPH.
df['Calories'].plot(kind='hist')
plt.show()

        # PIE CHART.
duration_counts = df['Duration'].value_counts()
plt.pie(duration_counts, labels=duration_counts.index, autopct='%1.1f%%')
plt.title('Duration Distribution')
plt.show()

        #LINE GRAPH.
plt.plot(df['Duration'], df['Calories'])
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.title('Duration vs Calories')
plt.show()
