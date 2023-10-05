import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sample_data.csv')
new_data = df.pivot_table('Sale_Amount', 'Date', ['Portal'], aggfunc={'Sale_Amount': 'sum'})
print(new_data)
new_data.plot(kind="line", title="My plot", label='Sale_Amount', legend=True)
plt.show()
